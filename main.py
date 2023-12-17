import os
import platform
import sys
import time

installed_apps = []

def list_directory(path="."):
    try:
        contents = os.listdir(path)
        print(f"Contents of '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print("Directory not found.")

def install_app(app_name):
    if app_name.lower() in installed_apps:
        print(f"'{app_name}' is already installed.")
    else:
        installed_apps.append(app_name.lower())
        print(f"'{app_name}' installed successfully.")

def show_installed_apps():
    if not installed_apps:
        print("No apps installed.")
    else:
        print("Installed apps:")
        for app in installed_apps:
            print(app.capitalize())

def install_command(command):
    if len(command) > 2 and command[1] == '-i':
        install_app(command[2])
    else:
        print("Invalid install command. Use 'NookOSAPT -i <app_name>'.")

def clock():
    print("Clock mode activated. Press 'Ctrl+C' to return to the main menu.")
    while True:
        try:
            current_time = time.strftime("%H:%M:%S", time.localtime())
            print(f"Current time: {current_time}", end="\r")
            time.sleep(1)
        except KeyboardInterrupt:
            print("\nExiting clock mode.")
            break

def calculator():
    print("Calculator mode activated.")
    try:
        expression = input("Enter an expression: ")
        result = eval(expression)
        print(f"Result: {result}")
    except Exception as e:
        print("Invalid expression or operation:", e)

def system_info():
    system = platform.system()
    machine = platform.machine()
    processor = platform.processor()
    python_version = platform.python_version()
    print(f"System: {system}")
    print(f"Machine: {machine}")
    print(f"Processor: {processor}")
    print(f"Python Version: {python_version}")
    print(f"OS Version: 1.3")

def text_editor(file_name):
    try:
        with open(file_name, 'r') as file:
            print(f"Editing file: {file_name}")
            lines = file.readlines()
            for line in lines:
                print(line, end='')
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    text = input("\nEnter text (type 'exit' to save and exit): ")
    if text.lower() != 'exit':
        with open(file_name, 'w') as file:
            file.write(text)
        print(f"Changes saved to '{file_name}'.")

def edit_command(command):
    if 'texteditor' in installed_apps:
        if len(command) > 1:
            text_editor(command[1])
        else:
            print("Please provide a file name to edit.")
    else:
        print("Text Editor app is not installed. Please install it using 'NookOSAPT -i texteditor'.")

def make_directory(directory_name):
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except Exception as e:
        print(f"Error creating directory: {e}")

def remove_directory(directory_name):
    try:
        os.rmdir(directory_name)
        print(f"Directory '{directory_name}' removed.")
    except FileNotFoundError:
        print(f"Directory '{directory_name}' not found.")
    except OSError as e:
        print(f"Error removing directory: {e}")

def make_file(file_name):
    try:
        with open(file_name, 'w') as file:
            print(f"File '{file_name}' created.")
    except FileExistsError:
        print(f"File '{file_name}' already exists.")
    except Exception as e:
        print(f"Error creating file: {e}")

def remove_file(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' removed.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error removing file: {e}")

def process_file_commands(command):
    if command[0] == 'mkdir':
        if len(command) > 1:
            make_directory(command[1])
        else:
            print("Please provide a directory name.")
    elif command[0] == 'rmdir':
        if len(command) > 1:
            remove_directory(command[1])
        else:
            print("Please provide a directory name.")
    elif command[0] == 'mk':
        if len(command) > 1:
            make_file(command[1])
        else:
            print("Please provide a file name.")
    elif command[0] == 'rm':
        if len(command) > 1:
            remove_file(command[1])
        else:
            print("Please provide a file name.")

def main():
    print("Welcome to NookOS")
    print("Type 'help' to see available commands.")

    while True:
        command = input("\nEnter a command: ").split()

        if len(command) == 0:
            continue

        if command[0] == 'cd':
            pass  # Add your 'cd' functionality here
        elif command[0] == 'mkdir' or command[0] == 'rmdir' or command[0] == 'mk' or command[0] == 'rm':
            process_file_commands(command)
        elif command[0] == 'ls':
            if len(command) > 1:
                list_directory(command[1])
            else:
                list_directory()
        elif command[0] == 'sysinfo':
            system_info()
        elif command[0] == 'calc':
            calculator()
        elif command[0] == 'NookOSAPT':
            install_command(command)
        elif command[0] == 'clock':
            clock()
        elif command[0] == 'edit':
            edit_command(command)
        elif command[0] == 'help':
            print("List of available commands:")
            print("cd <directory_path> - Change directory")
            print("mkdir <directory_name> - Make a directory")
            print("rmdir <directory_name> - Remove a directory")
            print("mk <file_name> - Make a file")
            print("rm <file_name> - Remove a file")
            print("ls <directory_path> - List contents of a directory")
            print("sysinfo - Display system information")
            print("calc - Calculator")
            print("NookOSAPT -i <app_name> - Install an app")
            print("clock - Clock app")
            print("edit <file_name> - Text Editor")
            print("help - Show available commands")
            print("exit - Exit the program")
        elif command[0] == 'exit':
            print("Exiting NookOS...")
            break
        else:
            print("Command not recognized. Type 'help' for available commands.")

if __name__ == "__main__":
    main()
