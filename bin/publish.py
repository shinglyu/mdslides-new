import re
from slugify import slugify

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
    if title == None:
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
## Inline the pictures
# Save to file with filename

def main():
# Read the template
    with open('slide.html', 'r') as templatefile:
        template = ''.join(templatefile.readlines())
# print(template)

# Read the md
    with open('slide.md', 'r') as mdfile:
        md = ''.join(mdfile.readlines())

    title = getTitle(md)
    slugified_title = slugify(title)
    output = injectMd(template, md)
    with open(slugified_title + "_slide.html", 'w') as f:
        f.write(output)

if __name__ == "__main__":
    main()


