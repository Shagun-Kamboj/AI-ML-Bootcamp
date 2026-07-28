import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
#API_KEY = os.getenv("AQ.Ab8RN6LwfnhFTkzeAaKocG9FdFFSE3Aj0-Q_3b51PXWrG_o9Gg")

print("API KEY FOUND:", API_KEY is not None)

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3.5-flash")
try:
    test = model.generate_content("Hello")
    print("GEMINI TEST SUCCESS")
except Exception as e:
    print("GEMINI TEST FAILED:", e)
# =====================================
# TASK PLAN
# =====================================

def generate_task_plan(title, description):

    prompt = f"""
You are an expert productivity planner and study mentor.

Task Title:
{title}

Task Description:
{description}

Analyze the task deeply.

Requirements:

1. Understand the complete task.
2. Break it into smaller actionable steps.
3. Assign High, Medium and Low priority.
4. Arrange tasks in logical order.
5. Create a realistic execution roadmap.
6. Estimate required time.
7. Mention milestones.
8. Suggest completion strategy.
9. If syllabus, chapters, topics, modules or units are given,
   prioritize difficult and important topics first.
10. Create a smart sequence for learning.

Output Format:

📌 TASK ANALYSIS

🔥 HIGH PRIORITY TASKS

⚡ MEDIUM PRIORITY TASKS

🟢 LOW PRIORITY TASKS

📅 DAILY EXECUTION PLAN

⏰ TIME ESTIMATION

🎯 COMPLETION STRATEGY

✅ FINAL RECOMMENDATION
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
            print("GEMINI ERROR:", e)
            return f"Gemini Error: {str(e)}"


# =====================================
# DASHBOARD INSIGHTS
# =====================================

def generate_dashboard_insights(tasks):

    if not tasks:
        return """
🤖 AI Dashboard

No tasks found.

Create tasks to receive:

* Productivity Score
* Deadline Analysis
* Smart Recommendations
* Workload Forecast
"""

    task_text = ""

    for task in tasks:

        task_text += f"""
Title: {task.title}
Priority: {task.priority}
Status: {task.status}
Deadline: {task.deadline}

"""

    prompt = f"""
Analyze the following tasks.

Provide:

1. Productivity Score (0-100)
2. Workload Analysis
3. Deadline Risks
4. Smart Suggestions
5. Priority Improvements
6. Productivity Tips

Tasks:

{task_text}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
     print("GEMINI ERROR:", e)
     return f"Gemini Error: {str(e)}"

# =====================================
# AI SCHEDULE
# =====================================

def generate_schedule(task):

    prompt = f"""
You are an AI Scheduler.

Task Title:
{task.title}

Description:
{task.description}

Priority:
{task.priority}

Deadline:
{task.deadline}

Create a complete schedule.

Requirements:

1. Divide task day-wise.
2. Prioritize important topics first.
3. Mention estimated hours.
4. Add revision time.
5. Ensure completion before deadline.
6. Keep schedule practical.

Output Format:

📅 Day 1
- Work
- Hours

📅 Day 2
- Work
- Hours

📅 Day 3
- Work
- Hours

🎯 Final Revision Day

✅ Completion Summary
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print("GEMINI ERROR:", e)
        return f"Gemini Error: {str(e)}"

# =====================================
# AI CHAT
# =====================================

def ask_task_question(task, question):

    prompt = f"""
Task Title:
{task.title}

Task Description:
{task.description}

User Question:
{question}

Give a clear and helpful answer.
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
#API_KEY = os.getenv("AQ.Ab8RN6LwfnhFTkzeAaKocG9FdFFSE3Aj0-Q_3b51PXWrG_o9Gg")

print("API KEY FOUND:", API_KEY is not None)

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3.5-flash")

# =====================================
# TASK PLAN
# =====================================

def generate_task_plan(title, description):

    prompt = f"""
You are an expert productivity planner and study mentor.

Task Title:
{title}

Task Description:
{description}

Analyze the task deeply.

Requirements:

1. Understand the complete task.
2. Break it into smaller actionable steps.
3. Assign High, Medium and Low priority.
4. Arrange tasks in logical order.
5. Create a realistic execution roadmap.
6. Estimate required time.
7. Mention milestones.
8. Suggest completion strategy.
9. If syllabus, chapters, topics, modules or units are given,
   prioritize difficult and important topics first.
10. Create a smart sequence for learning.

Output Format:

📌 TASK ANALYSIS

🔥 HIGH PRIORITY TASKS

⚡ MEDIUM PRIORITY TASKS

🟢 LOW PRIORITY TASKS

📅 DAILY EXECUTION PLAN

⏰ TIME ESTIMATION

🎯 COMPLETION STRATEGY

✅ FINAL RECOMMENDATION
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
            print("GEMINI ERROR:", e)
            return f"Gemini Error: {str(e)}"


# =====================================
# DASHBOARD INSIGHTS
# =====================================

def generate_dashboard_insights(tasks):

    if not tasks:
        return """
🤖 AI Dashboard

No tasks found.

