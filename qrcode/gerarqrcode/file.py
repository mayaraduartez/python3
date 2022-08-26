import pyqrcode 
import png 
from pyqrcode import QRCode 
  

# link = input("Digite o link que deseja para gerar o código: ")
# nome = input("Digite um nome para o QRCode: ")

s = "https://github.com/mayaraduartez/python3/blob/main/teste.py"
url = pyqrcode.create(s) 
url.png("amandaaa", scale = 6) 