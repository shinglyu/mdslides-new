import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def browser(request):
    browser = webdriver.Firefox()
    def fin():
        browser.close()
    request.addfinalizer(fin)
    return browser# provide the fixture value

@pytest.mark.skipif(True, reason="Wait until the specify text file function is ready, otherwise we can't specify the test md file")
def test_launch(browser):

    # TODO: extract the setup and teardown
    browser.get('http://localhost:9876')
    assert 'MDSlides' in browser.title

    #import time
    #time.sleep(50)
    editorText = browser.find_element_by_class_name('CodeMirror').text
    #element = WebDriverWait(ff, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
    assert "Hello world" in editorText

    slideFrame = browser.find_element_by_id('previewIframe')
    browser.switch_to_frame(slideFrame)
    slideText = browser.find_element_by_class_name('remark-slides-area').text
    assert "Hello world" in slideText

def test_input(browser):

    browser.get('http://localhost:9876')
    assert 'MDSlides' in browser.title

    #import time
    #time.sleep(50)
    #editor = browser.find_element_by_css_selector('.CodeMirror textarea')
    browser.execute_script('window.editor.setValue("#Customized String")')
    #editor = browser.find_element_by_tag_name('html')
    #element = WebDriverWait(ff, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
    #editor.send_keys('iI am typing!')

    slideFrame = browser.find_element_by_id('previewIframe')
    browser.switch_to_frame(slideFrame)
    #slideText = browser.find_element_by_class_name('remark-slides-area').text
    WebDriverWait(browser, 1).until(
        #EC.text_to_be_present_in_element((By.CLASS_NAME, "remarks-slides-content"), 'I am typing!')
        EC.presence_of_element_located((By.ID, 'customized-string'))
    )
    #assert "I am typing!" in slideText

