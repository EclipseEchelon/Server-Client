# Server-Client
This is a Server Client I created in python. It takes a list of strings from the client side and sends them to the server. The strings are formatted as polynomials and the server side evaluates these. The result is then sent back to the client side. This is a good project for understanding the connection between client and server and the manipulation of data between them. 

he server will listen on a specific port number (ex. 12345). It will carry out polynomial computations using the functions in the provided module. Requests are in one of two formats:
Evaluate Request 
Request starts with ‘E’ 
Followed by an argument value 
Followed by a single space 
Followed by the coefficients of a polynomial, separated by single spaces 
Bisection Request 
Requests starts with ‘S’ 
Followed by ‘a’, ‘b’, polynomial, tolerance separated by single spaces 
For example, here is a sample evaluate request:
E1.0 -945 1689 -950 230 -25 1
This is a request to evaluate the polynomial -945 + 1689x - 950x2 + 230x3 - 25x4 + x5 at the value x = 1.0
Here is a sample bisection request:
S0 2 -945 1689 -950 230 -25 1 1e-15
This requests the use of the bisection function with a = 0, b = 2, tolerance = 1e-15 and using the same polynomial as in the evaluate example.
The server will create a response to the client for each request. The first character of the response will indicate the type of response:
‘X’ indicates an error response. The remainder of the response is an error message 
‘E’ indicates a successful response to an evaluate request. This is immediately followed by the value returned by the evaluate function 
‘S’ indicates a successful response to a bisection request. This is immediately followed by the value returned by the bisection function 
The response to the example evaluate request would be2
    E2.2737367544323206e-13
The response to the example bisection request would be
    S1.0000000000000004
The server should operate in a continuing manner: the server should repeatedly accept a connection, get a request, send a response and close the connection to the client. In particular, only one request is handled for each connection.


