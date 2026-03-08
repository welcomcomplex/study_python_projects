import pandas as pd
import numpy as np

data = {
    '姓名': ['张三', '李四', '王五', '赵六', '孙七', '周八', '吴九', '郑十'],
    '班级': ['一班', '一班', '二班', '二班', '一班', '二班', '一班', '二班'],
    '语文': [85, 92, 78, 88, 95, np.nan, 82, 90],  # 注意周八的语文是缺失值
    '数学': [90, 85, 92, 76, 88, 95, 89, 94],
    '英语': [88, 90, 85, 92, 91, 87, np.nan, 89]   # 注意吴九的英语是缺失值
}

df = pd.DataFrame(data)
df = df.fillna(0)
print(df)

df = df[['姓名', '语文', '数学']]
df = df[df['数学'] > 90]
df = df.sort_values(by='语文', ascending=False)
print(df)