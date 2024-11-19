import math
import matplotlib.pyplot as plt

def menu():
    print("\n## Menu de Opções ## ")
    print("1. Calcular Seno (sin)")
    print("2. Calcular Cosseno (cos)")
    print("3. Calcular Tangente (tan)")
    print("0. Sair")
    print("----------------------------------")

'''def desenhar_triangulo(cateto1, cateto2):
    # Calcula a hipotenusa
    hipotenusa = (cateto1**2 + cateto2**2)**0.5

    # Coordenadas do triângulo
    x = [0, cateto1, 0, 0]  # Posição dos vértices no eixo x
    y = [0, 0, cateto2, 0]  # Posição dos vértices no eixo y

    # Criar o gráfico
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, 'b-', label='Triângulo Retângulo')  # Linhas do triângulo
    plt.fill(x, y, 'skyblue', alpha=0.3)  # Preenchimento do triângulo
    plt.scatter(x, y, color='red')  # Marca os vértices
    plt.text(cateto1 / 2, -0.5, f'Cateto1 = {cateto1}', ha='center')
    plt.text(-0.5, cateto2 / 2, f'Cateto2 = {cateto2}', va='center', rotation=90)
    plt.text(cateto1 / 2, cateto2 / 2, f'Hipotenusa = {hipotenusa:.2f}', color='green', ha='center')

    # Configurações do gráfico
    plt.title('Visualização do Triângulo Retângulo')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlim(-1, max(cateto1, cateto2) + 1)
    plt.ylim(-1, max(cateto1, cateto2) + 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.show() '''

def calcular_angulos(cateto1, cateto2, hipotenusa):
    # Calcula os ângulos
    angulo_a = math.degrees(math.asin(cateto2 / hipotenusa))  # Ângulo oposto a cateto2
    angulo_b = math.degrees(math.asin(cateto1 / hipotenusa))  # Ângulo oposto a cateto1

    return angulo_a, angulo_b

def executar(opcao, cateto1, cateto2, hipotenusa):
    angulo_a, angulo_b = calcular_angulos(cateto1, cateto2, hipotenusa)

    if opcao == 1:
        print("## SENO ## -> cateto oposto / hipotenusa")
        print(f"Seno do ângulo A: {math.sin(math.radians(angulo_a)):.2f}")
        print(f"Seno do ângulo B: {math.sin(math.radians(angulo_b)):.2f}")
    elif opcao == 2:
        print("## COSSENO ## -> cateto adjacente / hipotenusa")
        print(f"Cosseno do ângulo A: {math.cos(math.radians(angulo_a)):.2f}")
        print(f"Cosseno do ângulo B: {math.cos(math.radians(angulo_b)):.2f}")
    elif opcao == 3:
        print("## TANGENTE ## -> cateto oposto / cateto adjacente")
        print(f"Tangente do ângulo A: {math.tan(math.radians(angulo_a)):.2f}")
        print(f"Tangente do ângulo B: {math.tan(math.radians(angulo_b)):.2f}")
    elif opcao == 0:
        print("Saindo do programa...")
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
                executar(opcao)
                break
            executar(opcao, cateto1, cateto2, hipotenusa)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

if __name__ == "__main__":
    main()