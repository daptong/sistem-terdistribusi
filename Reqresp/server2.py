import socket

def program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 2222))

    server_socket.listen(1)
    conn, address = server_socket.accept()

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("received from client:", data)
        try:
            number = int(data)
            squared = number ** 2
            response = str(squared)
            print(f'calculating square of {number} : {response}')
        except ValueError:
            response = "send a valid integer"
        
        conn.send(response.encode())
    
    conn.close()

if __name__ == '__main__':
    program()