from werkzeug.serving import make_server
import threading
import time
import flask
import logging as log
class ServerThread(threading.Thread):

    def __init__(self, app):
        print('init')
        threading.Thread.__init__(self)
        self.server = make_server('127.0.0.1', 5000, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        print('starting server')
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()

def start_server():
    global server
    app = flask.Flask('hello')
    # App routes defined here
    @app.route('/')
    def hello_world():
        return ' Ciao Hello, World! ciao bello come stai '
    server = ServerThread(app)
    server.start()
    print('server started')

def stop_server():
    global server
    server.shutdown()



    

if __name__ == "__main__":
    print('start main')
    start_server()
    time.sleep(60)
    stop_server()
    
    print('stop main')
    
