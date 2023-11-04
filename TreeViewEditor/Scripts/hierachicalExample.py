import tkinter as tk
from tkinter import ttk

def add_folder(tree, parent, folder_name):
    item_id = tree.insert(parent, "end", text=folder_name)
    return item_id

def main():
    root = tk.Tk()
    root.title("Hierarchical UI Example")

    tree = ttk.Treeview(root)
    tree.pack()

    root_folder = add_folder(tree, "", "Root Folder")

    subfolder1 = add_folder(tree, root_folder, "Subfolder 1")
    add_folder(tree, subfolder1, "Sub-subfolder 1")

    subfolder2 = add_folder(tree, root_folder, "Subfolder 2")
    add_folder(tree, subfolder2, "Sub-subfolder 2")

    root.mainloop()

if __name__ == "__main__":
    main()
