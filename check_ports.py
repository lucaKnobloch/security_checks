import socket


def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(port)
        return True
    except:
        return False


found_open = False
for port in range(1, 1024):
    is_open = scan_port(port)
    if is_open:
        found_open = True
        print(f'Port {port} is open.')

if not found_open:
    print('All ports are closed ')
