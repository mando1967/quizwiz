# Statics Concept & Application Set (30 Problems)

This Markdown follows your **Master Math Formatting Rules** so equations render correctly in VSCode/KaTeX (inline `$...$`, display `$$...$$` with blank lines, aligned environments, upright units via `\mathrm{}`)【10†source】.

## Problem 1: Equilibrium at a Ring (2D)

![Problem 1](statics_set/problem_01.png)
A 300 kg lantern is supported by two cables meeting at a ring $C$. The left cable makes $35^\circ$ with the ceiling; the right cable makes angle $\alpha$. Neglect cable weight.

(a) Write the scalar equilibrium equations at the ring.
(b) If $\alpha=50^\circ$, compute tensions $T_A$ and $T_B$ (take $g=9.81\,\mathrm{m/s^2}$).

---

## Problem 2: Terminology — Support Types (MC)

Identify the correct reaction set for a smooth pin support in 2D.

(a) Two reaction components $A_x, A_y$
(b) One unknown vertical reaction only
(c) A single moment only
(d) No reactions; it is a roller

---

## Problem 3: Concurrent Forces (MC)

Which condition must hold for a particle in planar equilibrium?

(a) $\sum F_x=0$ **and** $\sum F_y=0$
(b) $\sum M_O=0$ only
(c) $\sum F=0$ and $\sum M_O=0$ for any $O$
(d) $\sum F_x=\sum F_y$

---

## Problem 4: Moment Sense (MC)

With positive counterclockwise moments, a force producing clockwise rotation about point $O$ contributes:

(a) Negative moment
(b) Positive moment
(c) Zero moment
(d) Depends only on $O$'s coordinates

---

## Problem 5: Equivalent Force–Couple (Concept)

State how a **force–couple system** can be moved to a new point in a rigid body in planar statics. Provide the transformation formula for the free vector couple.

---

## Problem 6: Simply Supported Beam — Loads

![Problem 6](statics_set/problem_06.png)
The beam $AB$ carries the shown point load(s). Write reactions at $A$ (roller) and $B$ (pin) symbolically in terms of $P$ and $Q$ by applying $\sum F_x, \sum F_y, \sum M_A=0$. Clearly state sign conventions.

---

## Problem 7: Centroid of Composite Plate (Setup)

![Problem 7](statics_set/problem_11.png)
The figure shows a rectangular plate with a semicircular **hole**. Using the composite-areas method, write expressions for $\bar x$ and $\bar y$ using area algebra (additive for solids, negative for holes). Do not compute numerically.

---

## Problem 8: True/False — 3D Equilibrium

True or False: If a 3D rigid body satisfies $\sum \vec F=\vec 0$ and $\sum \vec M_O=\vec 0$ about **one** arbitrary point $O$, then it is in static equilibrium.

---

## Problem 9: Zero-Force Members in a Truss (MC)

At a joint with two non-collinear members and **no external load**, the member forces are:

(a) Both zero
(b) One zero, one non-zero
(c) Equal and opposite
(d) Cannot be determined

---

## Problem 10: Method Choice (Short Answer)

Explain when the **Method of Sections** is preferable to the **Method of Joints** for solving truss member forces.

---

## Problem 11: Cable Angles & Tensions

![Problem 11](statics_set/problem_11.png)
For the two-cable support, find $\alpha$ such that $T_A=T_B$. Then find the common tension for a $W=3.0\,\mathrm{kN}$ load.

---

## Problem 12: Beam with Two Loads

![Problem 12](statics_set/problem_08.png)
For the beam, $P=6.0\,\mathrm{kN}$ at midspan and $Q=3.0\,\mathrm{kN}$ at one-quarter span from $B$. Determine reactions at $A$ and $B$.

---

## Problem 13: Centroid — Numerical

![Problem 13](statics_set/problem_13.png)
Rectangle width $b=700\,\mathrm{mm}$, height $h=350\,\mathrm{mm}$. Semicircular **void** radius $r=120\,\mathrm{mm}$ centered on the $x$-axis as shown. Compute $(\bar x,\bar y)$ from the corner at $(0,0)$.

---

## Problem 14: Planar Moment by Vector

Force $\vec F=\langle 300, -200\rangle\,\mathrm{N}$ acts at point with position $\vec r=\langle 0.60, 0.25\rangle\,\mathrm{m}$ from $O$. Compute scalar moment $M_O$ using 
$$
\begin{aligned}
M_O &= \hat{k}\cdot (\vec r \times \vec F).
\end{aligned}
$$
 Give the sign and units.

---

## Problem 15: Truss — Method of Joints (setup)

![Problem 15](statics_set/problem_16.png)
Using the joint at the apex first, write the two equilibrium equations and solve for the two connected member forces **symbolically** in terms of $P$.

---

