"""
Módulo: Simulador de Gravidade Planetária
Autor: Marcella Bongiolo
Descrição: Script em Python que calcula o peso corporal de um usuário
           em diferentes corpos celestes do Sistema Solar com base na gravidade relativa.
"""

# Dicionário com a gravidade superficial relativa à Terra (m/s² ou fator multiplicativo)
GRAVIDADES_PLANETAS = {
    "Mercúrio": 0.38,
    "Vênus": 0.91,
    "Terra": 1.00,
    "Marte": 0.38,
    "Júpiter": 2.34,
    "Saturno": 0.93,
    "Urano": 0.92,
    "Netuno": 1.12,
    "Lua": 0.165
}

def calcular_pesos(peso_terrestre: float):
    """Calcula e exibe o peso correspondente em cada planeta."""
    print("\n" + "=" * 50)
    print(" 🪐 SIMULAÇÃO DE PESO NO SISTEMA SOLAR 🚀")
    print("=" * 50)
    print(f"Peso base na Terra: {peso_terrestre:.2f} kg\n")
    print(f"{'Planeta':<15} | {'Peso Calculado':<15}")
    print("-" * 35)
    
    for planeta, fator in GRAVIDADES_PLANETAS.items():
        peso_planeta = peso_terrestre * fator
        print(f"{planeta:<15} | {peso_planeta:.2f} kg")
        
    print("=" * 50)

def main():
    try:
        print("=" * 50)
        print(" 🌌 BEM-VINDO AO CALCULADOR DE PESO PLANETÁRIO 🌌")
        print("=" * 50)
        
        peso_usuario = float(input("Digite o seu peso atual na Terra (kg): "))
        
        if peso_usuario <= 0:
            print("⚠️ Por favor, insira um valor de peso válido maior que zero.")
            return
            
        calcular_pesos(peso_usuario)
        
    except ValueError:
        print("⚠️ Erro: Insira apenas números válidos.")

if __name__ == "__main__":
    main()
