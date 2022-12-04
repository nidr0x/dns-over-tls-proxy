import ssl
from multiprocessing import Process
import socket

class DNSResolver:
  def main(self):
    try:
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((self.LISTEN_IP, self.LISTEN_PORT))
        s.listen()
        while True:
          conn = s.accept()[0]
          data = conn.recv(1024)

          if not data:
            break
          proc = Process(target=self.tcp, args=(conn, data))
          proc.start()
    except Exception:
      conn.close()

  def dns_query(self, query):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)

    wrapped_socket = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=self.DNS_ADDR)
    wrapped_socket.connect((self.DNS_ADDR, self.DNS_PORT))
    wrapped_socket.send(query)

    data = wrapped_socket.recv(1024)

    return data

  def tcp(self, conn, data):
    response = self.dns_query(data)
    if response:
      conn.sendto(response, conn.getpeername())
    else:
      print('Error in DNS query: \n', data)
      conn.close()

  def __init__(self):
    self.DNS_ADDR = '1.1.1.1'
    self.DNS_PORT = 853
    self.LISTEN_IP = '0.0.0.0'
    self.LISTEN_PORT = 53

if __name__ == '__main__':
  lookup = DNSResolver()
  lookup.main()
