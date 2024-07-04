from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Luiz', 4)
restaurante_praca.receber_avaliacao('Alguém', 7)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()