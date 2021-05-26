import socket

host, port = ('localhost', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.connect((host, port))
    print('Connexion Established.')
    # request for new messages
    data = "new values yet ? "
    data = data.encode('utf-8')
    socket.sendall(data)
except:
    print('Connexion to local server Failed ')
finally:
    socket.close()
