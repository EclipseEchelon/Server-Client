import socket
import polynomials

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 8080

server.bind(('127.0.0.1', PORT))

server.listen(5)

while True:
    conn, addr = server.accept()
    from_client = ''

    try:
        while True:
            data = conn.recv(4096)
            if not data: break
            test_string = data.decode()



            print("Server received: " + test_string)
            try:

                # Evaluate expression
                if test_string.split(' ').pop(0)[0] is 'E':

                    try:
                        if len(test_string.split(' ')) is 1:
                            conn.sendall(str.encode("XToo few arguments "))

                        else:
                            x = float(test_string.split(' ').pop(0)[1:])
                            poly = list(map(int, test_string[5:].split(' ')))
                            result = str(polynomials.evaluate(x, poly))

                            print("Sending back to client... E" + result)
                            conn.sendall(str.encode("E" + result))

                    except:
                        conn.sendall(str.encode("Could not convert string to float"))

                #evaluate bisection
                if test_string.split(' ').pop(0)[0] is 'S':

                    try:
                        if len(test_string.split(' ')) is 1:
                            conn.sendall(str.encode("XToo few arguments "))

                        else:
                            a = float(test_string.split(' ').pop(0)[1])
                            b = float(test_string.split(' ')[1])
                            poly = list(map(int, test_string.split(' ')[2:-1]))
                            tole = list(map(float, test_string.split(' ')[-1:]))

                            if tole[0] <= 0.0:
                                conn.sendall(str.encode("XInvalid Tolerance"))

                            else:
                                result = str((polynomials.bisection(a, b, poly, tole[0])))

                                print("Sending back to client... S" + result)
                                conn.sendall(str.encode("S" + result))

                    except:
                        conn.sendall(str.encode("Xcould not convert string to float"))

                if test_string.split(' ').pop(0)[0] != "E" and test_string.split(' ').pop(0)[0] != "S":
                    conn.sendall(str.encode("XIncorrect Command Type"))

            except:
                conn.sendall(str.encode("Xcould not convert string to float"))

    except socket.error:
        print("Error Occurred")
    break

conn.close()

print("Client Disconnected")


