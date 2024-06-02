import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        # Listbox to display tasks
        self.tasks_listbox = tk.Listbox(root, height=15, width=50)
        self.tasks_listbox.pack(pady=20)

        # Entry box to add new tasks
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Button to add a new task
        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Button to update selected task
        self.update_task_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_task_button.pack(pady=5)

        # Button to delete selected task
        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # Load tasks from file
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            new_task = self.task_entry.get()
            if new_task:
                self.tasks_listbox.delete(selected_task_index)
                self.tasks_listbox.insert(selected_task_index, new_task)
                self.task_entry.delete(0, tk.END)
                self.save_tasks()
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(selected_task_index)
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def save_tasks(self):
        tasks = self.tasks_listbox.get(0, tk.END)
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
                for task in tasks:
                    self.tasks_listbox.insert(tk.END, task.strip())
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
