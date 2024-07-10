import sys
from crayons import red

def cabecalho():
    print("")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("CALCULATOR")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("")

def transforma_sinal():
    global sinal
    global sinal2
    if sinal == 1:
        sinal2 = "+"
    elif sinal == 2:
        sinal2 = "-"
    elif sinal == 3:
        sinal2 = "x"
    elif sinal == 4:
        sinal2 = "/"
    else:
        print("ERRO. PROVAVELMENTE VOCE ESCOLHEU UMA OPCAO DIFERENTE DE 1, 2, 3 ou 4.")

def calculo():
    global resultado
    if sinal == 1:
        resultado = num1 + num2
    elif sinal == 2:
        resultado = num1 - num2
    elif sinal == 3:
        resultado = num1 * num2
    elif sinal == 4:
        if num2 == 0:
            print("\nErro: divisao por zero\n")
            sys.exit()
        else:
            resultado = num1 / num2

cabecalho()

num1 = float(input("Digite o primeiro numero: "))
sinal = int(input("Digite uma opcao entre: SOMAR(1), SUBTRAIR(2), MULTIPLICAR(3) ou DIVIDIR(4): "))
num2 = float(input("Digite o segundo numero: "))
sinal2 = ""
transforma_sinal()
resultado = 0
calculo()

print(f"\nVoce solicitou calcular o seguinte: {num1} {sinal2} {num2}")
print("")
print(red(f"E o resultado do calculo e: {resultado}"))
print("")


