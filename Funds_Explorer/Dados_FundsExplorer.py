import requests
from bs4 import BeautifulSoup as bs


class Dados(object):

    def __init__(self, url='https://www.fundsexplorer.com.br/ranking'):
        self.url = url
        self.informacoes_fundos = self.__conteudo_fundos(self.url)

    def __conteudo_fundos(self, url):
        content = requests.get(url=url).content
        resultado = bs(content, 'html.parser')
        cabecalho = resultado.find('thead').find_all('th')
        fundos = resultado.find('tbody').find_all('tr')
        dados = [ ]
        for fundo in fundos:
            cab = 0
            dados_por_fundo = { }
            for informacao in str(fundo.text).split('\n'):
                if informacao:
                    dados_por_fundo[ cabecalho[cab].text ] = self.__tratamento_numeros(informacao)
                    cab += 1
            dados_por_fundo['link'] = f'https://www.fundsexplorer.com.br/funds/{dados_por_fundo["Códigodo fundo"]}'
            dados.append(dados_por_fundo)
        return dados

    def update(self, url):
        self.__init__(url)

    @staticmethod
    def __tratamento_numeros(numero_string):
        try : return int(numero_string)
        except ValueError : pass

        numero = str(numero_string)\
            .replace('%', '')\
            .replace(' ', '')\
            .replace('R$', '')\
            .replace(',', '')\
            .replace('.', '')\
            .replace('N/A', '0.0')

        try: return  int(numero) / 100
        except ValueError:return numero


if __name__ == '__main__':
    url = 'https://www.fundsexplorer.com.br/ranking'
    found = Dados(url=url)
    fundos = found.informacoes_fundos
    print(fundos)
