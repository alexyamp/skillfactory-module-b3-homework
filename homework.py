from yattag import Doc
from yattag import indent

doc, tag, text = Doc().tagtext()

with tag('html'):
    with tag('head'):
        with tag('title'):
            text('hello')
    with tag('body'):
        with tag('h1', klass=('main-text')):
            text('Test')
        with tag('div', klass='container container-fluid', id='lead'):
            with tag('p'):
                text = 'another test'
            doc.stag('img', src='/icon.png', data_image='responsive')
            
result = indent(doc.getvalue())

with open('/Users/admin/Downloads/test.html', 'w') as f:
    f.write(result)
