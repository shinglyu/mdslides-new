import os
import sys

TEMPLATE_FILE = "{}/../template/template.html".format(os.path.dirname(__file__))
def main():
    print("Opening file {}".format(sys.argv[1]))
    with open(sys.argv[1], 'rb') as infile:
        mdsource = infile.read()

    with open(TEMPLATE_FILE, 'rb') as templatefile:
        template = templatefile.read()

    output = template.replace("<!-- MARKDOWN CONTENT -->", mdsource)

    print("Generated {}.html".format(sys.argv[1]))
    with open(sys.argv[1] + ".html", 'wb') as outfile:
        outfile.write(output)


if __name__ == '__main__':
    main()
