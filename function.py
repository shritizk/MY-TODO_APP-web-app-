FILEPATH="todo.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath,"r") as file_local:
        existing_todos=file_local.readlines()

    return existing_todos


def write_todos(existing_todos_arg,file_path=FILEPATH):
    with open(file_path,"w") as file:
            file.writelines(existing_todos_arg)
