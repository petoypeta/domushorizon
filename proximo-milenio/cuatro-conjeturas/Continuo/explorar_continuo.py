import json

# 1. Diagonal argument demonstration over a finite list of "real numbers" in (0,1)
samples = [
    "314159265359",
    "271828182846",
    "161803398875",
    "141421356237",
    "066987298092",
    "057721566490",
]

def build_diagonal_counterexample(sample_list):
    length = min(len(sample_list), min(len(s) for s in sample_list))
    result = []
    for i in range(length):
        d = int(sample_list[i][i])
        new_d = (d + 1) % 9
        result.append(str(new_d))
    return "".join(result)

counterexample = build_diagonal_counterexample(samples)

diffs = []
for i, s in enumerate(samples):
    diffs.append(s[i] != counterexample[i])

# 2. Countability of rationals: Calkin-Wilf enumeration
from math import gcd

def enumerate_rationals(limit):
    rationals = []
    a, b = 1, 1
    for _ in range(limit):
        rationals.append(f"{a}/{b}")
        k = a // b
        a, b = b, (2*k + 1)*b - a
    return rationals

some_rationals = enumerate_rationals(20)

# 3. Cardinality of power set for finite set
def power_set(s):
    ps = [[]]
    for elem in s:
        ps += [subset + [elem] for subset in ps]
    return ps

finite_set = ['a', 'b', 'c']
ps = power_set(finite_set)

with open('continuo_resultados.json', 'w', encoding='utf-8') as f:
    json.dump({
        'argumento_diagonal': {
            'muestras_reales': samples,
            'contraejemplo_diagonal': counterexample,
            'difiere_de_cada_muestra': all(diffs)
        },
        'racionales_enumerables_muestra': some_rationals,
        'cardinalidad_potencia_conjunto_finito': {
            'conjunto': finite_set,
            'partes': [sorted(p) for p in ps],
            'cantidad_partes': len(ps),
            'formula_2_n': 2 ** len(finite_set)
        },
        'nota': 'CH no es computablemente verificable; es independiente de ZFC.'
    }, f, ensure_ascii=False, indent=2)

print('Resultados guardados en continuo_resultados.json')
print('Contraejemplo diagonal:', counterexample)
print('Difiere de cada muestra:', all(diffs))
