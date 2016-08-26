#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from slugify import slugify
import base64
import os
import sys
import Image
import base64
import cStringIO



template_file = os.path.join("..","template", "template.html")
css_files = ["static/style/slide.css", "static/style/monokai-sublime.css"]

# Extract the filename

def getTitle(md):
    title = None
    for line in md.split('\n'):
        result = re.search('^\s*#\s*(\w.*)', line)
        if result is not None:
            #print result.group(1)
            title = result.group(1).strip()
            break
        # print(result.group(0))
    if title is None:
        for line in md.split('\n'):
            if line.strip() != '':
                title = line.strip()
                break
    return title

# Inject the md

def injectMd(template, md):
    p = re.compile('<textarea id="source">(.*)</textarea>', re.DOTALL)
    return re.sub(p, '<textarea id="source">\n' + md + '\n</textarea>', template)
    #return template

def injectCSS(template, files):
    script_path = os.path.dirname(os.path.realpath(__file__)) # XXX:repeat
    for cssfile in files:
        with open(os.path.join(script_path, "..", cssfile), 'rb') as f:
            css = f.read()
        template = template.replace(
            '<link rel="stylesheet" href="{}" type="text/css" media="all" />'.format(cssfile),
            '<style>{}</style>'.format(css)
        )
    return template

## Change the title and filename
def injectHTMLTitle(template, title):
    p = re.compile('<title>(.*)</title>', re.DOTALL)
    return re.sub(p, '<title>' + title + ' (powered by MDSlides)</title>', template)

## Inline the pictures
def resizeImage(path):
    #max_width=1024
    #max_height=768
    max_size = 800,600 #width, height

    img = Image.open(path)# .convert('RGBA')
    img.thumbnail(max_size)
    return img

def inlineLocalImg(md):
    newlines = []
    for line in md.split('\n'): #Assume picture is in its own line
        # TODO: handle
        # background-image: url('pic/mozlondon-7.jpg')

        md_result = re.search(r'\!\[[^\]*]*\]\((.*)\)', line)
        html_result = re.search(r'<img [^>]*src="([^"]+)"', line)
        if md_result is not None:
            path = md_result.group(1)
        elif html_result is not None:
            path = html_result.group(1)
        else:
            newlines.append(line)
            continue

        if not path.startswith('http') and \
            any(map(lambda ext: path.endswith(ext), ['png', 'jpg', 'gif'])):
            extension = path[-3:] # TODO: handle extensions other then 3 chars

            buffer = cStringIO.StringIO()
            img = resizeImage(path)
            img.save(buffer, format="PNG")
            img_str = base64.b64encode(buffer.getvalue())
            encoded_string = 'data:image/' + extension + ';base64,' + img_str

            newline = line.replace(path, encoded_string)
            newlines.append(newline)

        elif not path.startswith('http') and path.endswith('svg'):

            with open(path, 'rb') as f:
                file_content = f.read()
            # We can directly inline svg without base64 encoding, but escaping
            # The string is too complicated
            # encoded_string = "data:image/svg+xml;charset=utf-8," + img_str.replace('\n', '')

            img_str = base64.b64encode(file_content)
            encoded_string = 'data:image/svg+xml;base64,' + img_str

            newline = line.replace(path, encoded_string)
            newlines.append(newline)

        else:
            newlines.append(line)

    return '\n'.join(newlines)

# Save to file with filename

def main():
    # Read the template
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, template_file), 'rb') as templatefile: #FIXME: relative path only when run in base
        template = templatefile.read()

    # Read the md
    with open('slide.md', 'r') as mdfile:
        md = mdfile.read()

    title = getTitle(md)
    slugified_title = slugify(unicode(title))
    print "Filename: {}. \t Do you wish to change it? \nInput a custom filename or [Enter] to skip:".format(slugified_title)

    custom_title=raw_input()
    if custom_title != '':
        slugified_custom_title = slugify(unicode(custom_title))
        print "Filename: {}. Is that OK? [Y/n]".format(slugified_custom_title)
        yes=raw_input()
        if yes == '' or yes == 'y' or yes == 'Y':
            slugified_title=slugified_custom_title
        else:
            print "Abort. No file was generated"
            sys.exit()




    md_w_image = inlineLocalImg(md)
    template_w_title = injectHTMLTitle(template, title)
    template_w_title = injectMd(template_w_title, md_w_image)
    output = injectCSS(template_w_title, css_files)
    #inline template css

    full_filename = slugified_title + "_slide.html"
    with open(full_filename, 'w') as f:
        f.write(output)
    print "file://{}/{} was generated".format(os.getcwd(), full_filename)
if __name__ == "__main__":
    main()


