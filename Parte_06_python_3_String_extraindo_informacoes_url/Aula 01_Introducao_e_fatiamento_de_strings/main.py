url ="bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

url_base = url[0:19]
print(url_base)  # Vai imprimir “bytebank.com/cambio”

url_parametro = url[20:36]
print(url_parametro)