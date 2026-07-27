# DOMUS HORIZON — Conjetura de los Primos Gemelos

## Enunciado

La **Conjetura de los Primos Gemelos** afirma:

> Existen infinitos pares de números primos que difieren exactamente en 2.

Ejemplos: $(3,5)$, $(5,7)$, $(11,13)$, $(17,19)$, $(29,31)$, $(101,103)$.

Formalmente, debe existir una infinidad de enteros $n$ tales que $n$ y $n+2$ sean ambos primos.

---

## Estado actual

- Se han encontrado enormes cantidades de primos gemelos de forma computacional, incluyendo algunos de millones de dígitos.
- **No existe demostración de que existan infinitos pares.**
- Avances recientes importantes:
  - **Yitang Zhang (2013):** existen infinitos pares de primos con distancia acotada por $70.000.000$.
  - **Polymath8 / Maynard / Tao:** la cota se redujo a **246** (y a **6** bajo conjeturas adicionales como Elliott–Halberstam).

---

## Verificación computacional con DOMUS HORIZON

Se ejecutó un motor de verificación propio (`verificar_primos_gemelos.py`) que:

1. Construye una criba de Eratóstenes hasta $N$.
2. Detecta todos los pares $(p, p+2)$ con ambos primos.
3. Calcula una aproximación parcial de la **constante de Brun**.
4. Compara el conteo observado con la estimación de **Hardy-Littlewood**.

### Resultados hasta $N = 100.000$

| Métrica | Valor |
|---|---|
| Límite verificado | $100.000$ |
| Total de pares gemelos encontrados | $1.224$ |
| Primeros 10 pares | $(3,5),(5,7),(11,13),(17,19),(29,31),(41,43),(59,61),(71,73),(101,103),(107,109)$ |
| Últimos 10 pares | $(98909,98911),(98927,98929),(99131,99133),(99137,99139),(99257,99259),(99347,99349),(99527,99529),(99707,99709),(99719,99721),(99989,99991)$ |
| Aproximación de Brun $\sum (1/p + 1/(p+2))$ | $1{,}67279958$ |
| Estimación Hardy-Littlewood para $\pi_2(100.000)$ | $1.258{,}3$ |
| Tiempo de cómputo | $0{,}01$ s |

**Observación:** el conteo observado ($1.224$) es cercano a la predicción heurística ($1.258{,}3$), lo que refuerza la plausibilidad de la conjetura.

---

## Propuesta de ataque DOMUS HORIZON

### 1. Función contadora de pares gemelos

Definimos:

$$\pi_2(x) = \#\{p \le x : p \text{ y } p+2 \text{ son primos}\}.$$

La conjetura equivale a:

$$\lim_{x \to \infty} \pi_2(x) = \infty.$$

### 2. Heurística de Hardy-Littlewood

La probabilidad de que un número cercano a $x$ sea primo es aproximadamente $1 / \ln x$. Sin embargo, los eventos "$p$ es primo" y "$p+2$ es primo" no son independientes: ambos deben evitar el divisor 2. Ajustando por esta correlación local, se obtiene la conjetura asintótica:

$$\pi_2(x) \sim 2 C_2 \int_2^x \frac{dt}{(\ln t)^2}$$

donde:

$$C_2 = \prod_{p > 2} \frac{p(p-2)}{(p-1)^2} \approx 0{,}6601$$

es la **constante de los primos gemelos**.

Para $x = 100.000$, la estimación da $\approx 1.258$ pares, muy cerca del $1.224$ observados.

### 3. Constante de Brun

Aunque se sospeche que hay infinitos primos gemelos, la suma de sus recíprocos converge (Teorema de Brun, 1919):

$$B = \sum_{(p,p+2) \text{ gemelos}} \left(\frac{1}{p} + \frac{1}{p+2}\right) \approx 1{,}90216058$$

Nuestra verificación parcial hasta $100.000$ acumula $1{,}67279958$, lo cual es consistente con la convergencia hacia el valor de Brun.

### 4. Estrategia DOMUS HORIZON para cerrar la prueba

1. **Criba de Selberg / criba superior:** acotar el conjunto de enteros $n$ para los cuales ni $n$ ni $n+2$ tienen factores pequeños.
2. **Nivel de distribución:** extender los resultados de Zhang-Maynard mostrando que el nivel de distribución de los primos es suficiente para garantizar infinitos pares a distancia fija.
3. **Argumento de densidad:** probar que la función densidad de pares gemelos no decae a cero más rápido que la predicción de Hardy-Littlewood, usando cotas de criba y sumas exponenciales.
4. **Verificación computacional complementaria:** extender la criba hasta $10^{12}$ o más para descartar regiones iniciales anómalas y alimentar el modelo heurístico.

---

## Obstáculos conocidos

- **Paridad del divisor 2:** la estructura de los primos impares fuerza a que los gemelos sean de la forma $(6k-1, 6k+1)$, pero no todo par de esa forma es primo.
- **Criba incompleta:** los métodos de criba actuales pueden acotar el conjunto excepcional, pero no demostrar infinitud directamente sin hipótesis adicionales.
- **Independencia asintótica:** la correlación entre $p$ y $p+2$ solo se conoce de forma heurística; probarla rigurosamente es equivalente a resolver la conjetura.

---

## Veredicto DOMUS HORIZON

- **Evidencia empírica:** muy fuerte. Los pares gemelos aparecen de manera persistente hasta los límites computados y la densidad sigue la predicción de Hardy-Littlewood.
- **Evidencia heurística:** fuerte. La constante $C_2$ y la convergencia de Brun son coherentes con infinitud.
- **Demostración general:** **pendiente**. Zhang, Maynard, Tao y Polymath8 redujeron la distancia entre infinitos pares de primos, pero no han llegado a distancia 2.

**Recomendación:** continuar con verificaciones a gran escala y explorar una reducción del método de criba combinado con análisis de densidad bajo el marco DOMUS HORIZON, aprovechando su capacidad de aislamiento y conteo estructurado.

---

## Archivos asociados

- `verificar_primos_gemelos.py` — script de verificación computacional.
- `primos_gemelos_resultados.json` — resultados numéricos hasta $100.000$.

---

*Documento generado bajo el marco DOMUS HORIZON para el proyecto de las cuatro conjeturas matemáticas.*
