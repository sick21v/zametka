from delete_note import delete_note
from edit_note import edit_note
from find_note import find_note
from open_note import open_note
from add_note import add_note
from show_all import show_all

def main():
    n = 0
    while True:
        print("Выберите:\n"
              "1. Добавить заметку\n"
              "2. Показать все\n"
              "3. Выполнить заметку\n"
              "4. Удалить заметку\n"
              "5. Редактировать\n"
              "6. Найти заметки\n"
              "7. Выйти")
        n = input()
        if n == "1":
            add_note()
        if n == "2":
            show_all()
        if n == "3":
            open_note()
        if n == "4":
            delete_note()
        if n == "5":
            edit_note()
        if n == "6":
            find_note
        if n == '7':
            break

if __name__ == '__main__':
    main()