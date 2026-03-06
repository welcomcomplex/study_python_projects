str1 : str = "Hello, World! 1234567890"
print(str1.strip("0"))
str2 : str = str1.split(",").join("-")
print(str2)
