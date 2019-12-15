import pymysql as my
from Investimento.Funds_Explorer.Dados_FundsExplorer import Dados


class AdicionarFundosBanco(Dados):

    def __init__(self, url='https://www.fundsexplorer.com.br/ranking', host='localhost', database='', usuario='root', pasword=''):
        super(AdicionarFundosBanco, self).__init__(url)
        self.__dados = self.informacoes_fundos
        self.conexao = my.connect(
            host=host,
            user=usuario,
            passwd=pasword,
            database=database
        )
        self.cursor = self.conexao.cursor()

    def __script_dados(self, dados_funds_explorer):
        query = f'''Insert INTO founds_explorer(
        cd_fundo,
        setor ,
        v_atual,
        liquidez_d,
        dividendo,
        dividendYeld,
        DY_3m_acumulado,
        DY_6m_acumulado,
        DY_12m_acumulado,
        DY_3m_medio,
        DY_6m_medio,
        DY_12m_medio,
        DY_Ano,
        variacao_preco,
        rent_periodo,
        rent_acumulado,
        patri_liquido,
        VPA,
        P_VPA,  
        DYPatrimonial,
        VariaçãoPatrimonial,
        Rentab_Patr_no_Período,
        Rentab_Patr_Acumulada,
        VacânciaFísica,
        VacânciaFinanceira,
        QuantidadeAtivos,
        link
)
        VALUES(
        '{dados_funds_explorer['Códigodo fundo']}',
        '{dados_funds_explorer['Setor']}',
        {dados_funds_explorer['Preço Atual']},
        {dados_funds_explorer['Liquidez Diária']},
        {dados_funds_explorer['Dividendo']},
        {dados_funds_explorer['DividendYield ']},
        {dados_funds_explorer['DY (3M)Acumulado']},
        {dados_funds_explorer['DY (6M)Acumulado']},
        {dados_funds_explorer['DY (12M)Acumulado']},
        {dados_funds_explorer['DY (3M)Média']},
        {dados_funds_explorer['DY (6M)Média']},
        {dados_funds_explorer['DY (12M)Média']},
        {dados_funds_explorer['DY Ano']},
        {dados_funds_explorer['Variação Preço']},
        {dados_funds_explorer['Rentab.Período']},
        {dados_funds_explorer['Rentab.Acumulada']},
        {dados_funds_explorer['PatrimônioLíq.']},
        {dados_funds_explorer['VPA']},
        {dados_funds_explorer['P/VPA']},
        {dados_funds_explorer['DYPatrimonial']},
        {dados_funds_explorer['VariaçãoPatrimonial']},
        {dados_funds_explorer['Rentab. Patr.no Período']},
        {dados_funds_explorer['Rentab. Patr.Acumulada']},
        {dados_funds_explorer['VacânciaFísica']},
        {dados_funds_explorer['VacânciaFinanceira']},
        {dados_funds_explorer['QuantidadeAtivos']},
        '{dados_funds_explorer["link"]}'
        )
        '''
        return query

    def update_database(self, truncate=True):
        self.cursor.execute('truncate table founds_explorer') if truncate else None
        for fundo in self.__dados:
            query = self.__script_dados(fundo)
            self.cursor.execute(query)
            print(f'Fundo {fundo["Códigodo fundo"]} adicionado.')
        self.conexao.commit()

    def get_dados(self):
        return self.__dados

    def update(self, url='https://www.fundsexplorer.com.br/ranking', server='172.31.0.6', database='', usuario='nfe', pasword='nfe2019'):
        self.__init__(url, server, database, usuario, pasword)


if __name__ == '__main__':
    dados = AdicionarFundosBanco(database='Investimento')
    dados.update_database(truncate=False)
    print(dados.informacoes_fundos)
