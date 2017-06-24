import markdown

def source_to_md_array(md_source):
    raw_pages = md_source.split('---') # TODO: Be more robust here, how about '------'?
    md = markdown.Markdown()
    pages = map(md.convert, raw_pages)
    return list(pages)


