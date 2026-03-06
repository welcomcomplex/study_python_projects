from collections import deque
window = deque(maxlen=3)  # ← 已帮你创建好
# 请向 window 添加元素 [1, 2, 3, 4, 5]
for i in range(1, 6):
    window.popleft() if len(window) == window.maxlen else None
    window.appendleft(i)
    
# 最终 window 应为 deque([3, 4, 5])

from collections import Counter
logs = ["ERROR", "INFO", "WARNING", "ERROR", "INFO", "ERROR"]
word_count = Counter((logs))
str1 :str = word_count.most_common(1) 

# ❌ 错误：set 不能作 dict key
role_permissions = {
    frozenset({"read", "write"}): "editor",
    frozenset({"read"}): "viewer"
}
