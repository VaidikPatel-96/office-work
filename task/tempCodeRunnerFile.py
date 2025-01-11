students = [("John", 90), ("Jenny", 80), ("Tom", 70)]
scores = []

for student in students:
    name, score = student
    print(f"{name} scored {score}")
    scores.append(score)

average = sum(scores) / len(scores)
print(f"\nThe average score is {average:.2f}")
