# Answer Key — Statics Concept & Application Set (30 Problems)

Below are concise solutions for the early concept items and progressively more detailed, step‑by‑step answers for the later analysis problems. All math follows the formatting rules used in the problems (inline `$...$`, display blocks with `$$...$$`, aligned environments, upright units via `\mathrm{}`).

---

## Problem 1: Equilibrium at a Ring (2D)

**Equations** (angles measured from the ceiling/horizontal):

$$
\begin{aligned}
\sum F_x &: \; T_B\cos\alpha - T_A\cos 35^{\circ} = 0,\\
\sum F_y &: \; T_A\sin 35^{\circ} + T_B\sin\alpha - W = 0.
\end{aligned}
$$

**With** $\alpha=50^{\circ}$ and $W=300\,\mathrm{kg}\cdot 9.81\,\mathrm{m/s^2} = 2943.0\,\mathrm{N}$,

$$
\begin{aligned}
T_B &= T_A\,\frac{\cos 35^{\circ}}{\cos 50^{\circ}},\\
T_A\sin 35^{\circ} + T_A\,\frac{\cos 35^{\circ}}{\cos 50^{\circ}}\sin 50^{\circ} &= W.
\end{aligned}
$$

**Numerical result:** $T_A \approx 1899\,\mathrm{N}$ and $T_B \approx 2420\,\mathrm{N}$.

---

## Problem 2: Terminology — Support Types (MC)

**Answer:** Two reaction components $A_x, A_y$. A smooth pin in 2D provides two force reactions and no moment.

---

## Problem 3: Concurrent Forces (MC)

**Answer:** $\sum F_x=0$ **and** $\sum F_y=0$. For a particle (no size), moment equilibrium is automatically satisfied if the force sum is zero.

---

## Problem 4: Moment Sense (MC)

**Answer:** Negative moment. With CCW positive, a clockwise tendency is negative.

---

## Problem 5: Equivalent Force–Couple (Concept)

A force $\vec F$ acting at $A$ can be moved to any other point $B$ on a rigid body by adding a **free couple**

$$
\vec M_B = \vec M_A + \vec r_{BA} \times \vec F.
$$

If no initial couple exists at $A$, then at $B$ we carry the **same force $\vec F$** and add the couple $\vec r_{BA}\times\vec F$. The couple (moment) is a free vector and is **independent of point**.

---

## Problem 6: Simply Supported Beam — Loads

Let reactions be $A_y$ at the roller and $B_x,B_y$ at the pin. Write

$$
\begin{aligned}
\sum F_x &: \; B_x = 0,\\
\sum F_y &: \; A_y + B_y - P - Q = 0,\\
\sum M_A &: \; B_y L - P x_P - Q x_Q = 0
\end{aligned}
$$

with $x_P, x_Q$ measured from $A$. Solve symbolically for $B_y$ then $A_y = P+Q-B_y$.

---

## Problem 7: Centroid of Composite Plate (Setup)

Using **area algebra** (hole negative):

$$
\begin{aligned}
\bar x &= \frac{\sum A_i x_i}{\sum A_i}, \qquad
\bar y = \frac{\sum A_i y_i}{\sum A_i},
\end{aligned}
$$

where $i$ runs over the rectangle (positive) and the semicircular **hole** (negative). Use known centroids: rectangle at its center; semicircle at $\tfrac{4r}{3\pi}$ from its flat side.

---

## Problem 8: True/False — 3D Equilibrium

**Answer:** **True.** If $\sum\vec F=\vec 0$ and $\sum\vec M_O=\vec 0$ about one arbitrary point, the body is in static equilibrium (the moment sum will be zero about any other point as well).

---

## Problem 9: Zero-Force Members in a Truss (MC)

**Answer:** Both zero. At a joint with two non‑collinear members and no external load, equilibrium forces in both members must vanish.

---

## Problem 10: Method Choice (Short Answer)

Use **Method of Sections** when a few specific member forces are required. Cutting through up to three members and taking moments about a convenient point often yields a target force from a **single scalar equation**, avoiding a full joint‑by‑joint solve.

---

## Problem 11: Cable Angles & Tensions

Equal tensions require equal angles, so $\alpha = 35^{\circ}$. With $W=3.0\,\mathrm{kN}$,

$$
T = \frac{W}{2\sin 35^{\circ}} \approx 2.62\,\mathrm{kN}.
$$

---

## Problem 12: Beam with Two Loads

Let span be $L$. Load $P$ at $L/2$ and $Q$ at a point one‑quarter span from $B$ (i.e., at $x=3L/4$ from $A$).

$$
\begin{aligned}
\sum F_y &: \; A_y + B_y = P + Q,\\
\sum M_A &: \; B_y L - P\left(\tfrac{L}{2}\right) - Q\left(\tfrac{3L}{4}\right) = 0.
\end{aligned}
$$

Therefore

