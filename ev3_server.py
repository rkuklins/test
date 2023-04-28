# server program
import socket
from command_parser import *

def establish_connection(server_socket):
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        command_decode(data)


def server_program():
    # get the hostnam
    host = ""
    port = 27700  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    print("Server started on: " + str(host))
    server_socket.listen(2)

    while True:
        establish_connection(server_socket) 

    conn.close()  # close the connection


def command_decode(data):
    print ("Command:" + data)
    if data == "TurnLeft!":
        turn_left(data)
    elif data == "TurnRight!":
        turn_right(data)
    elif data == "EngineAhead!":
        move_forward(data)
    elif data == "EngineBack!":
        move_backward(data)
    elif data == "EngineStop!":
        stop(data)
    else:
        unknown_command(data)



            
