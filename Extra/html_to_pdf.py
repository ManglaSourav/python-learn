import pdfkit


# pdfkit.from_url('file:///Users/souravmangla/Desktop/Grokking%20Modern%20System%20Design%20Interview%20for%20Engineers%20&%20Managers/1.%20System%20Design%20Interviews/1.%20What%20Is%20a%20System%20Design%20Interview_.html', 'out.pdf')

options = {
    # 'page-size': 'A4',
    # 'margin-top': '0.75in',
    # 'margin-right': '0.75in',
    # 'margin-bottom': '0.75in',
    # 'margin-left': '0.75in',
    # 'encoding': "UTF-8",
    # 'image-quality':'20',
    # 'no-pdf-compression':'',
    # 'enable-local-file-access': None,
    # 'custom-header': [
    #     ('Accept-Encoding', 'gzip')
    # ],
    # 'image-dpi': 400,
    # 'lowquality': True
    # 'cookie': [
    #     # ('cookie-empty-value', '""')
    #     ('cookie-name1', 'cookie-value1'),
    #     ('cookie-name2', 'cookie-value2'),
    # ],
    # 'no-outline': None
}

pdfkit.from_file(
    '/Users/souravmangla/Desktop/Do/python-learn/Extra/file1.html', 'out.pdf',  options=options)


# import weasyprint
# pdf = weasyprint.HTML('http://www.google.com').write_pdf()
