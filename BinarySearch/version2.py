import tkinter as tk
from tkinter import messagebox

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def search():
    target = int(entry.get())
    result = binary_search(sorted_list, target)

    if result != -1:
        messagebox.showinfo("Result", f"Element {target} found at index {result}.")
    else:
        messagebox.showinfo("Result", f"Element {target} not found.")

# GUI
root = tk.Tk()
root.title("Binary Search")
root.geometry("300x200")

label_list = tk.Label(root, text="Enter a list of numbers (comma-separated):")
label_list.pack()

entry_list = tk.Entry(root)
entry_list.pack()

button_generate = tk.Button(root, text="Generate List", command=lambda: generate_sorted_list())
button_generate.pack()

label_search = tk.Label(root, text="Enter a number to search:")
label_search.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Search", command=search)
button.pack()

def generate_sorted_list():
    input_list = entry_list.get().split(",")
    input_list = [int(num.strip()) for num in input_list if num.strip()]
    global sorted_list
    sorted_list = sorted(input_list)

root.mainloop()
