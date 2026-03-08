import re

text = "Room 102, Floor 5, Code: 9876, Year 2024"
# 期望输出：['102', '987', '024'] ← 注意：'9876' 中取 '987' 和 '876'？不！题目要“连续3位”，默认不重叠匹配（re.findall 默认非重叠）→ 实际输出是？请思考并验证。
match = re.search(r'\d{3}',text)
if match:
    print(match.group())

new_text = re.findall(r'\d{3}', text)
#print(new_text)

text1 = "Valid IDs: A1, X9, Z0, m5, B12, C3, @D4"
# 期望输出：['A1', 'X9', 'C3'] （注意：Z0 的 0 是数字 ✅；m5 小写❌；B12 两位数❌；@D4 @不是字母❌）
new_text1 = re.findall(r'[A-Z]\d', text1)
#print(new_text1)

text2 = "IDs: user123, ab, Test4, hello55, a1b2c3d, OK99"
# 期望输出：['user123', 'Test4', 'hello55', 'a1b2c3d']  
# ✅ user123（7位？等等！→ 仔细看：长度4~6 → 'user123' 是7位？❌ 所以实际应为？请重新判断！）
# 👉 正确期望：['Test4', 'hello55', 'OK99']？还是另有答案？动手验证！
new_text2 = re.findall(r'[A-Za-z][A-Za-z\d]{3,5}',text2)
#print(new_text2)

text3 = "Examples: a-b, 1-2, @-#, x--y, --, A-B-C"
# 期望输出：['a-b', '1-2', '@-#', 'A-B'] ← 注意：'x--y' 有两个 `-`，只取第一个合法的 'x-'？不！要完整匹配 `X-Y` → 所以 'x--y' 中匹配到的是？  
# 提示：`.` 匹配任意单字符（除换行），`-` 是普通字符需字面匹配。
new_text3 = re.findall(r'[A-Za-z]-[A-Za-z]',text3)
print(new_text3)