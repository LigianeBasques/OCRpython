# 1º coletar imagens, que contenham textos;
# 2º colocar na pasta images;
# 3º fazer um script que liste os arquivos da pasta images;
# 4º criar uma lista com os caminhos dos arquivos que foram listados na etapa 3.

import os


diretorio = 'images'

arquivos = os.listdir(diretorio)
#print(arquivos)
print(len(arquivos))
for arquivo in arquivos:
    print(arquivo)


lista = []
lista.append(arquivos)
print(lista)




