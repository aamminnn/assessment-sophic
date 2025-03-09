from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

@app.route('/')
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    tasks = load_tasks()
    new_task = request.form.get("task")
    new_hour = request.form.get("hour")
    if new_task and new_hour:
        tasks.append({"description": new_task, "expected_hours":new_hour ,"completed": False})
        save_tasks(tasks)
    return redirect(url_for("index"))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    tasks = load_tasks()
    if request.method == 'POST':
        new_description = request.form.get("task")
        new_hour = request.form.get("hour")
        if new_description and new_hour:
            tasks[task_id]["description"] = new_description
            tasks[task_id]["expected_hours"] = new_hour
            save_tasks(tasks)
        return redirect(url_for("index"))
    return render_template("edit.html", task=tasks[task_id], task_id=task_id)

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = True
        save_tasks(tasks)
    return redirect(url_for("index"))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True)
