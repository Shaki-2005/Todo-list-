from tkinter import simpledialog, messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Add Task", command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Edit Task", command=self.edit_task).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Mark Completed", command=self.complete_task).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Delete Task", command=self.delete_task).grid(row=0, column=3, padx=5)
        tk.Button(button_frame, text="Clear Completed", command=self.clear_completed).grid(row=0, column=4, padx=5)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter task:")
        if task:
            self.tasks.append({'task': task, 'completed': False})
            self.refresh_list()

    def edit_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            current_task = self.tasks[index]['task']
            new_task = simpledialog.askstring("Edit Task", "Edit task:", initialvalue=current_task)
            if new_task:
                self.tasks[index]['task'] = new_task
                self.refresh_list()

    def complete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]['completed'] = not self.tasks[index]['completed']
            self.refresh_list()

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            del self.tasks[selected[0]]
            self.refresh_list()

    def clear_completed(self):
        self.tasks = [t for t in self.tasks if not t['completed']]
        self.refresh_list()

    def refresh_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "[✔]" if task['completed'] else "[ ]"
            self.task_listbox.insert(tk.END, f"{status} {task['task']}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

input("Press Enter to exit...")