$$
\begin{aligned}
B_y &= \frac{P}{2} + \frac{3Q}{4},\\
A_y &= P+Q - B_y = \frac{P}{2} + \frac{Q}{4}.
\end{aligned}
$$

---

## Problem 13: Centroid — Numerical

Rectangle $b=700\,\mathrm{mm}$, $h=350\,\mathrm{mm}$; semicircular **void** radius $r=120\,\mathrm{mm}$ with flat side on the base at $y=0$ and centered at $x=b/2$.

Areas and $y$‑locations:
$$
\begin{aligned}
A_\text{rect} &= bh = 245000\,\mathrm{mm^2}, & y_\text{rect} &= \tfrac{h}{2} = 175.0\,\mathrm{mm},\\
A_\text{semi} &= \tfrac{1}{2}\pi r^2 = 22619.5\,\mathrm{mm^2}, & y_\text{semi} &= \tfrac{4r}{3\pi} = 50.93\,\mathrm{mm}.
\end{aligned}
$$

Net centroid:

$$
\begin{aligned}
\bar x &= \frac{b}{2} = 350.0\,\mathrm{mm},\\
\bar y &= \frac{A_\text{rect} y_\text{rect} - A_\text{semi} y_\text{semi}}{A_\text{rect} - A_\text{semi}} \approx 187.62\,\mathrm{mm}.
\end{aligned}
$$

---

## Problem 14: Planar Moment by Vector

Given $\vec r=\langle 0.60,0.25\rangle\,\mathrm{m}$ and $\vec F=\langle 300,-200\rangle\,\mathrm{N}$, the scalar moment about $O$ is

$$
\begin{aligned}
M_O &= \hat{k}\cdot(\vec r\times\vec F) = xF_y - yF_x \\
&= (0.60)(-200) - (0.25)(300) = -195\,\mathrm{N\cdot m}.
\end{aligned}
$$

Negative sign $\Rightarrow$ clockwise sense about $O$.

---

## Problem 15: Truss — Method of Joints (setup)

At the apex joint (two unknown member forces meeting the external $P$), write

$$
\begin{aligned}
\sum F_x&=0,\\
\sum F_y&=0,
\end{aligned}
$$

resolve member forces into components along each bar using the bar geometry. Solve symbolically to get the two connected member forces in terms of $P$ (tension positive by convention).

---

## Problem 16: Pipe Elbow — Moment about $A$

Let $\vec r_{AC}=\langle x_C-x_A,\; y_C-y_A,\; z_C-z_A\rangle$ and $\vec F=\langle 0,0,-F\rangle$ if vertical downward at $C$. Then

$$
\vec M_A = \vec r_{AC}\times\vec F =
\begin{vmatrix}
\hat i & \hat j & \hat k\\
x & y & z\\
0 & 0 & -F
\end{vmatrix}
= \langle -yF,\; xF,\; 0\rangle.
$$

Insert the actual coordinates from the sketch to compute components numerically.

---

## Problem 17: Forearm — Required Biceps Force

Moment about $O$ (upward biceps, downward weight):

$$
T_b r_b - W r_W = 0 \;\Rightarrow\; T_b = W\,\frac{r_W}{r_b}.
$$

With $W=5.0\,\mathrm{lb}$, $r_W=0.30\,\mathrm{m}$, $r_b=0.04\,\mathrm{m}$,

$$
T_b \approx 37.5\,\mathrm{lb}.
$$

(Any consistent length unit gives the same ratio.)

---

## Problem 18: Equilibrium Classification (MC)

**Answer:** $\sum F_x=\sum F_y=\sum M_O=0$ is sufficient for planar rigid‑body equilibrium.

---

## Problem 19: Distributed Load Equivalent

Uniform load over $L=8\,\mathrm{m}$ with $w=4\,\mathrm{kN/m}$ is replaced by a single force

$$
R = wL = 32\,\mathrm{kN},
$$

acting at the centroid of the uniform distribution — midspan, i.e., at $x=4.0\,\mathrm{m}$ from the left end.

---

## Problem 20: Check of Units

Centroid coordinates are ratios of **first moments of area** to area: $\bar y = (\int y\,\mathrm{d}A)/A$. First moment has units of area·length, so dividing by area leaves **length**.

---

## Problem 21: 3D Wrench Equilibrium

(a) With $\vec r_D=\langle 0.2,0.4,0\rangle\,\mathrm{m}$ and $\vec F=\langle 30,100,-50\rangle\,\mathrm{N}$,

$$
\begin{aligned}
\vec M_O &= \vec r_D \times \vec F = \langle -20,\; 10,\; 8 \rangle\,\mathrm{N\cdot m}.
\end{aligned}
$$

(b) The point on the line of action closest to $O$ is

$$
\vec r_0 = \frac{\vec F \times \vec M_O}{\lVert\vec F\rVert^2}
= \left\langle 0.0970,\; 0.0567,\; 0.1716 \right\rangle\,\mathrm{m}.
$$

