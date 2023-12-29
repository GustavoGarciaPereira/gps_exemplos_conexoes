import serial
import time

# Configurações da porta serial
PORT = 'COM3'  # Altere para a porta onde seu GPS está conectado
BAUDRATE = 9600  # Altere para a taxa de transmissão do seu dispositivo

def main():
    try:
        # Inicializa a conexão serial
        with serial.Serial(PORT, BAUDRATE, timeout=1) as ser:
            print(f"Conectado a {ser.name}")

            while True:
                # Lê uma linha de dados
                data = ser.readline().decode('utf-8').rstrip()
                
                # Imprime os dados, se houver
                if data:
                    print(f"Dados Recebidos: {data}")

                # Intervalo para evitar consumo excessivo de CPU
                time.sleep(1)

    except serial.SerialException as e:
        print(f"Erro ao acessar a porta serial: {e}")

if __name__ == "__main__":
    main()
