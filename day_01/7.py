data = ["apple", "banana", "cherry"]
for i,itum in enumerate(data):
    print(f"Index: {i}, Item: {itum}")

count = 0
while count < 5:
    print(count)
    # ← 缺少这一行！
    count += 1

numbers = [2, 4, 6, 8]
target = 5
for j,itum in enumerate(numbers):
    if itum == target:
        print(f"Found {target} at index {j}")
        break
    elif j == len(numbers) - 1:
        print(f"{target} not found in the list.")

        

