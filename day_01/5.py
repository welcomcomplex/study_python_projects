data = {"name": "Alice", "scores": [95, 87]}
grade = data.get("grade", "Not Available")

def add_item(item, items_list=None):
    if items_list is None:
        items_list = []
    items_list.append(item)
    return items_list

users = [
    {"name": "Alice", "dept": "AI"},
    {"name": "Bob", "dept": "Backend"},
    {"name": "Charlie", "dept": "AI"}
]
from collections import defaultdict
dept_users = defaultdict(list)
for user in users:
    dept_users[user["dept"]].append(user["name"])
    
