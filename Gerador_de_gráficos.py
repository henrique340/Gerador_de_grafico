import matplotlib.pyplot as plt

def perguntas():
    altura = int(input('Digite a altura do gráfico: '))
    largura = int(input('Digite a largura do gráfico: '))
    cor = input('Digite a cor do gráfico: ')
    listaX = []
    listaY = []
    for x in range(largura):
        a = input(f'Digite o dado {x+1} de X: ')
        listaX.append(a)
    for y in range(altura):
        b = input(f'Digite o dado {y+1} de Y: ')
        listaY.append(b)

    plt.plot(listaX, listaY, color = 'Green')

def PerguntasExtras():
    titulo = input('Digite o título do gráfico: ')
    grade = input('Deseja colocar grade? [S]/[N]: ')
    moldura = input('Deseja colocar moldura? [S]/[N]: ')
    legenda = input('Digite a legenda do gráfico: ')
    legendaX = input('Digite a legenda X: ')
    legendaY = input('Digite a legenda Y: ')

# Principal

while True:
    print('-' * 60)
    print('GERADOR DE GRÁFICOS'.center(60))
    print('-' * 60)
    print("""
    Esse gerador cria um gráfico personalizado para você
    """)
    print('-' * 60)
    print('-' * 60)
    print('MENU'.center(60))
    print("""
    1 - Gerar gráfico
    2 - Sair
    """)
    escolha1 = int(input('Digite a opção: '))
    if escolha1 == 1:
        print("""
        A - Gráfico de linhas
        B - Gráfico de barras 
        C - Histograma
        D - Gráfico de pizza
        E - Gráfico de dispersão
        F - Gráfico de caixa
        """)

        escolha2 = input("Digite a opção desejada: ")
        if escolha2 == 'A' or escolha2 == 'a':
            perguntas()
            plt.plot(x, y, color='Green')
            plt.show()
    elif escolha1 == 2:
        break
    else:
        print("Erro, tente novamente")
