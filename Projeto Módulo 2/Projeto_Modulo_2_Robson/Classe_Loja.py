import datetime
import math

class Loja:
    def __init__(self, estoque):
        self.estoque = estoque
        self.bic_alugadas = 0
        
    def recebe_locacao(self, cliente):
        self.cliente = cliente
        
        if self.estoque >= self.cliente.qtd_bic:
            self.qtd_bic = self.cliente.qtd_bic
            self.estoque -= self.cliente.qtd_bic
            self.bic_alugadas += self.cliente.qtd_bic
            self.aux_bic_alugadas = self.cliente.qtd_bic

            print(f'''
            Bicicletas Alugadas: {self.cliente.qtd_bic}
            Bicicletas Disponíveis: {self.estoque}
            Tipo de Locação: {self.cliente.tipo_locacao}
            Valor da Locação por Bicicleta: {self.cliente.valor_locacao}''')
        else:
            print('Quantidade de bicicletas insuficiente.')

    def devolve_locacao(self, cliente):
        self.cliente = cliente
        self.estoque += self.cliente.qtd_bic
        self.bic_alugadas -= self.cliente.qtd_bic
        self.dt_devolucao = datetime.datetime(2022, 2, 22, 22, 55, 8, 202514)
        #self.dt_devolucao = datetime.datetime.today()
        
    def calcula_conta(self, cliente):
        self.cliente = cliente
        self.periodo = (self.dt_devolucao - self.cliente.dt_inicio)
        if self.cliente.tipo_locacao == 'Hora':
            #self.periodo = math.ceil(self.periodo.hour)
            self.periodo = math.ceil(self.periodo.seconds / 3600)
        elif self.cliente.tipo_locacao == 'Dia':
            self.periodo = math.ceil(self.periodo.days)
        elif self.cliente.tipo_locacao == 'Semana':
            self.periodo = math.ceil(self.periodo.days) / 7
        
        if self.cliente.qtd_bic >= 3:
            self.valor_aluguel = (self.cliente.valor_locacao * (self.cliente.qtd_bic * self.periodo))
            self.valor_aluguel -= self.valor_aluguel * 0.3
            #return self.valor_aluguel

        else:    
            self.valor_aluguel = self.cliente.valor_locacao * (self.cliente.qtd_bic * self.periodo)
            #return self.valor_aluguel

        print(f'''
    Bicicletas Devolvidas: {self.cliente.qtd_bic}
    Bicicletas Disponíveis: {self.estoque}
    Tipo de Locação: {self.cliente.tipo_locacao}
    Período de Locação: {self.periodo}
    Valor da Locação: {self.cliente.valor_locacao}
    Valor do aluguel: {self.valor_aluguel}''')
    aux_bic_alugadas = 0