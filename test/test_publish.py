import sys
sys.path.append('bin') # Assume you run py.test in the root dir
import publish
def test_h1_title():
    md = "\n#Hello\n"
    assert(publish.getTitle(md) == "Hello")

def test_no_h1_title():
    md = "\nHello\n"
    assert(publish.getTitle(md) == "Hello")

def test_h1_title_after_h2_subtitle():
    md = "\n##Welcome to\n# Hello\n"
    assert(publish.getTitle(md) == "Hello")

def test_h1_title_with_spaces():
    md = "\n##Welcome to\n # Hello\n"
    assert(publish.getTitle(md) == "Hello")

def test_multiple_h1():
    md = "\n#Hello\n # World\n"
    assert(publish.getTitle(md) == "Hello")

def test_injectMd():
    template = '''
  <body onload="var slideshow = remark.create();">
    <textarea id="source">

class: center, middle

# Loading...

    </textarea>
    <script type="text/javascript">
    '''
    md = "#FooBar \n Hello \n* hehe"
    expected = '''
  <body onload="var slideshow = remark.create();">
    <textarea id="source">
#FooBar \n Hello \n* hehe
</textarea>
    <script type="text/javascript">
    '''
    assert(publish.injectMd(template, md) == expected)


