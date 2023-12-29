import socket

# Configurações do servidor GPS
GPS_IP = '192.168.1.2'  # Substitua pelo endereço IP do dispositivo GPS
GPS_PORT = 12345        # Substitua pela porta usada pelo dispositivo GPS

def main():
    # Criando um socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Conectando ao servidor GPS
        s.connect((GPS_IP, GPS_PORT))
        print(f"Conectado a {GPS_IP}:{GPS_PORT}")

        try:
            while True:
                # Recebendo dados (ajuste o tamanho do buffer conforme necessário)
                data = s.recv(1024)
                if data:
                    print(f"Dados Recebidos: {data.decode('utf-8')}")
                else:
                    # Nenhum dado recebido, encerra a conexão
                    break
        except Exception as e:
            print(f"Erro ao receber dados: {e}")
        finally:
            print("Conexão encerrada.")

if __name__ == "__main__":
    main()
