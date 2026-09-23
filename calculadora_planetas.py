"""
Calculadora de peso planetário.

Calcula o peso equivalente de uma pessoa em diferentes corpos celestes
a partir do peso informado na Terra.
"""

GRAVIDADES_PLANETAS = {
    "Mercúrio": 0.38,
    "Vênus": 0.91,
    "Terra": 1.00,
    "Marte": 0.38,
    "Júpiter": 2.34,
    "Saturno": 0.93,
    "Urano": 0.92,
    "Netuno": 1.12,
    "Lua": 0.165,
}


def calcular_pesos(peso_terrestre: float) -> dict[str, float]:
    """Retorna o peso equivalente em cada corpo celeste."""
    if peso_terrestre <= 0:
        raise ValueError("O peso deve ser maior que zero.")

    return {
        corpo_celeste: peso_terrestre * fator
        for corpo_celeste, fator in GRAVIDADES_PLANETAS.items()
    }


def exibir_resultados(peso_terrestre: float, pesos: dict[str, float]) -> None:
    """Exibe os resultados da simulação no terminal."""
    print("\n" + "=" * 50)
    print("🪐 SIMULAÇÃO DE PESO NO SISTEMA SOLAR 🚀")
    print("=" * 50)
    print(f"Peso informado na Terra: {peso_terrestre:.2f} kg\n")
    print(f"{'Corpo celeste':<15} | {'Peso calculado':>15}")
    print("-" * 35)

    for corpo_celeste, peso in pesos.items():
        print(f"{corpo_celeste:<15} | {peso:>12.2f} kg")

    print("=" * 50)


def main() -> None:
    """Executa a interface principal do programa."""
    print("=" * 50)
    print("🌌 BEM-VINDO À CALCULADORA DE PESO PLANETÁRIO 🌌")
    print("=" * 50)

    try:
        peso_usuario = float(input("Digite seu peso na Terra (kg): "))
        pesos = calcular_pesos(peso_usuario)
        exibir_resultados(peso_usuario, pesos)
    except ValueError:
        print("⚠️ Informe um número válido maior que zero.")


if __name__ == "__main__":
    main()
