import bluetooth

# Endereço MAC do dispositivo Bluetooth (substitua pelo do seu dispositivo)
target_address = "00:00:00:00:00:00"

def receive_data():
    # Criando um socket Bluetooth
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    try:
        # Conectando ao dispositivo
        sock.connect((target_address, 1))
        print(f"Conectado ao dispositivo com endereço {target_address}")

        while True:
            data = sock.recv(1024)  # Recebendo dados (ajuste o tamanho do buffer conforme necessário)
            if data:
                print(f"Dados Recebidos: {data.decode('utf-8')}")

    except bluetooth.btcommon.BluetoothError as e:
        print(f"Erro na conexão Bluetooth: {e}")

    finally:
        sock.close()

if __name__ == "__main__":
    receive_data()
