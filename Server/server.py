from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

PARAMS = "127.0.0.1", 8106

class HelloHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Receiving Info
        infos = []
        infos.append('client_address: %s' % str(self.client_address))
        infos.append('address_string: %s' % self.address_string())
        infos.append('command: %s' % self.command)
        infos.append('unparsed path: %s' % self.path)
        parsed = urlparse(self.path)
        infos.append('parsed path: %s' % parsed.path)
        infos.append('query: %s' % parsed.query)
        infos.append('request version: %s' % self.request_version)
        infos.append('server version: %s' % self.server_version)
        infos.append('sys version: %s' % self.sys_version)
        infos.append('protocol version: %s' % self.protocol_version)

        for k, v in self.headers.items():
            infos.append('HEADERS %s: %s' % (k, v.strip()))

                # Start of response
        self.send_response(200)
        self.send_header(b'Content-type', b'text/html')
        self.end_headers()

            # Navigation page header
        infos = b'<ul><li>' + b'</li><li>'.join([bytes(i, 'utf-8') for i in infos]) + b'</li></ul>'
        self.wfile.write(b"""<html><head><title>Hello World</title></head><body><p>Hello World</p>""" + infos + b"""</body></html>""")

        server = HTTPServer(PARAMS, HelloHandler)
        server.serve_forever()
        

