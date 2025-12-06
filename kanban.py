import json

class Task:

    def __init__(self, id, title, description=""):

        self.id = id
        self.title = title
        self.description = description

    def __repr__(self):

        return f"Task({self.id}, {self.title})"
    
class Column:

    def __init__(self, name):

        self.name = name
        self.tasks = []

    def add_task(self, task):

        self.tasks.append(task)

    def remove_task(self, task_id):

        # new_tasks = []                     
        # for task in self.tasks:            
        #     if task.id != task_id:         
        #         new_tasks.append(task)     

        # self.tasks = new_tasks             

        # or

        self.tasks = [task for task in self.tasks if task.id != task_id]

    def __repr__(self):

        return f"Column({self.name}, tasks={len(self.tasks)})"

class Board:

    def __init__(self):

        self.columns = {}

    def add_column(self, column):

        self.columns[column.name] = column

    def add_task(self, column_name, task):

        if column_name in self.columns:

            self.columns[column_name].add_task(task)

    def show_board(self):

        for column_name, column in self.columns.items():

            print(f"[{column_name}]")

            for task in column.tasks:

                print(f" - ({task.id}) {task.title}: {task.description}")

            print()


    def move_task(self, task_id, from_column, to_column):

        if from_column in self.columns and to_column in self.columns:

            for task in self.columns[from_column].tasks:

                if task.id == task_id:

                    self.columns[to_column].add_task(task)
                    self.columns[from_column].remove_task(task_id)

                    return
                
    def save_board(self, filename="board.json"):

        data = {}

        for column_name, column in self.columns.items():

            data[column_name] = [

                {
                    "id": task.id,
                    "title": task.title,
                    "description": task.description
                }

                for task in column.tasks

            ]

        with open(filename, "w") as f:

            json.dump(data, f, indent=4)

        print(f"Board saved to {filename}")
                
def menu(board):

    while True:

        command = input("Enter command (add/move/show/save/quit): ")

        if command == "show":

            board.show_board()

        elif command == "move":

            task_id = int(input("Task ID: "))
            from_col = input("From column: ")
            to_col = input("To column: ")

            board.move_task(task_id, from_col, to_col)

        elif command == "add":

            task_id = int(input("Task ID: "))
            title = input("Task title: ")
            description = input("Task description: ")
            column = input("Column to add task: ")

            board.add_task(column, Task(task_id, title, description))

        elif command == "save":

            board.save_board()
        
        elif command == "quit":

            print("Exiting Kanban Board...")

            break

        else:
            
            print("Unknown command, try again.")

def main():

    print("Welcome to the Kanban Board!")

    todo_column = Column("To Do")
    in_progress_column = Column("In Progress")
    done_column = Column("Done")

    board = Board()
    board.add_column(todo_column)
    board.add_column(in_progress_column)
    board.add_column(done_column)

    board.add_task("To Do", Task(1, "Implement feature X", "Details about feature X"))
    board.add_task("To Do", Task(2, "Fix bug Y", "Details about bug Y"))
    board.add_task("In Progress", Task(3, "Write documentation", "Details about documentation"))

    menu(board)

if __name__ == "__main__":

    main()