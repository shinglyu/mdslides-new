#!/usr/bin/env python
import re
from slugify import slugify
import base64
import os

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

## Change the title and filename
def injectHTMLTitle(template, title):
    p = re.compile('<title>(.*)</title>', re.DOTALL)
    return re.sub(p, '<title>' + title + ' (powered by MDSlides)</title>', template)

## Inline the pictures
def inlineLocalImg(md):
    newlines = []
    for line in md.split('\n'): #Assume picture is in its own line
        result = re.search(r'\!\[[\w\s]*\]\((.*)\)', line)
        if result is not None and not result.group(1).startswith('http'):

            path = result.group(1)
            for extension in ['png', 'jpg', 'gif']:
                if path.endswith(extension):
                    with open(path, "rb") as image: # Hey, relative path?
                        encoded_string = 'data:image/' + extension + ';base64,' + base64.b64encode(image.read())

            # TODO: inline svg
            newline = line.replace(path, encoded_string)
            newlines.append(newline)

        else:
            newlines.append(line)

    return '\n'.join(newlines)

# Save to file with filename

def main():
    # Read the template
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(script_path + '/../dist/slide.html', 'r') as templatefile: #FIXME: relative path only when run in base
        template = templatefile.read()

    # Read the md
    with open('slide.md', 'r') as mdfile:
        md = mdfile.read()

    title = getTitle(md)
    slugified_title = slugify(title)

    md_w_image = inlineLocalImg(md)
    template_w_title = injectHTMLTitle(template, title)
    output = injectMd(template_w_title, md_w_image)
    #inline template css

    with open(slugified_title + "_slide.html", 'w') as f:
        f.write(output)

if __name__ == "__main__":
    main()


