#!/usr/bin/python3
import cgi
import html

with open('vendor/remark-latest.min.js.script', 'rb') as f:
    content = f.read().decode('UTF-8')
    print(html.escape(content, quote=True))

