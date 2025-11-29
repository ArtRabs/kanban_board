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

        # new_tasks = []                     # start with an empty list
        # for task in self.tasks:            # go through each task in the column
        #     if task.id != task_id:         # check if the task's id is NOT the one to remove
        #         new_tasks.append(task)     # if so, keep it by adding to new list

        # self.tasks = new_tasks             # replace old list with the filtered one

        # or

        self.tasks = [task for task in self.tasks if task.id != task_id]

    def __repr__(self):

        return f"Column({self.name}, tasks={len(self.tasks)})"

def main():

    print("Welcome to the Kanban Board!")

    task1 = Task(1, "Implement feature X", "Details about feature X")
    task2 = Task(2, "Fix bug Y", "Details about bug Y")

    todo_column = Column("To Do")
    todo_column.add_task(task1) # Column(To Do, tasks=1)

    in_progress_column = Column("In Progress")
    in_progress_column.add_task(task2) # Column(In Progress, tasks=1)

    print(todo_column)
    print(in_progress_column)

    todo_column.remove_task(1) # Column(To Do, tasks=0) # remove by id, not amount

    print(todo_column)

if __name__ == "__main__":

    main()