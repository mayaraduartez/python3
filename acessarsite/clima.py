from bs4 import BeautifulSoup
import requests

#carrega a página
html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/349/bage-rs").content

#faz parser no html da pagina
soup = BeautifulSoup(html, "html.parser")

#captura dados navegando nos elementos do html
resume = soup.find(class_="-gray -line-height-24_center")
tempMin = soup.find(id="min-temp-1")
tempMax = soup.find(id="max-temp-1")

#mostra os resultados no terminal
print('\n Resumo: ' + str(resume))
print(' Temp. Mínima: ' + tempMin.string)
print(' Temp. Máxima: ' + tempMax.string)