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


*   **Belief Space** introduction to planning and advantages
    -   Intro
    -   Advantages via Examples
    -   RRT
*   **Distance Functions** for sampling planners
    -   L1
    -   KL Divergence
    -   Hausdorff
    -   Earth Movers Distance (EMD)
*   **Analysis** 
    -   Results
    -   Back to basics (Nondeterministic formulation)
    -   Downsides


Introduction to Belief Space Planning
=====================================

> * A belief is a pdf over the possible (not necessarily reachable) physical states 
> * Goal is to generate a strategy (sequence of actions, or mapping from beliefs
to best actions) that takes agent from start states (set of beliefs) to goal
states (set of beliefs)
> * "Size is doubly exponential in the number of state space dimensions"
>       * If we restrict the space of pdfs to those with finite parameterizations
>       * Otherwise is an infinite cardinality space of possible pdfs

Belief Space Advantages through Examples
========================================

* If you plan in the space of beliefs, you can control the variance of your belief
    - leads to information gathering as a strategy in partially observable spaces
    - can set bounds on collision probability as input to planner

Belief Space Example: Information Gathering
===========================================

![Given a region with available localization, the robot can plan to reduce variance by entering the measurement area [^1]](./figures/information-gathering.png)

[^1]: [@bry2011rapidly], Bry & Roy ICRA 2011

Open-loop planning in belief space
===================

Paper terminology: **NOMDP** (Non-Observable Markov Decision Process)

**Non-Observable:** no sensor readings (open loop plan)

**Markov Decision Process:** next belief depends only on current belief and action
(this update function is given)

. . .

How to tame high dimensionality of belief space?

. . .

Random sampling!


RRT in Belief Space
===================


```python
G = {V -> {b_0}, E -> 0}

for N iterations do
    # choose belief in tree closest to random belief
    b_selected = SelectNode(B, V, d_n)
```
. . .
```python
    # apply a random control for a random time
    b_new = Random_Prop(b_select, U, Tmax)
```
. . .
```python
    # optimize wrt cost function
    if NodeLocallyBest(b_new, S, d_s):
        V <- V U {b_new}
        E <- E U {b_select -> b_new}
        Prune_Tree(b_new, V, E, d_s)
```

Distance Functions for Sampling Planners
============================


* Need distance functions that work in belief space
	- Must take into account the pdf of the belief as well as the physical state

L1 Distance
===========


\centering
$$D_{L1}(b, b') = \int_{x \in \mathbb{X}} | b(x) - b'(x) | dx$$


KL-Divergence
=============


* Information theoretic distance between pdfs

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

$$D_{w}(b, b') = \inf_{f} \bigg\{   \bigg\}$$


Spaces in Belief Space Planning
===============================

* P Space: Same as in deterministic case
* Y Space: Same as Probabilistic case
* I Space: P$\times \mathbb{P}$ ($\mathbb{P}$ is the space of all distributions)


Belief Space Disadvantages
=============

* Stay in Gaussian land for the most part
  - Few good ways to model pdf's
  - Everyone uses Gaussian distribution for beliefs
* Dimensionality is huge
* Steering function not studied between beliefs
* No longer have space filling properties
* Reachability expensive to consider in planning



References
==========

\tiny

