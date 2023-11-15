import subprocess, multiprocessing, time, socket

username = "ist199139"
password = "WTFdeixala17"
pid = 0

def VPN():
	print("Este é o processo filho 1.")
	comando = "sudo openvpn --config /etc/openvpn/tecnico.ovpn --auth-user-pass auth.conf"
	
	processo_openvpn = subprocess.Popen(comando, shell=True)
	pid = processo_openvpn.pid
	
	print("1")
	processo = multiprocessing.Process(target=LigacaoServidor)
	processo.start()
	filho = processo.pid
	print(f"PID do processo filho: {filho}")
	
	
	
	
def LigacaoServidor():

	print("Este é o processo filho 2.")
	time.sleep(5)
	HOST = "10.2.20.6"
	PORT = 12345
	
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect((HOST, PORT))
	message = "Olá, servidor!"
	client_socket.sendall(message.encode('utf-8'))
	print("2")
	
	
	response = client_socket.recv(1024)
	print(f"Resposta do servidor: {response.decode('utf-8')}")
	
	client_socket.close()


    

if __name__ == "__main__":

	processo_filho = multiprocessing.Process(target=VPN)
    
    
	processo_filho.start()
	pid_filho = processo_filho.pid
	print(f"PID do processo filho: {pid_filho}")
	time.sleep(60)
	comando = f"sudo kill {pid_filho}"
	resultado = subprocess.getoutput(comando)
	comando = f"sudo kill {pid}"
	resultado = subprocess.getoutput(comando)
	processo_filho.terminate()
    
    
	processo_filho.join()

	print("Este é o processo pai.")
