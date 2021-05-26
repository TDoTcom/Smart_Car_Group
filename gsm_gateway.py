import serial
import time


class TextMessage:
    def __init__(self, recipient="+2348065777685", message="TextMessage.content not set."):
        self.recipient = recipient
        self.content = message

    def setRecipient(self, number):
        self.recipient = number

    def setContent(self, message):
        self.content = message

    def connectPhone(self):
        self.ser = serial.Serial('COM11', 57600, timeout=5, xonxoff=False, rtscts=False,
                                 bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
        time.sleep(1)

    def sendMessage(self):
        self.ser.write('ATZ\r'.encode())
        time.sleep(1)
        self.ser.write('AT+CMGF=1\r'.encode())
        time.sleep(1)
        self.ser.write(('''AT+CMGS="''' + self.recipient + '''"\r''').encode())
        time.sleep(1)
        self.ser.write((self.content + "\r").encode())
        time.sleep(1)
        self.ser.write(chr(26).encode())
        time.sleep(1)

    def read(self):
        self.ser.write('ATZ\r'.encode())
        time.sleep(1)
        self.ser.write('AT+CMGF=1\r'.encode())  # put in textmode
        time.sleep(1)
        self.ser.write('AT+CMGL="ALL"\r'.encode())  # fetch all sms's
        read = self.ser.readlines()
        for msg in read:
            if "+CMGL\r".encode() in msg:  # +CMGL looks for all SMS messages
                print(msg)

    def disconnectPhone(self):
        self.ser.close()


# sms = TextMessage("+237691740926", "Module has send you a text message.")
# sms.connectPhone()
# sms.sendMessage()
# # sms.read()
# sms.disconnectPhone()
# print("message sent successfully")
