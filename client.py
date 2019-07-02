import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
test_string = ["E1.0 -945 1689 -950 230 -25 1", "S0 2 -945 1689 -950 230 -25 1 1e-15", "S10", "E.10",
               "S0 2 -945 1689 -950 230 -25 1 -1e-15", "S0 2 -945 1689 -950 230 -25 1 0",
               "S0 2 -945 1689 -950 230 G 1 1e-15", "G.10 0 0", "4 1 0"]

PORT = 8080

client.connect(('127.0.0.1', PORT))

print("Connection Approved")

for index in test_string:

    print("Sending over to server... " + index)

    client.sendall(str.encode(index))

    from_server = client.recv(4096)

    print(b'Receiving from server... ' + from_server)

client.close()
