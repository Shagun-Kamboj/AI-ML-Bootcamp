from flask import Flask, render_template, request, redirect, url_for, session
from datetime import date

from models.models import db
from models.user import User
from models.task import Task
from models.gemini_ai import (
    generate_task_plan,
    generate_dashboard_insights,
    generate_schedule,
    ask_task_question
)


app = Flask(__name__)

# =====================================
# Secret Key
# =====================================

app.secret_key = "ai_task_manager_secret"

# =====================================
# Database Configuration
# =====================================

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# =====================================
# HOME
# =====================================

@app.route("/")
def home():
    return render_template("index.html")

# =====================================
# LOGIN
# =====================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(
            email=email,
            password=password
        ).first()

        if user:

            session["user_name"] = user.name

            return redirect(url_for("dashboard"))

        else:

            return "Invalid Email or Password"

    return render_template("login.html")

# =====================================
# REGISTER
# =====================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        new_user = User(

            name=request.form["name"],
            email=request.form["email"],
            password=request.form["password"]

        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")
# =====================================
# DASHBOARD
# =====================================

@app.route("/dashboard")
def dashboard():

    # Check Login
    if "user_name" not in session:
        return redirect(url_for("login"))

    name = session.get("user_name", "User")

    # Fetch Tasks
    tasks = Task.query.order_by(Task.id.desc()).all()

    # AI Dashboard Insights
    try:
        ai_insights = generate_dashboard_insights(tasks)
    except Exception:
        ai_insights = """
### 🤖 AI Assistant

Welcome!

Create your first task to receive:

* Productivity Score
* Deadline Analysis
* Smart Recommendations
* Workload Prediction
"""

    # Statistics
    total_tasks = len(tasks)

    completed = Task.query.filter_by(
        status="Completed"
    ).count()

    pending = Task.query.filter_by(
        status="Pending"
    ).count()

    overdue = 0

    today = date.today()

    for task in tasks:

        try:

            task_date = date.fromisoformat(task.deadline)

            if (
                task.status != "Completed"
                and task_date < today
            ):
                overdue += 1

        except Exception:
            pass

    return render_template(

        "dashboard.html",

        name=name,

        tasks=tasks,

        total_tasks=total_tasks,

        completed=completed,

        pending=pending,

        overdue=overdue,

        ai_insights=ai_insights

    )
# =====================================
# ADD TASK
# =====================================

@app.route("/add_task", methods=["GET", "POST"])
def add_task():

    if "user_name" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]
        priority = request.form["priority"]
        deadline = request.form["deadline"]

        # Generate AI Task Plan
        try:

            ai_plan = generate_task_plan(
                title,
                description
            )

        except Exception:

            ai_plan = """
Unable to generate AI recommendation.

Please try again later.
"""

        new_task = Task(

            title=title,
            description=description,
            priority=priority,
            deadline=deadline,
            status="Pending",
            ai_plan=ai_plan

        )

        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for("view_tasks"))

    return render_template("add_task.html")


# =====================================
# VIEW TASKS
# =====================================

@app.route("/view_tasks")
def view_tasks():

    if "user_name" not in session:
        return redirect(url_for("login"))

    tasks = Task.query.order_by(
        Task.id.desc()
    ).all()

    return render_template(
        "view_tasks.html",
        tasks=tasks
    )


# =====================================
# EDIT TASK
# =====================================

@app.route("/edit_task/<int:id>", methods=["GET", "POST"])
def edit_task(id):

    if "user_name" not in session:
        return redirect(url_for("login"))

    task = Task.query.get_or_404(id)

    if request.method == "POST":

        task.title = request.form["title"]
        task.description = request.form["description"]
        task.priority = request.form["priority"]
        task.deadline = request.form["deadline"]
        task.status = request.form["status"]

        db.session.commit()

        return redirect(url_for("view_tasks"))

    return render_template(
        "edit_task.html",
        task=task
    )
# =====================================
# AI PLAN
# =====================================

@app.route("/ai_plan/<int:id>")
def ai_plan(id):

    if "user_name" not in session:
        return redirect(url_for("login"))

    task = Task.query.get_or_404(id)

    return render_template(
        "ai_plan.html",
        task=task
    )


# =====================================
# AI CHAT
# =====================================

@app.route("/ai_chat/<int:id>", methods=["GET", "POST"])
def ai_chat(id):

    if "user_name" not in session:
        return redirect(url_for("login"))

    task = Task.query.get_or_404(id)

    answer = ""

    if request.method == "POST":

        question = request.form["question"]

        try:

            answer = ask_task_question(
                task,
                question
            )

        except Exception:

            answer = """
❌ Unable to connect to Gemini AI.

Please try again later.
"""

    return render_template(

        "ai_chat.html",

        task=task,

        answer=answer

    )
# =====================================
# AI PLAN
# =====================================


# AI CHAT
# ====================================
# AI SMART SCHEDULE
# =====================================

@app.route("/ai_schedule/<int:id>")
def ai_schedule(id):

    if "user_name" not in session:
        return redirect(url_for("login"))

    task = Task.query.get_or_404(id)

    try:
        schedule = generate_schedule(task)

    except Exception as e:
        schedule = f"❌ Gemini Error: {str(e)}"

    return render_template(
        "ai_schedule.html",
        task=task,
        schedule=schedule
    )


# =====================================
# DELETE TASK
# =====================================

@app.route("/delete_task/<int:id>")
def delete_task(id):

    if "user_name" not in session:
        return redirect(url_for("login"))

    task = Task.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()

    return redirect(url_for("view_tasks"))


# =====================================
# USERS
# =====================================

@app.route("/users")
def users():

    if "user_name" not in session:
        return redirect(url_for("login"))

    all_users = User.query.all()

    return render_template(
        "users.html",
        users=all_users
    )


# =====================================
# LOGOUT
# =====================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


# =====================================
# RUN APP
# =====================================

if __name__ == "__main__":

    app.run(
        debug=True
    )