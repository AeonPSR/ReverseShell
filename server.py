import socket

HOST = "192.168.56.102"
PORT = 12345

# Connect stuff
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Waiting for connection on {HOST}:{PORT}...")
drone_socket, drone_address = server_socket.accept()
print(f"Connection from {drone_address} established.")

while True:
	command = input("Command to send: ")
	if command.lower() == 'quit':
		break
	drone_socket.send(command.encode("UTF-8"))
	# Wait for acknowledgment from drone before sending the next command
	report = drone_socket.recv(1024).decode("UTF-8")
	print(report)
drone_socket.close()
server_socket.close()