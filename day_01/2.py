username :str = "Alice"
score : int = 95
if score >= 90:
    grade : str = "A"
elif score >= 80:
    grade : str = "B"
else:
    grade : str = "C"
print("{username} scored {score} and received grade {grade}.")