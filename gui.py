import functions
import PySimpleGUI as gui
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "a") as file:
        pass

gui.theme("Black")

clock = gui.Text('', key='clock')
label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button("Add", size=10 )
list_box = gui.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=[45, 10])
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")

message_label = gui.Text(key="message")

window = gui.Window('My To-Do App',
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [message_label],
                            [exit_button]],
                    font=('Helvetica', 10))

while True:
    event, value = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%p %d, %Y %H:%M:%S"))
    match event:
        case "todos":
            window["todo"].update(value=value["todos"][0])
        case "Add":
            todos = functions.get_todos()

            new_todo = value['todo'] + "\n"
            todos.append(new_todo)

            functions.write_todos(todos)

            new_todo = new_todo.strip("\n")

            window["todos"].update(values=todos)
            window["message"].update(value=f"Successfully added '{new_todo}'.")

        case "Edit":
            try:
                todo_to_edit = value["todos"][0]
                new_todo = value["todo"] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo

                functions.write_todos(todos)

                new_todo = new_todo.strip("\n")

                window["todos"].update(values=todos)
                window["message"].update(value=f"Successfully edited '{new_todo}'.")
            except IndexError:
                gui.popup("Please select an item first.", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = value["todos"][0]

                todos = functions.get_todos()
                todos.remove(todo_to_complete)

                functions.write_todos(todos)

                todo_to_complete = todo_to_complete.strip("\n")

                window['todos'].update(values=todos)
                window['todo'].update(value="")
                window["message"].update(value=f"Marked '{todo_to_complete}' as completed.")
            except IndexError:
                gui.popup("Please select a todo to mark as completed!", font=("Helvetica", 20))
        case "Exit":
            break
        case gui.WIN_CLOSED:
            break

window.close()
