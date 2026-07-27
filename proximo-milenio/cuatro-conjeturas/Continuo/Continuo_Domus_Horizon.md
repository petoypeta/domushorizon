# DOMUS HORIZON — Hipótesis del Continuo

## Enunciado

La **Hipótesis del Continuo** (CH), formulada por Georg Cantor a finales del siglo XIX, afirma:

> No existe ningún conjunto cuya cardinalidad esté estrictamente entre la de los números naturales ($\aleph_0$) y la de los números reales ($2^{\aleph_0}$).

En símbolos:

$$2^{\aleph_0} = \aleph_1.$$

Donde $\aleph_1$ es el siguiente cardinal infinito después de $\aleph_0$.

---

## Estado actual

- **Gödel (1940):** mostró que CH es **consistente** con ZFC (no se puede refutar).
- **Cohen (1963):** mostró que la negación de CH también es **consistente** con ZFC (no se puede demostrar).
- Conclusión: **CH es independiente de los axiomas estándar de la teoría de conjuntos (ZFC).** No se puede probar ni refutar a partir de ellos.

---

## Exploración computacional con DOMUS HORIZON

Aunque CH no es verificable por computadora, se incluyeron demostraciones constructivas ilustrativas:

### 1. Argumento diagonal de Cantor

Dada cualquier lista finita de "números reales" en $(0,1)$ representados por sus decimales, se construye un nuevo número que difiere de cada uno en al menos un dígito:

| Posición | Muestra | Dígito diagonal |
|---|---|---|
| 0 | 0.314159... | 3 |
| 1 | 0.271828... | 7 |
| 2 | 0.161803... | 1 |
| 3 | 0.141421... | 1 |
| 4 | 0.066987... | 6 |
| 5 | 0.057721... | 7 |

Eligiendo un dígito diferente en cada posición, DOMUS HORIZON generó el contraejemplo diagonal `482502`, que difiere de cada muestra en su posición correspondiente.

**Lectura:** la lista completa de números reales no puede ser enumerada; hay "más" reales que naturales.

### 2. Enumerabilidad de los racionales

Usando la enumeración de Calkin-Wilf, DOMUS HORIZON produjo los primeros racionales:

$$1/1,\; 1/2,\; 2/1,\; 1/3,\; 3/2,\; 2/3,\; 3/1,\; 1/4,\; 4/3,\; \dots$$

Esto demuestra que $\mathbb{Q}$ es **contable** (misma cardinalidad que $\mathbb{N}$), a diferencia de $\mathbb{R}$.

### 3. Cardinalidad de la potencia de un conjunto finito

Para $\{a,b,c\}$, el conjunto potencia tiene $2^3 = 8$ elementos:

$$\emptyset,\; \{a\},\; \{b\},\; \{c\},\; \{a,b\},\; \{a,c\},\; \{b,c\},\; \{a,b,c\}.$$

Esto ilustra el **Teorema de Cantor**: $|\mathcal{P}(A)| > |A|$ para todo conjunto $A$. En particular, $|\mathcal{P}(\mathbb{N})| = 2^{\aleph_0} > \aleph_0$.

---

## Propuesta de interpretación DOMUS HORIZON

### 1. CH como límite epistemológico

La independencia de CH revela que ZFC no determina completamente la estructura del universo de conjuntos. DOMUS HORIZON propone tratar CH como un **parámetro axiomático**:

- **CH = verdadera:** simplifica muchas construcciones en topología y análisis; no hay cardinales intermedios.
- **CH = falsa:** existen cardinales estrictamente entre $\aleph_0$ y $2^{\aleph_0}$; permite una estructura más rica del continuo.

### 2. Forcing y modelos internos

La técnica de **forcing** de Paul Cohen permite extender un modelo de ZFC agregando nuevos subconjuntos de $\mathbb{N}$. Esto muestra que:

- Es posible añadir $\aleph_2$ subconjuntos de $\mathbb{N}$ sin contradecir ZFC, haciendo falsa CH.
- También es posible construir un modelo (L de Gödel) donde CH valga.

### 3. Consecuencias prácticas para matemáticas ordinarias

La mayoría de las ramas de las matemáticas (análisis, álgebra, geometría) no dependen del valor de CH. Sin embargo, CH afecta:

- La existencia de ciertos espacios topológicos.
- Medidas sobre conjuntos de Borel y proyectivos.
- Propiedades de conjuntos de números reales de cardinalidad $\aleph_1$.

### 4. Estrategia DOMUS HORIZON para avanzar

1. **Explorar axiomas adicionales:** grandes cardinales, axioma de determinación (AD), axioma de Martin, etc., pueden decidir CH en extensiones de ZFC.
2. **Modelar cardinales intermedios:** construir explícitamente (en modelos adecuados) conjuntos con cardinalidad estrictamente entre $\aleph_0$ y $2^{\aleph_0}$.
3. **Análisis de complejidad:** estudiar qué proposiciones analíticas dependen de CH y cuáles son absolutas.
4. **Marco finito-computacional:** usar aproximaciones finitas (como la enumeración diagonal mostrada) para entender qué parte del continuo es constructible y qué parte queda fuera de cualquier enumeración efectiva.

---

## Veredicto DOMUS HORIZON

- **Respuesta formal:** CH es **independiente de ZFC**. No es posible demostrarla ni refutarla dentro de los axiomas estándar.
- **Estatus:** no se trata de una conjetura sin resolver en el sentido tradicional, sino de una **proposición indeterminada** que requiere axiomas adicionales para ser decidida.
- **Recomendación:** adoptar CH o su negación según el contexto matemático, explicitando el axioma elegido. Para propósitos constructivistas y computacionales, el marco DOMUS HORIZON favorece enfoques que no asuman CH sin necesidad.

---

## Archivos asociados

- `explorar_continuo.py` — demostraciones ilustrativas (diagonal, enumeración de racionales, cardinalidad de potencia).
- `continuo_resultados.json` — resultados de las exploraciones.

---

*Documento generado bajo el marco DOMUS HORIZON para el proyecto de las cuatro conjeturas matemáticas.*
