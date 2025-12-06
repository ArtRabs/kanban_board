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

def main():

    print("Welcome to the Kanban Board!")

    task1 = Task(1, "Implement feature X", "Details about feature X")
    task2 = Task(2, "Fix bug Y", "Details about bug Y")
    task3 = Task(3, "Write documentation", "Details about documentation")

    todo_column = Column("To Do")
    in_progress_column = Column("In Progress")
    done_column = Column("Done")

    board = Board()

    board.add_column(todo_column)
    board.add_column(in_progress_column)
    board.add_column(done_column)

    board.add_task("To Do", task1)
    board.add_task("To Do", task2)
    board.add_task("In Progress", task3)

    board.show_board()

    board.move_task(1, "To Do", "In Progress")

    print("\n--- After Moving Task 1 ---")
    board.show_board()

if __name__ == "__main__":

    main()