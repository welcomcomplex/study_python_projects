# ❌ 危险代码（会出什么问题？）
f = open("config.txt")
content = f.read()
f.close()

with open("config.txt", encoding="utf-8") as f:
    content = f.read()  

import json
with open("config.json", encoding="utf-8") as f:
    content = f.read()
    config = json.loads(content)

with open("sever.log", encoding="utf-8") as f:
    for line in f:
        if "CRITICAL" in line:
            print(line)

def get_line(filepath: str, line_number: int) -> str:
    with open(filepath, encoding="utf-8") as f:
        for current_line_number, line in enumerate(f, start=1):
            if current_line_number == line_number:
                return line
    raise ValueError(f"Line {line_number} does not exist in the file.")