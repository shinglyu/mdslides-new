import argparse
from flask import Flask, send_from_directory, abort
import json
from time import time
import os.path

# Global settings
watchfile = None # Set in main() from command line arg
mdslides_root = os.path.dirname(os.path.realpath(__file__))
template = os.path.join(mdslides_root, 'template/template.html')

# Global data as DB
template_str = "Fail to load template!"
refresh_flag = {
    'timestamp': 0,
    'page': 1
}

app = Flask(__name__)

@app.route('/')
def serve_slides():
    print('Reading content file')
    with open(watchfile, 'rb') as f:
        content_str = f.read()
    autoreload_scripts = """
        <script src="static/js/application.js"></script>
    """
    print('Template processing')
    global template_str
    # template_str is global, do not modify it, make a copy
    return template_str.replace('<!-- autoreload -->', autoreload_scripts)\
                       .replace('<!-- MARKDOWN CONTENT -->', content_str)


@app.route('/pic/<path:path>')
def send_pic(path):
    try:
        pic = send_from_directory(os.path.join(os.getcwd(),'pic'), path)
        return pic
    except:
        abort(404)


@app.route('/needrefresh/', methods=['GET'])
def get_need_refresh():
    return json.dumps(refresh_flag)


@app.route('/needrefresh/<int:page_no>', methods=['POST'])
def set_need_refresh(page_no):
    refresh_flag['timestamp'] = time()
    refresh_flag['page'] = page_no
    return 'OK'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create HTML5 slides with markdown")
    parser.add_argument("input_md", help="the input markdown file")
    args = parser.parse_args()

    watchfile = args.input_md

    with open(template, 'rb') as f:
        template_str = f.read()

    app.run(threaded=True) # Use threaded to reduce AJAX disconnect broken pipe
