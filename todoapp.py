import tkinter as tk
import os

global tasks
tasks = []

task_listbox = None

base_folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_folder, "tasks.txt")

root = tk.Tk()
root.title('To-Do App')
window_width = 500
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg="lightblue")

def add_task():
    task = task_entry.get().strip()
    if task and task not in tasks:
        tasks.append(task)
        with open(file_path, 'a') as file:
            file.write(task + '\n')
        task_entry.delete(0, tk.END)
        show_tasks()  # Refresh the list
        
def show_tasks():
    global task_listbox, tasks

    # Load from file before displaying
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]

    # Remove previous listbox if exists
    if task_listbox:
        task_listbox.destroy()

    task_listbox = tk.Listbox(root, width=30)
    task_listbox.pack(pady=10)

    if tasks:
        for idx, task in enumerate(tasks, start=1):
            task_listbox.insert(tk.END, f"{idx}) {task}")
    else:
        task_listbox.insert(tk.END, "Empty list")
    
def delete_task():
    global task_listbox
    # with open(file_path, "w") as file:
    #     pass
    task_listbox.destroy()
    # tasks.clear()
    
def delete_data():
    global task_listbox
    with open(file_path, "w") as file:
         pass
    task_listbox.destroy()
    tasks.clear()
    
def delete_selected():
    global task_listbox
    selection = task_listbox.curselection()
    if selection:
        index = selection[0]
        tasks.pop(index)
        with open(file_path, 'w') as file:
            for task in tasks:
                file.write(task + '\n')
        show_tasks()
    else:
        print("No task selected")

label = tk.Label(root, text="Enter new task or task number to delete:", bg="lightblue", font=("Arial", 12))
label.pack(pady=(50, 5))

task_entry = tk.Entry(root, width = 50)
task_entry.pack(pady = (5, 30))

add_button = tk.Button(root, text = 'Add a task', command=add_task, width = 20)
add_button.pack(pady = 5)

delete_task_button = tk.Button(root, text = 'Delete task', command=delete_selected, width = 20)
delete_task_button.pack(pady = 5)

show_button = tk.Button(root, text = 'Show tasks', command=show_tasks, width = 20)
show_button.pack(pady = 5)

delete_button = tk.Button(root, text = 'Clear tasks', command=delete_task, width = 20)
delete_button.pack(pady = 5)

delete_data_button = tk.Button(root, text = 'Clear all data', command=delete_data, width = 20)
delete_data_button.pack(pady = 5)

root.mainloop()