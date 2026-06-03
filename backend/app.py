from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Check if the request is for the root URL
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            
            # Response text encoded in UTF-8
            response_text = "Hello from Effective Mobile!"
            self.wfile.write(response_text.encode('utf-8'))
        else:
            # return 404 error for all other paths
            self.send_error(404, "Page Not Found")

def run():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    print("Server running at http://localhost:8080")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()

if __name__ == '__main__':
    run()

