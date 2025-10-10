import sqlite3
import logging
import csv
from inputhelper import InputHelper

LONGFORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'
MESSAGEONLY = '%(message)s'
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f_handler = logging.FileHandler(filename='Todo.log', mode='a')
f_handler.setFormatter(logging.Formatter(LONGFORMAT))
logger.addHandler(f_handler)
s_handler = logging.StreamHandler()
s_handler.setFormatter(logging.Formatter(MESSAGEONLY))
logger.addHandler(s_handler)


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

    @staticmethod
    def printrow(row):
        return f"Id: {row[0]}  Task: {row[1]}  Priority: {row[2]}"

    def add_task(self):
        name = InputHelper.return_strresponse('Task')
        look = self.find_task(taskname=name)
        if look is not None:
            logger.warning("Cannot enter duplicate task")
            return None
        priority = InputHelper.return_intresponse('Priority')
        if name is None or priority is None:
            logger.warning("No valid new task!")
            return None
        cmd = self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()
        return cmd.lastrowid

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
        id = InputHelper.return_intresponse('Id')
        row = self.find_task(id=id)
        if row is None:
            logger.warning("Task not found")
            return None
        print(self.printrow(row))
        priority = InputHelper.return_intresponse('Priority')
        if priority is None:
            logger.warning("Missing priority!")
            return None
        cmd = self.c.execute('UPDATE tasks SET priority = ? WHERE id =  ?',(priority, id))
        self.conn.commit()
        return cmd.rowcount

    def delete_task(self):
        id = InputHelper.return_intresponse('Id')
        row = self.find_task(id=id)
        if row is None:
            logger.warning("Task not found")
            return None
        print(self.printrow(row))
        cmd = self.c.execute('DELETE FROM tasks WHERE id = ?', id)
        self.conn.commit()
        return cmd.rowcount

    def renumber_tasks(self):
        [(maxid,)] = self.c.execute('SELECT MAX(id) FROM tasks')
        tempid = maxid
        updates = 0
        for row in self.task_list():
            tempid += 1
            self.c.execute('UPDATE tasks SET id = ? WHERE id = ?',(tempid,row[0]))
        for row in self.task_list():
            cmd = self.c.execute('UPDATE tasks SET id = ? WHERE id = ?',(row[0]-maxid,row[0]))
            updates += cmd.rowcount
        return updates

    def export_csv(self):
        tasklist = self.task_list()
        with open('todo.csv','w',newline='') as csvfile:
            headers = ['id', 'name', 'priority']
            writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(headers)
            for row in tasklist:
                writer.writerow(row)
        return len(tasklist)

    def close(self):
        self.conn.commit()
        self.conn.close()

if __name__ == "__main__":
    app = Todo()
    while True:
        print('''Application Menu:
        1. Show Tasks
        2. Add Task
        3. Update priority
        4. Delete task
        5. Renumber tasks by priority
        6. Export
        7. Exit''')
        choice = InputHelper.return_intresponse('Choice')
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
            app.export_csv()
        elif choice == '7':
            break

    app.close()
