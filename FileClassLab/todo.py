import sqlite3


class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()

    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')

    def return_intresponse(self,field):
        result = '0'
        while True:
            result = input(f'Enter {field}: ')
            if self.dtype(result) != 'i':
                print(f"Invalid {field}!")
            break
        return result

    def return_strresponse(self,field):
        result = None
        while True:
            result = input(f'Enter {field}: ')
            if self.dtype(result) != 's':
                print(f"Invalid {field}!")
            break
        return result

    def printrow(self,row):
        return f"Id: {row[0]}  Task: {row[1]}  Priority: {row[2]}"

    def dtype(self,x):
        if x is not None and x != '':
            if x.isdigit():
                return 'i'
            if x.replace(' ','').isalnum():
                return 's'
        return 'u'

    def add_task(self):
        name = self.return_strresponse('Task')
        look = self.find_task(taskname=name)
        if look is not None:
            print("Cannot enter duplicate task")
            return None
        priority = self.return_intresponse('Priority')
        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()

    def find_task(self, taskname=None,id=None):
        for row in self.task_list():
            if taskname is not None:
                if taskname == row[1]:
                    return row
            if id is not None:
                if int(id) == row[0]:
                    return row
        return None

    def task_list(self):
        tl = self.c.execute('SELECT * FROM tasks order by priority')
        return tl.fetchall()

    def list_tasks(self):
        for row in self.task_list():
            print(self.printrow(row))

    def update_priority(self):
        id = self.return_intresponse('Id')
        row = self.find_task(id=id)
        if row is None:
            print("Task not found")
            return
        print(self.printrow(row))
        priority = self.return_intresponse('Priority')
        self.c.execute('UPDATE tasks SET priority = ? WHERE id =  ?',(priority, id))
        self.conn.commit()

    def delete_task(self):
        id = self.return_intresponse('Id')
        row = self.find_task(id=id)
        if row is None:
            print("Task not found")
            return
        print(self.printrow(row))
        self.c.execute('DELETE FROM tasks WHERE id = ?', (id))
        self.conn.commit()

    def renumber_tasks(self):
        [(maxid,)] = self.c.execute('SELECT MAX(id) FROM tasks')
        tempid = maxid
        for row in self.task_list():
            tempid += 1
            self.c.execute('UPDATE tasks SET id = ? WHERE id = ?',(tempid,row[0]))
        for row in self.task_list():
           self.c.execute('UPDATE tasks SET id = ? WHERE id = ?',(row[0]-maxid,row[0]))
        return

    def close(self):
        self.conn.commit()
        self.conn.close()


app = Todo()
while True:
    print('''Application Menu:
    1. Show Tasks
    2. Add Task
    3. Update priority
    4. Delete task
    5. Renumber tasks by priority
    6. Exit''')
    choice =  app.return_intresponse('Choice')
    if choice == '1':
        app.list_tasks()
    elif choice == '2':
        app.add_task()
    elif choice == '3':
        app.update_priority()
    elif choice == '4':
        app.delete_task()
    elif choice == '5':
        app.renumber_tasks()
    elif choice == '6':
        break

app.close()
