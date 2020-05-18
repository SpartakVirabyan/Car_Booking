import tkinter as tk

root = tk.Tk()
root.title("List App")
root.geometry("400x400")


def clicked():
    listbox.insert(tk.END, content.get())


def delete():
    listbox.delete(0, tk.END)


def delete_selected():
    listbox.delete(tk.ANCHOR)


# LISTBOX
content = tk.StringVar()
entry = tk.Entry(root, textvariable=content)
entry.pack()
button = tk.Button(root, text="Add Item", command=clicked)
button.pack()
button_delete = tk.Button(text="Delete", command=delete)
button_delete.pack()
button_delete_selected = tk.Button(text="Delete Selected", command=delete_selected)
button_delete_selected.pack()
listbox = tk.Listbox(root)
listbox.pack()
root.mainloop()