Create tasks to receive:

* Productivity Score
* Deadline Analysis
* Smart Recommendations
* Workload Forecast
"""

    task_text = ""

    for task in tasks:

        task_text += f"""
Title: {task.title}
Priority: {task.priority}
Status: {task.status}
Deadline: {task.deadline}

"""

    prompt = f"""
Analyze the following tasks.

Provide:

1. Productivity Score (0-100)
2. Workload Analysis
3. Deadline Risks
4. Smart Suggestions
5. Priority Improvements
6. Productivity Tips

Tasks:

{task_text}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
     print("GEMINI ERROR:", e)
     return f"Gemini Error: {str(e)}"

# =====================================
# AI SCHEDULE
# =====================================

def generate_schedule(task):

    prompt = f"""
You are an AI Scheduler.

Task Title:
{task.title}

Description:
{task.description}

Priority:
{task.priority}

Deadline:
{task.deadline}

Create a complete schedule.

Requirements:

1. Divide task day-wise.
2. Prioritize important topics first.
3. Mention estimated hours.
4. Add revision time.
5. Ensure completion before deadline.
6. Keep schedule practical.

Output Format:

📅 Day 1
- Work
- Hours

📅 Day 2
- Work
- Hours

📅 Day 3
- Work
- Hours

🎯 Final Revision Day

✅ Completion Summary
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print("GEMINI ERROR:", e)
        return f"Gemini Error: {str(e)}"

# =====================================
# AI CHAT
# =====================================

def ask_task_question(task, question):

    prompt = f"""
Task Title:
{task.title}

Task Description:
{task.description}

User Question:
{question}

Give a clear and helpful answer.
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
#API_KEY = os.getenv("AQ.Ab8RN6LwfnhFTkzeAaKocG9FdFFSE3Aj0-Q_3b51PXWrG_o9Gg")

print("API KEY FOUND:", API_KEY is not None)

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3.5-flash")

# =====================================
# TASK PLAN
# =====================================

def generate_task_plan(title, description):

    prompt = f"""
You are an expert productivity planner and study mentor.

Task Title:
{title}

Task Description:
{description}

Analyze the task deeply.

Requirements:

1. Understand the complete task.
2. Break it into smaller actionable steps.
3. Assign High, Medium and Low priority.
4. Arrange tasks in logical order.
5. Create a realistic execution roadmap.
6. Estimate required time.
7. Mention milestones.
8. Suggest completion strategy.
9. If syllabus, chapters, topics, modules or units are given,
   prioritize difficult and important topics first.
10. Create a smart sequence for learning.

Output Format:

📌 TASK ANALYSIS

🔥 HIGH PRIORITY TASKS

⚡ MEDIUM PRIORITY TASKS

🟢 LOW PRIORITY TASKS

📅 DAILY EXECUTION PLAN

⏰ TIME ESTIMATION

🎯 COMPLETION STRATEGY

✅ FINAL RECOMMENDATION
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
            print("GEMINI ERROR:", e)
            return f"Gemini Error: {str(e)}"


# =====================================
# DASHBOARD INSIGHTS
# =====================================

def generate_dashboard_insights(tasks):

    if not tasks:
        return """
🤖 AI Dashboard

No tasks found.

Create tasks to receive:

* Productivity Score
* Deadline Analysis
* Smart Recommendations
* Workload Forecast
"""

    task_text = ""

    for task in tasks:

        task_text += f"""
Title: {task.title}
Priority: {task.priority}
Status: {task.status}
Deadline: {task.deadline}

"""

    prompt = f"""
Analyze the following tasks.

Provide:

1. Productivity Score (0-100)
2. Workload Analysis
3. Deadline Risks
4. Smart Suggestions
5. Priority Improvements
6. Productivity Tips

Tasks:

{task_text}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
     print("GEMINI ERROR:", e)
     return f"Gemini Error: {str(e)}"

# =====================================
# AI SCHEDULE
# =====================================

def generate_schedule(task):

    prompt = f"""
You are an AI Scheduler.

Task Title:
{task.title}

Description:
{task.description}

Priority:
{task.priority}

Deadline:
{task.deadline}

Create a complete schedule.

Requirements:

1. Divide task day-wise.
2. Prioritize important topics first.
3. Mention estimated hours.
4. Add revision time.
5. Ensure completion before deadline.
6. Keep schedule practical.

Output Format:

📅 Day 1

Work:
...

Hours:
...

--------------------------------

📅 Day 2

Work:
...

Hours:
...

--------------------------------

📅 Day 3

Work:
...

Hours:
...

--------------------------------

🎯 Final Revision Day

...

✅ Completion Summary
✅ Completion Summary
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print("GEMINI ERROR:", e)
        return f"Gemini Error: {str(e)}"

# =====================================
# AI CHAT
# =====================================

def ask_task_question(task, question):

    prompt = f"""
Task Title:
{task.title}

Task Description:
{task.description}

User Question:
{question}

Give a clear and helpful answer.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print("GEMINI ERROR:", e)
        return f"Gemini Error: {str(e)}"