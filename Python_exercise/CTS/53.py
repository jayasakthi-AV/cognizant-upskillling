from datetime import datetime

tasks = [
    {"task": "Project", "due": "2026-06-10"},
    {"task": "Assignment", "due": "2026-06-05"}
]

tasks.sort(key=lambda x: x["due"])

for task in tasks:
    print(task["task"], "-", task["due"])