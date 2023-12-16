import os
import platform
import sys

# Define functions for the commands
# (Existing functions remain unchanged)

def list_directory(path="."):
    try:
        contents = os.listdir(path)
        print(f"Contents of '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print("Directory not found.")

def system_info():
    system = platform.system()
    machine = platform.machine()
    processor = platform.processor()
    python_version = platform.python_version()
    os_version = "0.8 Beta"  # New: OS Version
    print(f"System: {system}")
    print(f"Machine: {machine}")
    print(f"Processor: {processor}")
    print(f"Python Version: {python_version}")
    print(f"OS Version: {os_version}")  # New: Display OS Version

def show_help():
    print("List of available commands:")
    print("1. cd <directory_path> - Change directory")
    print("2. mkdir <directory_name> - Make a directory")
    print("3. rmdir <directory_name> - Remove a directory")
    print("4. mk <file_name> - Make a file")
    print("5. rm <file_name> - Remove a file")
    print("6. ls <directory_path> - List contents of a directory")
    print("7. sysinfo - Display system information")
    print("8. help - Show available commands")
    print("9. exit - Exit the program")

def exit_program():
    print("Exiting...")
    print("Thank you for using NookOS!")
    sys.exit(0)

# Main program loop
def main():
    print("Welcome to NookOS")
    show_help()

    while True:
        command = input("\nEnter a command: ").split()

        if len(command) == 0:
            continue

        if command[0] == 'cd':
            # Existing command function calls remain unchanged
            pass
        elif command[0] == 'mkdir':
            # Existing command function calls remain unchanged
            pass
        elif command[0] == 'rmdir':
            # Existing command function calls remain unchanged
            pass
        elif command[0] == 'mk':
            # Existing command function calls remain unchanged
            pass
        elif command[0] == 'rm':
            # Existing command function calls remain unchanged
            pass
        elif command[0] == 'ls':
            if len(command) > 1:
                list_directory(command[1])
            else:
                list_directory()
        elif command[0] == 'sysinfo':
            system_info()
        elif command[0] == 'help':
            # Existing command function calls remain unchanged
            pass
        elif command[0] == 'exit':
            exit_program()
        else:
            print("Command not recognized. Type 'help' for available commands.")

if __name__ == "__main__":
    main()
