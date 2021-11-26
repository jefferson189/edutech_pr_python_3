import re

padrao = "\w{5,50}@[a-z]{3,10}.com.br"
texto = "aaabbbcc jeffeofdragon@hotmail.com.br ccbbbaaa"
resposta = re.search(padrao, texto)

print(resposta.group())