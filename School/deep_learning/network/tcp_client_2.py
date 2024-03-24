from socket import *

serverName = 'localhost'
serverPort = 12000

def create_message():
    commands = {1: "UP", 2: "LW", 3: "CAP"}

    print("1. UPPER message, 2. LOWER message, 3. CAPITALIZE message, 4. EXIT")
    command = int(input("Enter command: "))

    if command == 4:
        exit()
    data = input("Enter data: ")
    message = commands[command] + ' ' + data

    return message.encode()

def parse_print(message):
    result = message.decode().split(' ', 1)
    if result[0] == "OK":
        print("From Server (Success):", result[1])
    else:
        print("From Server (Fail):", result[1])

def main():

    message = create_message()

    clientSocket = socket(AF_INET, SOCK_STREAM)

    clientSocket.connect((serverName,serverPort))

    clientSocket.send(message)
    modifiedSentence = clientSocket.recv(1024)

    parse_print(modifiedSentence)

    clientSocket.close()

if __name__ == '__main__':
    main()
