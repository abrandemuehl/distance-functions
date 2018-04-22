---
title: The Importance of a Suitable Distance Function in Belief Space Planning
author: Alli Nilles, Adrian Brandemuehl
date: \today
csl: ./ieee.csl
bibliography: ./slides.bib
date: April 28, 2018
header-includes:
    -   \usetheme[block=fill]{metropolis}
    -   \usepackage{ifthen}
    -   \usepackage{tikz}
    -   \usetikzlibrary{arrows}
    -   \usepackage[font=small]{subcaption}
---



Outline
=======


*   **Belief Space**
    -   Modelling choices
    -   Planning in belief space: RRT & POMDP solvers
*   **Distance Functions** in belief space 
    -   L1
    -   KL Divergence
    -   Hausdorff
    -   Earth Movers Distance (EMD)
*   **Analysis** 
    -   Results
    -   Comparison with I-space representation
    -   Discussion of advantages & disadvantages


Introduction to Belief Space Planning
=====================================

> * A *belief* is a probability distribution over the state space
> * *Belief space* is a space of all such beliefs
> * How big is the belief space?

Belief Space Planning 
=====================

**Plan:** a mapping from beliefs to best actions that
takes agent from start states (set of beliefs) to goal states (set of
beliefs)
    
If you plan in the space of beliefs, you can reduce the variance of your belief
by:

- choosing actions which decrease uncertainty
- going to areas where sensors have high expected information gain

Belief Space Example: Information Gathering
===========================================

\centering

![](bel1.png){width=6cm}\

![](bel2.png){width=6cm}\

[^3]

[^3]: Computational Robotics group (Ron Alterovitz), UNC Chapel Hill


Common Assumptions / Modeling Choices
=====================================

-   High dimensionality $\to$ sampling
-   Need efficient update of state estimation $p(x|u,y)$
    - Most choose Gaussian distribution for beliefs; can use Kalman filter for
        belief updates

- Inputs to planner:
    -  dynamics model (stochastic noise from known distribution)
    -  sensor model (stochastic noise from known distribution)
    -  bounds on collision probability
    -  confidence in goal state



Planning in belief space
===================


**NOMDP** (Non-Observable Markov Decision Process)

**POMDP** (Partially-Observable Markov Decision Process)

How to tame high dimensionality of belief space?

Random sampling!


RRT in Belief Space
===================


```python
G = {V -> {b_0}, E -> 0}

for N iterations do
    # choose belief in tree closest to random belief
    b_random = SampleBelief(B)
    b_selected = SelectNode(B, V, b_random, d_n)
```
. . .
```python
    # apply a random control for a random time
    b_new = Random_Prop(b_select, U, Tmax)
```
. . .
```python
    # optimize wrt cost function
    Prune_Tree(b_new, V, E, d_s)
```

POMDP Formulation
=================


-   include sensor readings
-   use off-the-shelf POMDP solver (Monte Carlo Value Iteration) and modify to
    use different distance functions
-   use distance function to discard samples if they are too close to existing
    nodes

Distance Functions for Sampling Planners
============================

\centering

What makes a good distance function in belief space?

. . .

1. How similar are the shapes of the belief distributions?
2. How far apart are the beliefs in the underlying state space?


L1 Distance
===========


\centering
$$D_{L1}(b, b') = \int_{x \in \mathbb{X}} | b(x) - b'(x) | dx$$


KL-Divergence
=============


\centering
$$D_{KL}(b, b') = \int_{x \in \mathbb{X}} b(x)(\ln b(x) - \ln b'(x)) dx$$



Hausdorff Distance
==================


\centering

$$D_{H}(b, b') = \max\Big\{d_{H}(b,b'), d_{H}(b', b)\Big\}$$
$$d_{H}(b, b') = \max_{x \in support(b)}\bigg\{ \min_{x' \in support(b')} \{ d_{\mathbb{X}}(x, x') \}\bigg\}$$

* $d_{\mathbb{X}}$ is the state space distance
* Does not take into account the distribution of states


Earth Mover's Distance (EMD)
============================

\centering


\begin{align}
  & D_{w}(b, b') = \inf_{f} \bigg\{ \int_{x \in \mathbb{X}} \int_{x \in \mathbb{X}} 
    d_{\mathbb{X}} (x, x') f(x,x')\partial x \partial x'  \bigg |  \nonumber \\
  & b = \int_{x'} f(x,x') \partial x', b'(x') = \int_{x}f(x,x')\partial x\bigg\} \nonumber
\end{align}


Can also be written as:
$$ EMD(b, b') = \inf_{f} \mathbb{E} [ d_{\mathbb{X}}(x, x') ] $$

where $f$ is space of all joint distributions with marginals $b$ and $b'$.

Finding $f$ is a linear programming problem - more expensive than other distance
functions.

Distance Function Demo
======================

\centering

![](distances.pdf)\



Results
=======

\centering

![](belief-008.png){width=6cm}\ ![](belief-009.png){width=6cm}\


![](belief-010.png){width=6cm}\ ![](belief-011.png){width=6cm}\


Results
=======


![](belief-012.png){width=6cm}\ ![](belief-013.png){width=6cm}\


![](belief-014.png){width=6cm}\ ![](belief-015.png){width=6cm}\



Connections to Class Topics
===========================




Spaces in Belief Space Planning
===============================

* P Space: metric representation of physical world
* Y Space: set of all possible sensor readings
* I Space: $\mathbb{P}$ (the space of all distributions over P)


Comparison with Nondeterministic Planning
===================================

I Space: $Pow(P)$


Is belief space planning with uniform distributions equivalent to nondet I-space
planning?


Updating Beliefs
================

Need to perform Bayes' update efficiently:

\begin{align*}
p(s_t | u_{1:t}, y_{1:t}) &= \frac{1}{Z} p(y_t | s_t) \int_S p(s_t | u_t,
s_{t-1}) p(s_{t-1}) ds_{t-1} \\
X_t (\eta_t) &= h^{-1}(y_t) \cap X_{t}(\eta_{t-1}, u_{t-1}) 
\end{align*}


Belief Space - Hard Modeling Choices
=============

* In certain robotic tasks (eg: grasping), Gaussians are not necessarily a natural
  representation, and can lead to "arbitrarily poor belief state estimates"[^2]
* Hard to find steering functions: given two beliefs, what control inputs go
  from one to the other?
    - *Sparse Methods for Efficient Asymptotically Optimal Kinodynamic
      Planning*, Li, Littlefield, Bekris WAFR 2014
* Belief space planning often assumes collisions are undesirable (how to model gaussian belief while
  in contact?)

[^2]: Platt, Kaelbling, Lozano-Perez, Tedrake ICRA 2012 [@platt2012non]


Discussion Questions
====================

> -  Is there one best distance function for every situation?
> -  How important is it to have real-time computation?
> -  When should we worry about discretization errors and approximations?
> -  When to use particle-based representations?
> -  When to use nondeterministic representation vs probabilistic representation?
> -  How could we represent compliant actions (wall collisions, grasping, etc)

References
==========

\tiny

