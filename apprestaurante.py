from modelos.restaurantes import Restaurante

restaurante_praca = Restaurante('sebo sabores','seboso')
restaurante_praca.receber_avaliacao('B', 1)
restaurante_praca.receber_avaliacao('C', 4)
restaurante_praca.receber_avaliacao('D', 0)
restaurante_praca.receber_avaliacao('E', 1)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()