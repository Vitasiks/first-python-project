try:
    with open("notes.txt", "r", encoding="utf-8") as file:
        notes = file.read().splitlines()
except FileNotFoundError:
    notes = []

while True:
    print()
    print("1. Добавить заметку")
    print("2. Показать заметки")
    print("3. Выйти")

    choice = input("Выбери действие: ")

    if choice == "1":
        note = input("Введи заметку: ")
        notes.append(note)

        with open("notes.txt", "a", encoding="utf-8") as file:
            file.write(note + "\n")

    elif choice == "2":
        for number, note in enumerate(notes, start=1):
            print(f"{number}. {note}")

    elif choice == "3":
        break
