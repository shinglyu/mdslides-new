import convert

def test_pages():
    md_source = """
    #123
    ---
    ## 456
    """

    expected = '''
    <div class="page">
    <h1>123</h1>
    </div>
    <div class="page">
    <h2>456</h2>
    </div>
    '''

    actual = convert.convert_all(md_source)
    assert expected == actual

def test_md_source_to_page_array():
    md_source = """
#123
#234
---
## 456
"""

    expected = ['<h1>123</h1>\n<h1>234</h1>', '<h2>456</h2>'] # The newline char is expected. When passed into a jinja template it will be treated as new line

    actual = convert.source_to_md_array(md_source)
    assert expected == actual
