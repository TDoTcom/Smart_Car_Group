import socket
import threading
from .gsm_gateway import TextMessage


host, port = ('', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print('-> Server Online.')


class ThreadingForClient(threading.Thread):
    def __init(self, conn):
        threading.Thread.__init__(self)
        self.client = conn

        def run(self):
            data = self.conn.revc(1024)
            data = data.encode("utf-8")
            print(data)  # data received from client

            sms = TextMessage(
                "+237695622901", "Module has send you a text message.")
            sms.connectPhone()
            text_messages = sms.read()
            text_messages = text_messages.encode('utf-8')
            socket.sendall(text_messages)
            print('Lecture en cours ..... ')


while True:
    socket.listen(5)
    conn, address = socket.accept()
    print('Waiting for new messages.....')

    msg_thread = ThreadingForClient(conn)
    msg_thread.start()

    # data = conn.recv(1024)
    # data = data.decode('utf-8')
    # print(data)

conn.close()
socket.close()
