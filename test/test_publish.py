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

def test_inlineLocalImg_no_local():
    md = "\n![cat](https://foo.bar.com/cat.jpg)\n"
    assert(publish.inlineLocalImg(md) == md)

def test_inlineLocalImg_local():
    md = "\n![cat](test/cat.png)\n" # Local file
    expected = "\n![cat](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAADOUlEQVR4XuWbsaoUMRSGrdViGhErB8HmKjKCjYU4jY3VFJYWg0+QykYupLWQgGIlMnY2FwYrbSSN1vMI8wh5hOMJuBbDJpmz/usmTuBjt1o2X5JzTjKTS0S0Cm4to/33/wmpAGK6HAVwq5me0Ux3TAGOqTPqeM9YhhZMTAMVsPjxKoMRtwxFmJkKJUAtDA8n7HzDOIZWMEAEBGyrE428Y0hA/VcCvMWAXcf0AWEVMzBOHjfSAyFExwWkgwwlcL8lKaZl+j2j1CKmfmQgTETOfJAAbh1DAFACVCrQhSSEMgJuraWpAQK6lFhuOiBAiQTcu39mX787p1f6JULAjAqAqQjPzQQEjFEBS9PPXzyj7z+/0J27ZwgBBpgFbGxWedkIASPPALr49pHef3hD129cA6x/eA1ghAFbSwSQx3fci7hy9fIfAU+ePia/NFjQagH/sEaYYoMgEhDCd/7rj8/08NED8s1/rilHmY4ZGLtA79InIkUGcF4QRMCt2zf90qBPF289fkZ4AUhmZmR0QIq0WPMMMAGMXxK+44FlAGdaIyKRshupgJmhzDAHVqtWvBnaFRMZMjG1cH/QHiKgYlymEhzTBs4pRKPvSW6CMsYwXWKgWrGApdmSSFd+8s0QlYb03DJqp2ABve/DVgVMkgpSUFsXg0YKsAUKaJEC9NYFqO0JKL8WUEgBVYECBoCAolOhBQgoOhMYtIB+M3WAfBaUnwXET2QLoDraKzKl7QPkAsqPBwohoOTqsAYIKDYoWsBrckXHgx4toKSzAgd4UbLoWGBOIaDOSEBzfAH4R2iaGVC5/zQCDu+AC77xKUedUoBGpazFUx4JFV7A8dOhjsSVSfr055QCGmjOlp9CKbAAOdAtq1xqk6eA9DSuEIHVC8tSQCo4HlBb2Fj6yy0I2oQAG1n7NnDpwQACIF5A4I+ZhACzp+NjLGAKMomYY1xc6Bi1NgAmOq8ZJQikWewGK6Zdu2tLLRVuOvQ7CNAV4JQokMaUgOWlrMXlC8eMyKt76NFXCQEqsJTaHfHcjgeZ+txu1ADrNnsBHWMX9Cu2yVWJAmBH52XdHcZnB7sVARTAbEVAx8x77hRWOQr4BawuLW/TjFULAAAAAElFTkSuQmCC)\n"
    assert(publish.inlineLocalImg(md) == expected)

def test_inlineLocalImg_local_space_in_name():
    md = ".halfwidth[![local cat](test/cat.png)]"
    expected = ".halfwidth[![local cat](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAADOUlEQVR4XuWbsaoUMRSGrdViGhErB8HmKjKCjYU4jY3VFJYWg0+QykYupLWQgGIlMnY2FwYrbSSN1vMI8wh5hOMJuBbDJpmz/usmTuBjt1o2X5JzTjKTS0S0Cm4to/33/wmpAGK6HAVwq5me0Ux3TAGOqTPqeM9YhhZMTAMVsPjxKoMRtwxFmJkKJUAtDA8n7HzDOIZWMEAEBGyrE428Y0hA/VcCvMWAXcf0AWEVMzBOHjfSAyFExwWkgwwlcL8lKaZl+j2j1CKmfmQgTETOfJAAbh1DAFACVCrQhSSEMgJuraWpAQK6lFhuOiBAiQTcu39mX787p1f6JULAjAqAqQjPzQQEjFEBS9PPXzyj7z+/0J27ZwgBBpgFbGxWedkIASPPALr49pHef3hD129cA6x/eA1ghAFbSwSQx3fci7hy9fIfAU+ePia/NFjQagH/sEaYYoMgEhDCd/7rj8/08NED8s1/rilHmY4ZGLtA79InIkUGcF4QRMCt2zf90qBPF289fkZ4AUhmZmR0QIq0WPMMMAGMXxK+44FlAGdaIyKRshupgJmhzDAHVqtWvBnaFRMZMjG1cH/QHiKgYlymEhzTBs4pRKPvSW6CMsYwXWKgWrGApdmSSFd+8s0QlYb03DJqp2ABve/DVgVMkgpSUFsXg0YKsAUKaJEC9NYFqO0JKL8WUEgBVYECBoCAolOhBQgoOhMYtIB+M3WAfBaUnwXET2QLoDraKzKl7QPkAsqPBwohoOTqsAYIKDYoWsBrckXHgx4toKSzAgd4UbLoWGBOIaDOSEBzfAH4R2iaGVC5/zQCDu+AC77xKUedUoBGpazFUx4JFV7A8dOhjsSVSfr055QCGmjOlp9CKbAAOdAtq1xqk6eA9DSuEIHVC8tSQCo4HlBb2Fj6yy0I2oQAG1n7NnDpwQACIF5A4I+ZhACzp+NjLGAKMomYY1xc6Bi1NgAmOq8ZJQikWewGK6Zdu2tLLRVuOvQ7CNAV4JQokMaUgOWlrMXlC8eMyKt76NFXCQEqsJTaHfHcjgeZ+txu1ADrNnsBHWMX9Cu2yVWJAmBH52XdHcZnB7sVARTAbEVAx8x77hRWOQr4BawuLW/TjFULAAAAAElFTkSuQmCC)]"
    assert(publish.inlineLocalImg(md) == expected)

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


