import math

def menu():
    print("\n## Menu de Opções ## ")
    print("1. Calcular Seno (sin)")
    print("2. Calcular Cosseno (cos)")
    print("3. Calcular Tangente (tan)")
    print("4. Calcular Tudo Sen, Cos e Tan")
    print("0. Sair")
    print("----------------------------------")

def fatorial(n):
    """Calcula o fatorial de um número."""
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def seno(x, termos=10):
    """Calcula o seno usando a série de Taylor."""
    x_rad = x * (3.141592653589793 / 180)  # Converte graus para radianos
    resultado = 0
    for n in range(termos):
        termo = ((-1) ** n) * (x_rad ** (2 * n + 1)) / fatorial(2 * n + 1)
        resultado += termo
    return resultado

def cosseno(x, termos=10):
    """Calcula o cosseno usando a série de Taylor."""
    x_rad = x * (3.141592653589793 / 180)  # Converte graus para radianos
    resultado = 0
    for n in range(termos):
        termo = ((-1) ** n) * (x_rad ** (2 * n)) / fatorial(2 * n)
        resultado += termo
    return resultado

def tangente(x, termos=10):
    """Calcula a tangente como seno/cosseno."""
    sen = seno(x, termos)
    cos = cosseno(x, termos)
    if cos == 0:
        return "Infinito (divisão por zero)"  # Evita divisão por zero
    return sen / cos

'''def calcular_angulos(cateto1, cateto2, hipotenusa):     ## ARRUMAAAAAAAAAAAAAAAAAAAAAAAR
    """Calcula os ângulos de um triângulo retângulo."""
    angulo_a = (cateto2 / hipotenusa) * 90  # Usando razão de proporcionalidade
    angulo_b = (cateto1 / hipotenusa) * 90 
    return angulo_a, angulo_b'''

def calcular_angulos(cateto1, cateto2, hipotenusa):
    # Calcula os ângulos
    angulo_a = math.degrees(math.asin(cateto2 / hipotenusa))  # Ângulo oposto a cateto2
    angulo_b = math.degrees(math.asin(cateto1 / hipotenusa))  # Ângulo oposto a cateto1

    return angulo_a, angulo_b

def executar(opcao, cateto1, cateto2, hipotenusa):
    angulo_a, angulo_b = calcular_angulos(cateto1, cateto2, hipotenusa)

    if opcao == 1:
        print(f"## SENO ## -> cateto oposto / hipotenusa\n"
                f"(PROVA REAL) Seno do ângulo A: {math.sin(math.radians(angulo_a)):.2f}\n"  ## TIRAR PROVA REAL
                f"(PROVA REAL) Seno do ângulo B: {math.sin(math.radians(angulo_b)):.2f}\n"  ## TIRAR PROVA REAL
                f"Seno do ângulo A: {seno(angulo_a):.2f}\n"
                f"Seno do ângulo B: {seno(angulo_b):.2f}")
        
    elif opcao == 2:
        print("## COSSENO ## -> cateto adjacente / hipotenusa\n"
                f"(PROVA REAL) Cosseno do ângulo A: {math.cos(math.radians(angulo_a)):.2f}\n"  ## TIRAR PROVA REAL
                f"(PROVA REAL) Cosseno do ângulo B: {math.cos(math.radians(angulo_b)):.2f}\n"  ## TIRAR PROVA REAL
                f"Cosseno do ângulo A: {cosseno(angulo_a):.2f}\n"
                f"Cosseno do ângulo B: {cosseno(angulo_b):.2f}")
        
    elif opcao == 3:
        print("## TANGENTE ## -> cateto oposto / cateto adjacente\n"
                f"(PROVA REAL) Tangente do ângulo B: {math.tan(math.radians(angulo_b)):.2f}\n"  ## TIRAR PROVA REAL
                f"(PROVA REAL) Tangente do ângulo A: {math.tan(math.radians(angulo_a)):.2f}\n"  ## TIRAR PROVA REAL
                f"Tangente do ângulo A: {tangente(angulo_a):.2f}\n"
                f"Tangente do ângulo B: {tangente(angulo_b):.2f}")
        
    elif opcao == 4:
        print("## SENO ## -> cateto oposto / hipotenusa\n"
                "## COSSENO ## -> cateto adjacente / hipotenusa\n"
                "## TANGENTE ## -> cateto oposto / cateto adjacente\n\n"
                "Ângulo A\n"
                f"Seno do ângulo A: {seno(angulo_a):.2f}\n"
                f"Cosseno do ângulo A: {cosseno(angulo_a):.2f}\n"
                f"Tangente do ângulo A: {tangente(angulo_a):.2f}\n\n"
                "Ângulo B\n"
                f"Seno do ângulo B: {seno(angulo_b):.2f}\n"
                f"Cosseno do ângulo B: {cosseno(angulo_b):.2f}\n"
                f"Tangente do ângulo B: {tangente(angulo_b):.2f}")
        
    elif opcao == 0:
        print("\nSaindo do programa...")
        
    else:
        print("Opção inválida. Por favor, tente novamente.")

def main():
    print("Cálculo do triângulo retângulo!")
    cateto1 = float(input("Digite o comprimento do primeiro cateto: "))
    cateto2 = float(input("Digite o comprimento do segundo cateto: "))
    hipotenusa = (cateto1**2 + cateto2**2)**0.5

    print(f"C1 = {cateto1} # C2 = {cateto2} # Hi = {hipotenusa} # AA e AB = {calcular_angulos(cateto1, cateto2, hipotenusa)}")

    while True:
        menu()
        try:
            opcao = int(input("\nEscolha uma opção: "))
            if opcao == 0 or cateto1 <= 0 or cateto2 <= 0:
                executar(opcao, cateto1, cateto2, hipotenusa)
                break
            executar(opcao, cateto1, cateto2, hipotenusa)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

if __name__ == "__main__":
    main()