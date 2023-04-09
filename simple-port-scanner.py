import socket

def port_scan(host, port):
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # set a timeout for the connection attempt
    s.settimeout(2)

    try:
        # try to connect to the specified host and port
        s.connect((host, port))

        # if the connection was successful, print a message indicating the port is open
        print(f"Port {port} is open on {host}")
        
    except:
        # if the connection failed, print a message indicating the port is closed
        print(f"Port {port} is closed on {host}")

    # close the socket
    s.close()

# specify the host and the range of ports to scan
host = 'localhost'
port_range = range(1, 1025)

# iterate over the range of ports and call the port_scan function for each one
for port in port_range:
    port_scan(host, port)
