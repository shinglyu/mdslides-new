#!/usr/bin/env python
import os
import difflib
from time import sleep
import subprocess
import requests
import argparse

root_url = "http://localhost:5000"
prev_content = []

def main(filename):

    watchfile = os.path.join(os.getcwd(), filename)
    print "----------"
    print "Watching file: {}".format(watchfile)
    print("Waiting for file change...")
    status = subprocess.call('inotifywait -e close {}'.format(watchfile), shell=True)
    print("File changed, reading the content")
    # print("prev: {}".format(prev_content))

    #print("CWD is:")
    #print(os.getcwd())
    #print("CWD contains:")
    #print(os.listdir(os.getcwd()))
    # sleep(0.5) # Dropbox will delete the file and create a temp file fo a while
    sleep(1) # Dropbox will delete the file and create a temp file fo a while
    #print(os.listdir(os.getcwd()))
    with open(watchfile, 'rb') as f:
        curr_content = f.readlines()
    global prev_content
    if prev_content == []:
        prev_content = curr_content

    d = difflib.Differ()
    diffs = d.compare(prev_content, curr_content)
    print(diffs)

    lineCount = 0
    changedLines = 0
    for line in diffs:
        #print(line)
        if line[:2] in ["  ", "+ "]:
            lineCount += 1
        if line[:2] in ["+ ", "- "]:
            changedLines = max(changedLines, lineCount)
            print("{}: {}".format(lineCount, line))

    if changedLines == 0:
        print("Nothing changed, continue")
        return

    #print(curr_content[:changedLines])
    #print(filter(lambda x: x.strip() == "---", curr_content[:changedLines]))
    changedPageNo = len(filter(lambda x: x.strip() == "---", curr_content[:changedLines])) + 1
    #print(changedPageNo)

    prev_content = curr_content
    print("Sending refresh signal, turn to page " + str(changedPageNo))
    #print(socketio)
    #socketio.emit('refresh', {'number': changedPageNo}, namespace='/test')
    r = requests.post('{root}/needrefresh/{pageno}'.format(root=root_url, pageno=changedPageNo))
    if (r.status_code == 200):
        print('OK!')
    else:
        print('Failed! {code} {reason}'.format(code=r.status_code, reason=r.reason))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Watch for slide markdown file change and notify the server to refresh")
    parser.add_argument("input_md", help="the input markdown file")
    args = parser.parse_args()

    while True:
        main(args.input_md)
