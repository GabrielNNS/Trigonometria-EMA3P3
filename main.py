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
    """Calcula o fatorial de um número."""
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def graus_para_radianos(graus):
    """Converte graus para radianos."""
    pi = 3.141592653589793
    return graus * (pi / 180)

def seno(x, termos=10):
    """Calcula o seno usando a série de Taylor."""
    x_rad = graus_para_radianos(x)
    resultado = 0
    for n in range(termos):
        termo = ((-1) ** n) * (x_rad ** (2 * n + 1)) / fatorial(2 * n + 1)
        resultado += termo
    return resultado

def cosseno(x, termos=10):
    """Calcula o cosseno usando a série de Taylor."""
    x_rad = graus_para_radianos(x)
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
        return "Infinito (divisão por zero)"
    return sen / cos

def calcular_angulos(cateto1, cateto2, hipotenusa):
    """Calcula os ângulos do triângulo retângulo usando arcsin."""
    def calcular_arcsin(x, termos=20):
        """Calcula arcsin(x) usando a série de Taylor."""
        resultado = x
        termo = x
        for n in range(1, termos):
            termo *= (x * x * (2 * n - 1)) / (2 * n)
            resultado += termo / (2 * n + 1)
        return resultado

    if cateto1 > cateto2:
        cateto_oposto_maior = cateto1
        cateto_oposto_menor = cateto2
    else:
        cateto_oposto_maior = cateto2
        cateto_oposto_menor = cateto1

    # Calcula os senos dos ângulos
    seno_a = cateto_oposto_maior / hipotenusa
    seno_b = cateto_oposto_menor / hipotenusa

    # Calcula os ângulos em radianos
    angulo_a_rad = calcular_arcsin(seno_a)
    angulo_b_rad = calcular_arcsin(seno_b)

    # Converte para graus
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

    print(f"\nCateto A = {cateto1}\n" 
          f"Cateto B = {cateto2} \n" 
          f"Hipotenusa = {hipotenusa} \n" 
          f"Angulos A e B = {calcular_angulos(cateto1, cateto2, hipotenusa)}")

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