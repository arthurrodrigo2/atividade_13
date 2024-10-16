# programa_principal.py

import calculos

def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Por favor, insira um número válido.")

def main():
    print("Bem-vindo ao programa de cálculos matemáticos!")
    
    while True:
        print("\nEscolha uma operação:")
        print("1 - Calcular potência")
        print("2 - Calcular raiz quadrada")
        print("3 - Sair")
        
        escolha = input("Digite o número da operação desejada: ")
        
        if escolha == '1':
            base = obter_numero("Digite a base: ")
            expoente = obter_numero("Digite o expoente: ")
            resultado = calculos.calcular_potencia(base, expoente)
            print(f"{base} elevado a {expoente} é igual a {resultado}")
        elif escolha == '2':
            numero = obter_numero("Digite o número para calcular a raiz quadrada: ")
            resultado = calculos.calcular_raiz_quadrada(numero)
            print(f"A raiz quadrada de {numero} é {resultado}")
        elif escolha == '3':
            print("Obrigado por usar o programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()