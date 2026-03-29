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
import json
import os
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

def read_results():
    if not os.path.exists("resultado.json"):
        return []
    with open("resultado.json", "r", encoding="utf-8") as f:
        resultados = json.load(f)
        if not isinstance(resultados, list):
            resultados = [resultados]
        return resultados

def save_result(results, numbers, average, qtd_numeros):
    resultado = {
        "qtd_numeros": qtd_numeros,
        "numeros": numbers,
        "media": average
    }
    results.append(resultado)
    with open("resultado.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)



if __name__ == "__main__":
    args = parse_args()
    numbers = generate_numbers(args.qtd_numeros)
    average = calculate_average(numbers)
    results = read_results()
    save_result(results, numbers, average, args.qtd_numeros)