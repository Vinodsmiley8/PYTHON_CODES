# Implement a basic operating system shell
import os

while True:
    command = input("Enter command: ")
    if command.lower() == 'exit':
        break
    else:
        os.system(command)