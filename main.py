PI = 3.141592653589793

def menu():
    print("----------------------------------")
    print("\n## Menu de Opções ## ")
    print("1. Calcular Seno (sin)")
    print("2. Calcular Cosseno (cos)")
    print("3. Calcular Tangente (tan)")
    print("4. Calcular Tudo Sen, Cos e Tan")
    print("0. Sair")
    print("----------------------------------")

def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def graus_para_radianos(graus):
    return graus * (PI / 180)

def seno(x, termos=10):
    x_rad = graus_para_radianos(x)
    resultado = 0
    for n in range(termos):
        termo = ((-1) ** n) * (x_rad ** (2 * n + 1)) / fatorial(2 * n + 1)
        resultado += termo
    return resultado

def cosseno(x, termos=10):
    x_rad = graus_para_radianos(x)
    resultado = 0
    for n in range(termos):
        termo = ((-1) ** n) * (x_rad ** (2 * n)) / fatorial(2 * n)
        resultado += termo
    return resultado

def tangente(x, termos=10):
    sen = seno(x, termos)
    cos = cosseno(x, termos)
    
    return sen / cos

def calcular_angulos(cateto1, cateto2, hipotenusa):
    def calcular_arcsin(x, termos=20):
        resultado = x
        termo = x
        for n in range(1, termos):
            termo *= (x * x * (2 * n - 1)) / (2 * n)
            resultado += termo / (2 * n + 1)
        return resultado

    seno_a = cateto1 / hipotenusa
    seno_b = cateto2 / hipotenusa

    angulo_a_rad = calcular_arcsin(seno_a)
    angulo_b_rad = calcular_arcsin(seno_b)

    angulo_a_graus = angulo_a_rad * (180 / PI)
    angulo_b_graus = angulo_b_rad * (180 / PI)

    return angulo_a_graus, angulo_b_graus

def executar(opcao, cateto1, cateto2, hipotenusa):
    angulo_a, angulo_b = calcular_angulos(cateto1, cateto2, hipotenusa)

    if opcao == 1:
        print(f"## SENO ## -> cateto oposto / hipotenusa\n"
                f"Seno do ângulo A: {seno(angulo_a):.2f}\n"
                f"Seno do ângulo B: {seno(angulo_b):.2f}")
        
    elif opcao == 2:
        print("## COSSENO ## -> cateto adjacente / hipotenusa\n"
                f"Cosseno do ângulo A: {cosseno(angulo_a):.2f}\n"
                f"Cosseno do ângulo B: {cosseno(angulo_b):.2f}")
        
    elif opcao == 3:
        print("## TANGENTE ## -> cateto oposto / cateto adjacente\n"
                f"Tangente do ângulo A: {tangente(angulo_a):.2f}\n"
                f"Tangente do ângulo B: {tangente(angulo_b):.2f}")
        
    elif opcao == 4:
        print("## SENO ## -> cateto oposto / hipotenusa\n"
                "## COSSENO ## -> cateto adjacente / hipotenusa\n"
                "## TANGENTE ## -> cateto oposto / cateto adjacente\n\n"
                f"Ângulo A - {angulo_a:.2f}\n"
                f"Seno do ângulo A: {seno(angulo_a):.2f}\n"
                f"Cosseno do ângulo A: {cosseno(angulo_a):.2f}\n"
                f"Tangente do ângulo A: {tangente(angulo_a):.2f}\n\n"
                f"Ângulo B - {angulo_b:.2f}\n"
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

    if cateto1 > cateto2:
        cateto_oposto_maior = cateto1
        cateto_oposto_menor = cateto2
    else:
        cateto_oposto_maior = cateto2
        cateto_oposto_menor = cateto1

    angulo_a, angulo_b = calcular_angulos(cateto_oposto_maior, cateto_oposto_menor, hipotenusa)

    print(f"\nCateto A = {cateto_oposto_maior}\n" 
          f"Cateto B = {cateto_oposto_menor} \n" 
          f"Hipotenusa = {hipotenusa:.2f} \n" 
          f"Ângulo A = {angulo_a:.2f} \n"
          f"Ângulo B = {angulo_b:.2f}")

    while True:
        menu()
        try:
            opcao = int(input("\nEscolha uma opção: "))
            if opcao == 0 or cateto_oposto_maior <= 0 or cateto_oposto_menor <= 0:
                executar(opcao, cateto_oposto_maior, cateto_oposto_menor, hipotenusa)
                break
            executar(opcao, cateto_oposto_maior, cateto_oposto_menor, hipotenusa)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

if __name__ == "__main__":
    main()