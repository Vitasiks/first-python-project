shopping_list = ["молоко", "хлеб", "яйца"]

while True:
    print()
    print("1. Добавить покупку")
    print("2. Удалить покупку")
    print("3. Показать список")
    print("4. Выйти")

    choice = input("Выбери действие: ")

    if choice == "1":
        new_item = input("Что добавить в список? ")

        if new_item.strip():
            shopping_list.append(new_item)
        else:
            print("Покупка не может быть пустой.")

    elif choice == "2":
        print("Твой список покупок:")
        for number, item in enumerate(shopping_list, start=1):
            print(f"{number}. {item}")

        try:
            delete_number = int(input("Какую покупку удалить? Введи её номер: "))
        except ValueError:
            print("Нужно ввести число.")
            delete_number = 0

        if 1 <= delete_number <= len(shopping_list):
            shopping_list.pop(delete_number - 1)
        else:
            print("Такого номера нет в списке.")

    elif choice == "3":
        print("Твой список покупок:")
        for number, item in enumerate(shopping_list, start=1):
            print(f"{number}. {item}")
        

    elif choice == "4":
        break

    else:
        print("Неверный выбор")
