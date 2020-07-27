import os
print("Hello! Thank's for using this simple program for work with text.")
file_input = input("Please, write a directory of file that you want to open: ")
file = open(file_input, 'r')
content = file.read()
file.close()
command = ''
pause = ''


def first_command():
    extension = ''
    tmp_s = file_input[len(file_input) - 1: 0: -1] + file_input[0]
    for i in range(len(tmp_s)):
        if tmp_s[i] == '.':
            break
        else:
            extension += tmp_s[i]
    extension = extension[len(extension) - 1: 0: -1] + extension[0]
    statinfo = os.stat(file_input)
    file_weight = statinfo.st_size
    print('File extension:', extension)
    print('File weight:', file_weight, 'bytes')


def second_command():
    file_new = open(file_input, 'r')
    content_new = file_new.read()
    file.close()
    print(content_new)
    print()


def third_command():
    new_file = open(file_input, 'w')
    new_content = content.strip()
    while "  " in new_content:
        new_content = new_content.replace("  ", " ")
    new_file.write(new_content)
    new_file.close()
    print('Well done!')


while command != '4':
    print("""
    1. Info about file
    2. File view
    3. Correct spaces
    4. Exit
    """)
    command = input("Please, choose option and write her number: ")
    print()
    if command == '1':
        first_command()
        pause = input("Press enter to continue...")
    if command == '2':
        second_command()
        pause = input("Press enter to continue...")
    if command == '3':
        third_command()
        pause = input("Press enter to continue...")
print('Goodbye!')
