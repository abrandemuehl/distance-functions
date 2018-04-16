---
title: The Importance of a Suitable Distance Function in Belief Space Planning
author: Alli Nilles, Adrian Brandemuehl
date: \today
csl: ./ieee.csl
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

* State -> Belief
* A belief is a pdf over the possible (not necessarily reachable) physical states 
* Beliefs can be arbitrary pdf's/pmf's
* Size is doubly exponential in the number of state space dimensions

Belief Space Advantages through Examples
========================================

* If you plan in the space of beliefs, you can control the variance of your belief
  - Information gathering, bounded collision probability

Belief Space Example: Information Gathering
===========================================

![Given a region with available localization, the robot can plan to reduce variance by entering the measurement area [^1]](./figures/information-gathering.png)

[^1]: [@NickRoy], Bry & Roy ICRA 2011

RRT in Belief Space
===================




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

