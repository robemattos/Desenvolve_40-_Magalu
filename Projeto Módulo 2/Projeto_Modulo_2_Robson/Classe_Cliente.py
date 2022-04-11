import datetime
import math

class Cliente:

    def locacao(self, qtd_bic, tipo_locacao, loja):
        self.qtd_bic = qtd_bic
        self.tipo_locacao = tipo_locacao
        self.loja = loja
        #self.dt_inicio = datetime.datetime(2022, 2, 20, 18, 55, 8, 202514) #datetime.datetime.today()
        self.dt_inicio = datetime.datetime.today()
        
        if self.tipo_locacao == 'h' or self.tipo_locacao == 'H':
            self.tipo_locacao = 'Hora'
            self.valor_locacao = 5
        elif self.tipo_locacao == 'd' or self.tipo_locacao == 'D':
            self.tipo_locacao = 'Dia'
            self.valor_locacao = 25
        elif self.tipo_locacao == 's' or self.tipo_locacao == 'S':
            self.tipo_locacao = 'Semana'
            self.valor_locacao = 100
        else:
            print('Tipo de locação inválido.')