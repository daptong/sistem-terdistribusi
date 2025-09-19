import socket

def program():
    client_socket = socket.socket()  
    client_socket.connect(('reqresp-server', 2222))  
    
    message = input("enter number: ")  
    
    try:
        while True:
            client_socket.send(message.encode())  
            data = client_socket.recv(1024).decode('utf-8')  
        
            print(f'{message} squared is : {data}')  
            
            message = input("enter another number: ")  
    except KeyboardInterrupt:
        client_socket.close()

if __name__ == '__main__':
    program()