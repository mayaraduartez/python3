import PyPDF2

pdfFileObj = open('meupdf.pdf', 'rb') #carrega o arquivo pdf da minha pasta

pdfReader = PyPDF2.PdfFileReader(pdfFileObj) #faz a leitura do arquivo

pageObj = pdfReader.getPage(0) #captura a primeira página

text = pageObj.extractText() # extrai do texto e passa para a variavel

print(text) #mostra o texto no terminal