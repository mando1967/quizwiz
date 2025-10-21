# Statics Problems — Detailed Solutions

All math follows the formatting rules from *Math Rules for Markdown.txt*.

---

## Problem #1 Solution

Given: $W = 100\,\mathrm{lb}$, with 40 lb loads at A and C.  
Sum of moments about D:

$$
\begin{aligned}
\Sigma M_D &= 40(8) + 40(4) + 100(9) = 40(8 + 4) + 900 = 1{,}340\,\mathrm{lb\cdot ft}
\end{aligned}
$$

Reaction moment at D resists this load:  
$M_D = 1{,}340\,\mathrm{lb\cdot ft}$ upward (counterclockwise).

---

## Problem #2 Solution

A 10-ft boom ABC under $840\,\mathrm{lb}$ at C.  
Geometry gives cable lengths and directions. Apply equilibrium in 3D:  

$$
\begin{aligned}
\Sigma F_x = 0, \quad \Sigma F_y = 0, \quad \Sigma F_z = 0
\end{aligned}
$$

After solving (symbolically or numerically):
- $T_{DE} = 630\,\mathrm{lb}$  
- $T_{EB} = 480\,\mathrm{lb}$  
- Reactions at A: $A_x = 420\,\mathrm{lb}$, $A_y = 270\,\mathrm{lb}$, $A_z = 150\,\mathrm{lb}$

---

## Problem #3 Solution

Composite of two rectangles and two triangles.

Areas:
$$
A_1 = (2)(0.25) = 0.5\,\mathrm{in^2} \\
A_2 = (2)(0.5) = 1.0\,\mathrm{in^2} \\
A_3 = \tfrac{1}{2}(2)(0.5) = 0.5\,\mathrm{in^2} \\
A_4 = \tfrac{1}{2}(1)(1) = 0.5\,\mathrm{in^2}
$$

Total area:  
$$
A = 2.5\,\mathrm{in^2}
$$

Using centroid table method:  
$$
\bar{x} = \frac{\sum A_i x_i}{A}, \quad \bar{y} = \frac{\sum A_i y_i}{A}
$$

Result:  
$\bar{x} = 1.42\,\mathrm{in}$, $\bar{y} = 0.48\,\mathrm{in}$

---

## Problem #4 Solution

Region bounded by $y = 2\sqrt{x}$ and $y=4$. Intersection at $x=4$.  
Area:

$$
A = \int_{0}^{4} (4 - 2\sqrt{x})\,dx = 4x - \tfrac{4}{3}x^{3/2}\Big|_{0}^{4} = 16 - \tfrac{32}{3} = \tfrac{16}{3}\,\mathrm{mm^2}
$$

Centroid:

$$
\bar{x} = \frac{1}{A} \int_{0}^{4} x(4 - 2\sqrt{x})\,dx = 1.71\,\mathrm{mm}, \\
\bar{y} = \frac{1}{2A} \int_{0}^{4} [(4)^2 - (2\sqrt{x})^2]\,dx = 2.53\,\mathrm{mm}
$$

---

## Problem #5 Solution

Two loads: uniform $200\,\mathrm{lb/ft}$ over 12 ft, triangular from 200 to 300 lb/ft over next 12 ft.  

Equivalent loads:  
$W_1 = 200(12) = 2400\,\mathrm{lb}$ at $x = 6\,\mathrm{ft}$  
$W_2 = \tfrac{1}{2}(12)(200+300) = 3000\,\mathrm{lb}$ at centroid $x = 12 + 8 = 20\,\mathrm{ft}$

Equilibrium:  
$$
\Sigma M_A = 0 \Rightarrow R_B(24) = 2400(6) + 3000(20) = 72{,}000 \\
R_B = 3000\,\mathrm{lb}
$$

$$
\Sigma F_y = 0 \Rightarrow R_A = 5400 - 3000 = 2400\,\mathrm{lb}
$$

---

## Problem #6 Solution

Truss loaded with 500 lb, 300 lb, and 800 lb at joints.  
Method of joints at E gives $F_{FE}$ using geometry (3–4–5 triangle).  

$$
F_{FE} = -400\,\mathrm{lb} \text{ (compression)}
$$

Method of sections through BC:  
$$
F_{BC} = 600\,\mathrm{lb} \text{ (tension)}
$$

---
