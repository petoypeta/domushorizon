# DOMUS HORIZON — Conjetura de Goldbach

## Enunciado

La **Conjetura de Goldbach** (Christian Goldbach, 1742) afirma:

> Todo número par mayor que 2 puede escribirse como la suma de dos números primos.
>
> $$n = p + q, \quad p, q \text{ primos}, \quad n \text{ par}, n > 2.$$

Ejemplos: $4 = 2 + 2$, $6 = 3 + 3$, $8 = 3 + 5$, $10 = 3 + 7 = 5 + 5$.

---

## Estado actual

- Ha sido verificada por computadora hasta valores astronómicos (más allá de $10^{18}$).
- **No existe una demostración matemática general** válida hasta la fecha.
- Es uno de los problemas abiertos más antiguos y accesibles de la teoría de números.

---

## Verificación computacional con DOMUS HORIZON

Se ejecutó un motor de verificación propio (`verificar_goldbach.py`) que:

1. Construye una criba de Eratóstenes hasta $N$.
2. Cuenta, para cada par $n \le N$, de cuántas maneras puede escribirse como $p + q$.
3. Detecta contraejemplos (pares sin representación).

### Resultados hasta $N = 100.000$

| Métrica | Valor |
|---|---|
| Límite verificado | $100.000$ |
| Total de primos encontrados | $9.592$ |
| Total de pares verificados | $49.999$ |
| Contraejemplos encontrados | **0** |
| Representaciones mínimas | $1$ (para $n = 4$) |
| Representaciones máximas | $2.168$ (para $n = 99.330$) |
| Tiempo de cómputo | $2{,}8$ s |

**Conclusión empírica:** dentro del rango verificado, la conjetura se sostiene sin excepciones.

---

## Propuesta de ataque DOMUS HORIZON

### 1. Reformulación combinatoria

Sea $\mathbb{P}$ el conjunto de primos y sea $r_2(n)$ la cantidad de pares ordenados $(p, q) \in \mathbb{P}^2$ tales que $p + q = n$. Goldbach equivale a:

$$r_2(n) > 0 \quad \text{para todo } n \text{ par}, n > 2.$$

### 2. Función característica y esperanza

Definamos la función indicatriz de primos:

$$\chi_{\mathbb{P}}(x) = \begin{cases} 1 & \text{si } x \text{ es primo} \\ 0 & \text{en otro caso} \end{cases}$$

Entonces:

$$r_2(n) = \sum_{p \le n/2} \chi_{\mathbb{P}}(p) \cdot \chi_{\mathbb{P}}(n-p).$$

Aplicando el **Teorema de los Números Primos** ($\pi(x) \sim x / \ln x$), la probabilidad heurística de que un entero cercano a $x$ sea primo es aproximadamente $1 / \ln x$.

### 3. Argumento heurístico de Hardy-Littlewood

Para $n$ par y grande, el número esperado de representaciones es:

$$r_2(n) \approx 2 \cdot C_2 \cdot \frac{n}{(\ln n)^2} \cdot \prod_{p > 2, p \mid n} \frac{p-1}{p-2}$$

donde $C_2 \approx 0{,}6601$ es la constante de los primos gemelos (twin-prime constant).

Dado que este valor **crece sin límite** cuando $n \to \infty$ (salvo factores multiplicativos acotados), la ausencia de contraejemplos grandes es consistente con la conjetura.

### 4. Estrategia DOMUS HORIZON para cerrar la prueba

El marco DOMUS HORIZON propone atacar Goldbach mediante una **reducción de densidad**:

1. **Acotar conjuntos excepcionales:** probar que el conjunto de pares "sin representación" es de densidad cero usando cribas y métodos de criba superior.
2. **Aislar la estructura multiplicativa:** separar la contribución de primos pequeños vs. primos grandes, usando la función de Möbius y desigualdades de tipo Brun-Titchmarsh.
3. **Aplicar el método del círculo de Hardy-Littlewood:** descomponer $r_2(n)$ en una parte principal (sumas exponenciales mayoritarias) y una parte residual (sumas exponenciales menores). La parte principal domina para $n$ suficientemente grande.
4. **Verificación finita:** completar el ataque con computación explícita hasta un umbral $N_0$ fijo, después del cual el método analítico garantiza el resultado.

---

## Obstáculos conocidos

- **Métodos de criba actuales** permiten probar resultados del tipo "todo par suficientemente grande es suma de a lo sumo $K$ primos", pero no $K = 2$.
- **Chen (1973)** probó que todo par suficientemente grande es suma de un primo y un producto de a lo sumo dos primos ($P_2$), lo que refuerza la plausibilidad, pero no cierra Goldbach.
- La dificultad radica en controlar la **convolución de la función prima** con precisión suficiente para descartar el caso residual.

---

## Veredicto DOMUS HORIZON

- **Evidencia empírica:** muy fuerte (sin contraejemplos hasta $100.000$ y verificado por otros hasta más de $10^{18}$).
- **Evidencia heurística:** muy fuerte (argumento de Hardy-Littlewood predice infinitas representaciones crecientes).
- **Demostración general:** **pendiente**. La propuesta DOMUS HORIZON ofrece una ruta metodológica pero no una prueba completa en este punto.

**Recomendación:** continuar con la verificación computacional a mayor escala y desarrollar cotas de criba para el conjunto excepcional, mientras se explora una reducción analítica novedosa compatible con el marco cuaternario/dodecimal de DOMUS HORIZON 3.

---

## Archivos asociados

- `verificar_goldbach.py` — script de verificación computacional.
- `goldbach_resultados.json` — resultados numéricos hasta $100.000$.

---

*Documento generado bajo el marco DOMUS HORIZON para el proyecto de las cuatro conjeturas matemáticas.*
