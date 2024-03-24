from socket import *

def parse_process(message):
    result_message = None
    try:
        command, sentence = message.decode().split(' ', 1)
        if command == 'UP':
            result_message = "OK" + ' ' + sentence.upper()
        elif command == 'LW':
            result_message = "OK" + ' ' + sentence.lower()
        elif command == 'CAP':
            result_message = "OK" +  ' ' + sentence.capitalize()
        else:
            result_message = "NOK" + ' ' + 'Invalid command'
    except Exception as e:
        result_message = "NOK" + ' ' + 'Invalid message format'
    return result_message.encode()

def main():

    serverPort = 12000
    serverSocket = socket(AF_INET,SOCK_STREAM)

    serverSocket.bind(('localhost',serverPort))
    serverSocket.listen(1)

    print('The server is ready to receive')

    while True:
        connectionSocket, addr = serverSocket.accept()
        message = connectionSocket.recv(1024)
        result = parse_process(message)
        connectionSocket.send(result)
        connectionSocket.close()

if __name__ == '__main__':
    main()
