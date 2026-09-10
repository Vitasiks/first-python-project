expenses = []

print("Вводи расходы по одному.")
print("Когда закончишь, просто нажми Enter.")

while True:
    expense = input("Введи расход: ")

    if expense == "":
        break

    try:
        expense = float(expense)
        expenses.append(expense)
    except ValueError:
        print("Нужно ввести число.")

if expenses:
    total = sum(expenses)
    largest = max(expenses)
    average = total / len(expenses)

    print(f"Общая сумма расходов: {total}")
    print(f"Самый большой расход: {largest}")
    print(f"Средний расход: {average}")
else:
    print("Ты не ввёл ни одного расхода.")
