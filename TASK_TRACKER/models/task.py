from models.models import db

class Task(db.Model):
    _tablename_ = "tasks"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)

    description = db.Column(db.Text, nullable=False)

    priority = db.Column(db.String(20), nullable=False)

    deadline = db.Column(db.String(30), nullable=False)

    status = db.Column(db.String(20), default="Pending")

    ai_plan = db.Column(db.Text)