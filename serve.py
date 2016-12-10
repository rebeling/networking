import SimpleHTTPServer
import SocketServer
PORT = 8000


def main():
    """Create a web server and serve the gui."""
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "serving at port", PORT
    httpd.serve_forever()


if __name__ == '__main__':
    main()
