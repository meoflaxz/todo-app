# from functions import get_todos, write_todos
import functions

while True:
    text = input("Do you want to add, show, edit, complete or exit?")
    text = text.strip()

    if text.startswith("add"):
        todo = text[4:]
        todos = functions.get_todos()
        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif text.startswith("edit"):
        try:
            number = int(text[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Invalid command.")
            continue

    elif text.startswith("complete"):
        try:
            opt = int(text[9:])

            todos = functions.get_todos()
            index = opt - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"{todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print(f"No item with number {opt}")
            continue
        except ValueError:
            print("Please specify item number.")
            continue

    elif text.startswith("show"):
        todos = functions.get_todos()

        for i, item in enumerate(todos, start=1):
            item = item.strip("\n")
            item = item.title()
            row = f"{i}-{item}"
            print(row)
    elif 'exit' in text:
        break
    else:
        print("Unknown command!")

print("Bye!")
