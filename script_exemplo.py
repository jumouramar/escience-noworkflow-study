"""
Calculadora de Médias
=======================================

Descrição:
    Gera números aleatórios (entre 10.0 e 50.0);
    Calcula a média e salva o resultado em um arquivo.

Uso:
    python script_exemplo.py --qtd_numeros <quantidade>

Dependências:
    - numpy
"""

import argparse

import numpy as np


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--qtd_numeros", type=int, default=10)
    return parser.parse_args()

def generate_numbers(qtd_numeros):
    numbers = [round(np.random.uniform(10.0, 50.0), 2) for _ in range(qtd_numeros)]
    print(f"Dados gerados ({qtd_numeros}): {numbers}")
    return numbers

def calculate_average(numbers):
    average = round(float(np.mean(numbers)), 4)
    print(f"Média = {average}")
    return average

def save_result(average, qtd_numeros):
    with open("resultado.txt", "w") as f:
        f.write(f"qtd_numeros: {qtd_numeros}\n")
        f.write(f"media: {average}\n")
    print("Resultado salvo em resultado.txt")

if __name__ == "__main__":
    args = parse_args()
    numbers = generate_numbers(args.qtd_numeros)
    average = calculate_average(numbers)
    save_result(average, args.qtd_numeros)