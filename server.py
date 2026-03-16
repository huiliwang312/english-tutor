import http.server
import ssl
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

server = http.server.HTTPServer(('0.0.0.0', 8443), http.server.SimpleHTTPRequestHandler)
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
base = os.path.dirname(os.path.abspath(__file__))
ctx.load_cert_chain(
    os.path.join(base, 'cert.pem'),
    os.path.join(base, 'key.pem')
)
server.socket = ctx.wrap_socket(server.socket, server_side=True)

print("HTTPS server running at https://10.0.0.11:8443")
server.serve_forever()
