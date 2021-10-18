import re

class UrlExtractor:
    def __init__(self, url):
        self.sanitiza_url(url)
        self.valida_url(url)
        self.url = url
        self.start_parametros = url.find("?")
        self.url_base = url[:self.start_parametros]
        self.parametros = url[self.start_parametros+1:]

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self, url):
        if not self.url:
            raise ValueError("A URL está vazia")

        matcher = re.compile("((http(s)?://)?(www.))?bytebank.com(.br)?/cambio")
        verifica = matcher.match(url)

        if not verifica:
            raise ValueError("A URL não é válida")

    def get_valor_parametro(self, parametro):
        indice_parametro = self.parametros.find(parametro)
        fim_parametro = self.parametros.find("&", indice_parametro+1)
        if fim_parametro == -1:
            return self.parametros[indice_parametro+len(parametro)+1:]
        else:
            return self.parametros[indice_parametro + len(parametro) + 1:fim_parametro]

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
ue = UrlExtractor(url)

print(ue.get_valor_parametro("quantidade"))
print(ue.get_valor_parametro("moedaOrigem"))
print(ue.get_valor_parametro("moedaDestino"))