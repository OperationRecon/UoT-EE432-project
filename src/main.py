# Function to be used in the CLI. most likely to be moved to a seperate file/folder. 
def hello_message():
    print('Hello World')


def login():
    u = input('username: ')
    p = input('password: ')

    if u == 'admin' and p == '12345678':
        print('welcome, Admin!')
    else:
        print('Invalid Credintials')


def commands_help(command = ''):
    command_list = ['hello','login','help']
    if command not in commands:
        for i in command_list:
            print(i)

# Dict containing the CLI commands related to each function. 
# Typing the key string in the terminal executes the value command
commands = {'hello': hello_message, 'login':login, 'help':commands_help}

# main file, to include initialisations and the CLI responses.
def main():
    print('Welcome to admin system. Enter help to open command list.')
    while True:
        command = input()
        if command in commands:
            commands[command]()
        elif(command == 'exit'):
            break   
        else:
            print('Uknown command. spell-check or Enter help to open command list.')


if __name__ == '__main__':
    main()