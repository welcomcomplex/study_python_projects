import pandas as pd
import random

names = ['关羽', '张飞', '赵云', '马超', '黄忠']


data = {
    '姓名': names,
    '语文': [random.randrange(50, 101) for _ in names],
    '数学': [random.randrange(50, 101) for _ in names],
    '英语': [random.randrange(50, 101) for _ in names]
}

#df = pd.DataFrame(data)

#df.to_csv(r'E:\my_python_project\IO_wenjian\123.csv', index=False, encoding='utf-8-sig')


#print(df)

data_result = pd.read_csv(r'E:\my_python_project\IO_wenjian\123.csv')
print(data_result)