import PySimpleGUI as sg


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


def main():
    layout = [
        [sg.Text("Enter a list of numbers (comma-separated):")],
        [sg.Input(key="-LIST-")],
        [sg.Button("Generate List", key="-GENERATE-")],
        [sg.Text("Enter a number to search:")],
        [sg.Input(key="-TARGET-")],
        [sg.Button("Search", key="-SEARCH-")],
    ]

    window = sg.Window("Binary Search", layout)

    sorted_list = []

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == "-GENERATE-":
            input_list = values["-LIST-"].split(",")
            input_list = [int(num.strip()) for num in input_list if num.strip()]
            sorted_list = sorted(input_list)

        if event == "-SEARCH-":
            target = int(values["-TARGET-"])
            result = binary_search(sorted_list, target)

            if result != -1:
                sg.popup(f"Element {target} found at index {result}.")
            else:
                sg.popup(f"Element {target} not found.")

    window.close()


if __name__ == "__main__":
    main()