## Problem 16: Pipe Elbow — Moment about A

![Problem 16](statics_set/problem_21.png)
A vertical force $F=85\,\mathrm{N}$ acts at the free end $C$ of the bent pipe. Using the shown axes, compute the **moment vector** $\vec M_A=\vec r_{AC}\times\vec F$.

---

## Problem 17: Forearm — Required Biceps Force

![Problem 17](statics_set/problem_26.png)
The forearm holds a weight $W=5.0\,\mathrm{lb}$ in the hand. Taking distances $r_W=0.30\,\mathrm{m}$ from elbow $O$ to the weight line of action and $r_b=0.04\,\mathrm{m}$ for the biceps insertion, find $T_b$ for static equilibrium (assume all forces vertical).

---

## Problem 18: Equilibrium Classification (MC)

Which of the following sets is **sufficient** to ensure **planar rigid-body** equilibrium?

(a) $\sum F_x=\sum F_y=\sum M_O=0$
(b) $\sum F=0$ only
(c) $\sum M_A=\sum M_B=0$ for two distinct points
(d) $\sum F_x=\sum F_y=0$ only

---

## Problem 19: Distributed Load Equivalent

An $8\,\mathrm{m}$ beam carries a uniform load $w=4\,\mathrm{kN/m}$. Replace it by a single resultant force: give its **magnitude** and **location** from the left end.

---

## Problem 20: Check of Units (Short)

Why must the centroid coordinates carry **length units** even though they are ratios of area moments to area? Provide a one-sentence justification.

---

## Problem 21: 3D Wrench Equilibrium

![Problem 21](statics_set/problem_23.png)
A force $\vec F=\langle 30,100,-50\rangle\,\mathrm{N}$ acts at point $D(0.2,0.4,0.0)\,\mathrm{m}$ on the bent pipe. (a) Compute $\vec M_O$ about the origin. (b) Find a point on the line of action closest to $O$ (use the wrench reduction).

---

## Problem 22: Truss — Method of Sections

![Problem 22](statics_set/problem_19.png)
Cut the truss to expose members $AC, BC, AB$. With a section through these three members and using $\sum M$ about a convenient joint, solve for a target member force directly from one scalar equation.

---

## Problem 23: Composite Area with Nonuniform Density

![Problem 23](statics_set/problem_14.png)
For the plate with circular hole, suppose an area density varying linearly in $y$: $\rho(y)=\rho_0(1+ky)$. Describe how the **center of gravity** shifts relative to the geometric centroid and provide the integral for $\bar y_G$.

---

## Problem 24: Beam with Mixed Loads

![Problem 24](statics_set/problem_07.png)
A beam has a uniform load $w$ over the left half and a point load $P$ at midspan. (a) Determine reactions. (b) Sketch the **shear** and **moment** diagrams qualitatively, showing key values.

---

## Problem 25: 3D Equilibrium — Direction Cosines

![Problem 25](statics_set/problem_25.png)
A cable from $A$ to $C$ carries tension $T$. Using the coordinates shown, write the direction cosines and the components of the tension vector. Then write the 3 equilibrium equations for a ring at $A$ with two other known forces.

---

## Problem 26: Forearm with Counterweight

![Problem 26](statics_set/problem_27.png)
Modify the arm so a **counterweight** $W_c$ is strapped at mid-forearm (distance $0.15\,\mathrm{m}$ from $O$). (a) Write the scalar moment about $O$. (b) Solve for $T_b$ that minimizes $T_b$ by choosing $W_c$ (treat $W$ fixed).

---

## Problem 27: Moment via Varignon (Computation)

Two non-parallel coplanar forces act on a plate: $\vec F_1=\langle 100,0\rangle\,\mathrm{N}$ at $(0.2,0)$ and $\vec F_2=\langle 0,-150\rangle\,\mathrm{N}$ at $(0.0,0.5)$. Using **Varignon’s theorem**, compute $M_O$ about $O$ by summing moments of components.

---

## Problem 28: Truss Determinacy (MC)

In a statically determinate planar truss with $m$ members, $j$ joints, and $r$ reaction components, which relation holds?

(a) $m=2j-3$ for simple trusses with $r=3$
(b) $m+j=r$
(c) $m=3j-6$
(d) $m=2j$

---

## Problem 29: Parallel-Axis Theorem (PSM)

State the **parallel-axis theorem** for the second moment of area and apply it to find $I_x$ of a rectangle of width $b$ and height $h$ about an axis through its **top edge**, parallel to the base.

---

## Problem 30: 3D Couple Example

A pure couple $\vec M=\langle 12,-6,4\rangle\,\mathrm{{N\cdot m}}$ acts on a rigid body. (a) Explain why its moment is the same about any point. (b) Provide one pair of equal/opposite forces separated by a vector $\vec d$ that realize this couple.

---
