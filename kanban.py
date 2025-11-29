class Task:

    def __init__(self, id, title, description=""):

        self.id = id
        self.title = title
        self.description = description

    def __repr__(self):

        return f"Task({self.id}, {self.title})"

def main():

    print("Welcome to the Kanban Board!")

    task1 = Task(1, "Implement feature X", "Details about feature X")
    task2 = Task(2, "Fix bug Y", "Details about bug Y")
    
    print(task1)
    print(task2)

if __name__ == "__main__":

    main()