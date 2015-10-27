import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="module")
def browser(request):
    browser = webdriver.Firefox()
    def fin():
        browser.close()
    request.addfinalizer(fin)
    return browser# provide the fixture value

def test_launch(browser):


    browser.get('http://localhost:9876')
    assert 'MDSlides' in browser.title

    editorText = browser.find_element_by_class_name('CodeMirror').text
    assert "Hello world" in editorText

    slideFrame = browser.find_element_by_id('previewIframe')
    browser.switch_to_frame(slideFrame)
    slideText = browser.find_element_by_class_name('remark-slides-area').text
    assert "Hello world" in slideText


