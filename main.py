import os
import time

path = "A:/code/python/courses/ardit/proj1/todos.txt"
now = time.strftime("%b %d, %Y %H:%M:%S")

if os.path.isfile(path):
    print(f"The file {path} exists.")
    print("It is", now)

    while True:
        user_action = input("Type a-add, e-edit, c-check, s-show or x-exit: ")
        user_action = user_action.strip()

        match user_action:
            case 'add' | 'a':

                todo = input("Enter a TODO: ") + '\n'

                with open('todos.txt', 'r') as file:
                    todos = file.readlines()

                todos.append(todo)

                with open('todos.txt', 'w') as file:
                    file.writelines(todos)

            case 'edit' | 'e':
                edit_todo_n = int(input("Choose a TODO # to edit: ")) - 1

                edit_todo = input("New TODO value: ") + '\n'

                with open("todos.txt", 'r') as file:
                    todos = file.readlines()

                todos[edit_todo_n] = edit_todo

                with open("todos.txt", 'w') as file:
                    file.writelines(todos)

            case 'check' | 'c':
                number = int(input("Choose a TODO # to check: ")) - 1

                with open("todos.txt", 'r') as file:
                    todos = file.readlines()

                todos.pop(number)

                with open("todos.txt", 'w') as file:
                    file.writelines(todos)

            case 'show' | 's':

                with open('todos.txt') as file:
                    todos = file.readlines()

                if not todos:  # if todos == []:
                    print("Empty now...")

                for index, item in enumerate(todos):
                    item = item.strip('\n')
                    item = item.title()
                    print(f"{index + 1}-{item}")

            case 'exit' | 'x':
                break
            case _:
                print("Hey, you entered an unknown command")
    print("Bye!")

else:
    print(f"\n\nUnfortunately, the file 'todos.txt' does not exist in this {path}."
          f" Create the file manually, please\n\n")
    print("It is", now)
