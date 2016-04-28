"""
Demo Flask application to test the operation of Flask with socket.io

Aim is to create a webpage that is constantly updated with random numbers from a background python process.

30th May 2014
"""

# Start with a basic flask app webpage.
import argparse
import difflib
from flask.ext.socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
import os
from random import random
import subprocess
from time import sleep
from threading import Thread, Event


__author__ = 'slynn'
watchfile= None
mdslides_root = os.path.dirname(os.path.realpath(__file__))
template = os.path.join(mdslides_root, 'template/template.html')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app)

#random number Generator Thread
thread = Thread()
thread_stop_event = Event()

class FileWatcherThread(Thread):
    def __init__(self, filename):
        print("Starting FileWatcherThread")
        self.filename=filename
        self.delay = 1
        self.prev_content = []
        super(FileWatcherThread, self).__init__()

    def watch(self):
        while True:
            #infinite loop of magical random numbers
            print "Watching file: {}".format(self.filename)
            # while not thread_stop_event.isSet():
            print("Setting up inotify")
            status = subprocess.call('inotifywait -e close {}'.format(self.filename), shell=True)
            # print self.prev_content
            print("File changed, re-reading the content")
            print("prev: {}".format(self.prev_content))

            with open(self.filename, 'rb') as f:
                curr_content = f.readlines()
            if self.prev_content == []:
                self.prev_content = curr_content

            d = difflib.Differ()
            diffs = d.compare(self.prev_content, curr_content)
            #print diffs

            lineCount = 0
            changedLines = 0
            for line in diffs:
                #print(line)
                if line[:2] in ["  ", "+ "]:
                    lineCount += 1
                if line[:2] in ["+ ", "- "]:
                    changedLines = max(changedLines, lineCount)
                    print("{}: {}".format(lineCount, line))

            #print(curr_content[:changedLines])
            #print(filter(lambda x: x.strip() == "---", curr_content[:changedLines]))
            changedPageNo = len(filter(lambda x: x.strip() == "---", curr_content[:changedLines])) + 1
            #print(changedPageNo)

            self.prev_content = curr_content
            print("Sending refresh signal, turn to page " + str(changedPageNo))
            socketio.emit('refresh', {'number': changedPageNo}, namespace='/test')

    def run(self):
        self.watch()

@app.route('/')
def index():
    # only by sending this page first will the client be connected to the socketio instance
    # By Flask default, files in statics/ will be served
    # TODO: cache the file
    print('In / handler')
    print('Reading template')
    with open(template, 'rb') as f:
        template_str = f.read()
    print('Reading test file')
    with open(watchfile, 'rb') as f:
        content_str = f.read()
        autoreload_scripts = """
            <script src="//cdnjs.cloudflare.com/ajax/libs/socket.io/0.9.16/socket.io.min.js"></script>
            <script src="static/js/application.js"></script>
        """
    print('Template replacing')
    template_str = template_str.replace('<!-- autoreload -->', autoreload_scripts)
    template_str = template_str.replace('<!-- MARKDOWN CONTENT -->', content_str)
    print('Serving')
    return template_str
    # return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print "Starting Thread"
        thread = FileWatcherThread(watchfile)
        # thread.daemon = True
        thread.start()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Create HTML5 slides with markdown")
    parser.add_argument("input_md", help="the input markdown file")
    args = parser.parse_args()

    watchfile = args.input_md
    print("Server started at http://localhost:5000")
    try:
        socketio.run(app)
    except KeyboardInterrupt:
        thread_stop_event.set()
        thread.join()
