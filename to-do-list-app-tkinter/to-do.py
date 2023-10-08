import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root # assign the root window to an instance variable
        self.root.title("To-Do List App") # set the title of the root window

        self.tasks = [] # create an empty list to store the tasks

        # Create widgets
        self.title = tk.Label(root, text="To-Do List App", font=("Helvetica", 15, "bold")) # create a label widget for the title
        self.task_entry = tk.Entry(root, width=50) # create an entry widget for the task entries
        self.task_listbox = tk.Listbox(root, width = 72, selectmode=tk.SINGLE) # create a listbox widget to display the tasks
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task) # create a button widget to add tasks
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task) # create a button widget to remove tasks

        # Place widgets on the grid
        self.title.grid(row=0, column=0, columnspan=2, padx=10, pady=10) 
        self.task_entry.grid(row=1, column=0, padx=(20, 10), pady=10, ipadx=10) 
        self.add_button.grid(row=1, column=1, padx=30, pady=10)
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.remove_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def add_task(self): 
        task = self.task_entry.get() # get the task from the entry box
        if task: # if the task is not empty
            self.tasks.append(task) # add the task to the list
            self.task_listbox.insert(tk.END, task) # add the task to the listbox
            self.task_entry.delete(0, tk.END) # clear the entry box
        else:
            messagebox.showwarning("Input Error", "Please enter a task.") # show warning message if task is empty

    def remove_task(self):
        selected_index = self.task_listbox.curselection() # get the selected index
        if selected_index: # if the index is not empty
            index = selected_index[0] # get the first element of the tuple
            removed_task = self.tasks.pop(index) # remove the task from the list
            self.task_listbox.delete(index) # remove the task from the listbox
            messagebox.showinfo("Task Removed", f'Task "{removed_task}" removed successfully.') # show info message
        else:
            messagebox.showwarning("Selection Error", "Please select a task to remove.") # show warning message if no task is selected

def main():
    root = tk.Tk() # create the root window
    app = ToDoListApp(root) # create the app
    root.mainloop() # run the main loop

if __name__ == "__main__": 
    main() 