Distance from $O$ to the line is $d=\lVert\vec r_0\rVert$.

---

## Problem 22: Truss — Method of Sections

Cut through members $AC$, $BC$, $AB$. Take moments about joint $A$ so that forces in $AB$ and $AC$ (both pass through $A$) drop out; solve directly for the force in $BC$ from **one** scalar equation. Then use $\sum F_x=0$, $\sum F_y=0$ on the cut‑freebody to find the remaining two member forces.

---

## Problem 23: Composite Area with Nonuniform Density

For surface mass density $\rho(y)=\rho_0(1+ky)$,

$$
\bar y_G = \frac{\iint y\,\rho(y)\,\mathrm{d}A}{\iint \rho(y)\,\mathrm{d}A},
$$

treating the hole as negative area. Since density increases with $y$ when $k>0$, the center of gravity lies **above** the geometric centroid (and vice versa when $k<0$).

---

## Problem 24: Beam with Mixed Loads

Let span be $L$. Replace the uniform load over the left half by $R_w = w(L/2)$ applied at $x=L/4$. A point load $P$ acts at $x=L/2$.

Reactions:

$$
\begin{aligned}
\sum F_y &: \; A_y + B_y = \tfrac{wL}{2} + P, \\
\sum M_A &: \; B_y L = \left(\tfrac{wL}{2}\right)\left(\tfrac{L}{4}\right) + P\left(\tfrac{L}{2}\right).
\end{aligned}
$$

Thus

$$
\begin{aligned}
B_y &= \tfrac{wL}{8} + \tfrac{P}{2},\\
A_y &= \tfrac{3wL}{8} + \tfrac{P}{2}.
\end{aligned}
$$

**Shear/Moment (qualitative):** shear starts at $V(0^+)=A_y$, decreases linearly over $[0,\,L/2]$ due to $w$, drops by $P$ at midspan, and remains constant to $x=L$. Bending moment is quadratic under the distributed load region and linear elsewhere; the peak occurs where $V=0$ in the left half.

---

## Problem 25: 3D Equilibrium — Direction Cosines

Let $\vec r_{AC}=\langle x_C-x_A,\,y_C-y_A,\,z_C-z_A\rangle$ and $\ell=\lVert\vec r_{AC}\rVert$. The direction cosines are

$$
\cos\alpha=\frac{x_C-x_A}{\ell},\quad
\cos\beta=\frac{y_C-y_A}{\ell},\quad
\cos\gamma=\frac{z_C-z_A}{\ell},
$$

and the tension components are $\vec T = T\langle \cos\alpha,\cos\beta,\cos\gamma\rangle$. Write ring equilibrium with the other two known forces to solve $T$.

---

## Problem 26: Forearm with Counterweight

Moment about $O$ (taking counterclockwise positive):

$$
T_b r_b + W_c(0.15) - W(0.30) = 0.
$$

For a given $W$, **minimize** $T_b$ by choosing $W_c$ so that external moment about $O$ is nearly zero:

$$
W_c = \frac{W(0.30)}{0.15} = 2W, \quad \text{giving } T_b \to 0^+.
$$

(Practical limits and muscle angle/geometry may require a nonzero $T_b$.)

---

## Problem 27: Moment via Varignon (Computation)

Moments about $O(0,0)$:

$$
\begin{aligned}
M_O &= x_1 F_{1y} - y_1 F_{1x} + x_2 F_{2y} - y_2 F_{2x} \\
&= (0.2)(0) - (0)(100) + (0)(-150) - (0.5)(0) = 0\,\mathrm{N\cdot m}.
\end{aligned}
$$

So the net moment is zero for this placement.

---

## Problem 28: Truss Determinacy (MC)

**Answer:** $m=2j-3$ (for simple planar trusses with three external reactions).

---

## Problem 29: Parallel-Axis Theorem (PSM)

For a rectangle about an axis parallel to its centroidal $x$‑axis and located at the **top edge** (distance $d=h/2$):

$$
\begin{aligned}
I_x^{\text{top}} &= I_x^{\text{centroid}} + A d^2 \\
&= \frac{b h^3}{12} + (b h)\left(\frac{h}{2}\right)^2 \\
&= \frac{b h^3}{3}.
\end{aligned}
$$

---

## Problem 30: 3D Couple Example

A pure couple is a **free vector**: its moment is the same about any point, independent of location.

One realizing pair: choose a force $\vec F=\langle 2,0,-6\rangle\,\mathrm{N}$ applied at one point and an equal/opposite force at a point separated by

$$
\vec d = \langle 1,2,0\rangle\,\mathrm{m}.
$$

Then

$$
\vec F \times \vec d = \langle 12,-6,4\rangle\,\mathrm{N\cdot m} = \vec M.
$$

This matches the required couple.
