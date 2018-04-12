---
geometry: margin=2cm
title: Mitra Research Group Meeting
author: Alli Nilles 
date: \today
bibliography: /home/alli/common/refs.bib
csl: ./ieee.csl
date: October 9, 2017
header-includes:
    -   \usetheme[block=fill]{metropolis}
    -   \usepackage{ifthen}
    -   \usepackage{jeffe}
    -   \usepackage{tikz}
    -   \usetikzlibrary{arrows}
    -   \usepackage[font=small]{subcaption}
---



Outline
=======


> -   **Bouncing robots:** discovering (and proving) dynamical properties of simple robot motion models
>     -   find minimal control and hardware that gives desired properties: periodic motion or
>         other attractors, coverage
>     -   SpaceEx project, possible future directions         
> -   **Improv:** high-level language for control of mobile robots
>     -   small domain-specific language, compiles to ROS
>     -   Future work: type-level checks and/or explicit model checking (with
>         DryVR?)?
> -   **Aggregate robot systems:** dynamics of local interactions toward minimal control
> -   **Automatic robot design** and automation of Robot Design Game


General Approach to Robot Decisionmaking
================================

> - focus on information spaces: space of all histories of sensor readings and actions
    taken
> - can reduce to different space (ex: only keep track of one bit: robot on wall,
    or not on wall)
> - can encode dynamical information explicity (equations) or implicitly (if robot goes
    forward forever, it will hit something)
> - can create filters, planners over information spaces (good for when we don't
    know, or don't need to know, physical state space)
> - **task specific** design: how to specify tasks?


Mobile Robots
=============

> - many mobile robot tasks are actually properties of the path the robot takes
    through space
    - coverage, environmental monitoring, patrolling, navigation
> - many simple models of mobile robot motion
> - which ones have nice dynamical properties that we can get "for free"
    (without a lot of feedback control)?


Blind, Bouncing Robots
======================

Model the robot as a point moving **in straight lines** in the plane, "bouncing" off the boundary
at a **fixed angle** $\theta$ from the normal:


![A point robot moving in the plane. The top row shows bounces at zero degrees
from the normal. The second row shows bounces at 50 degrees clockwise from
normal. The third row shows the same angle but with a "monotonicity" property
enforced.](../figures/bounce_examples_w_monotone.pdf)


Trapping or Coverage Properties
===============================


![In this environment, bouncing at the normal, the robot will become trapped
in the area between the purple lines.](../figures/triangle_trap.jpg)


Implementation
==============


> - Assume we know environment exactly
> - Can implement on a roomba with bump sensor and IR prox detector [^2]
> - "Collisions" can be virtual - for example, robot w/ camera stops when it is collinear
    with two landmarks, and rotates until one landmark is at a certain heading
> - Also useful model of very small "robots" or microorganisms [^5], or robots in
    low-bandwith environments

[^2]: [@LewOKa13], Lewis & O'Kane IJRR 2013
[^5]: [@microorganism2017], Thiffeault et. al. Physica D Nonlinear Phenomena
2017


Discovery Through Simulation
============================


-   Haskell with *Diagrams* library [@yorgey2012monoids]
-   fixed-angle bouncing, specular bouncing, add noise
-   render diagrams from simulations automatically [^7]

[^7]: \url{https://github.com/alexandroid000/bounce}

\centering

![](../figures/pent_05rad.pdf){width=3cm}\


Simulation Results
==================


\begin{figure}[tp]
\begin{subfigure}{.37\textwidth}
\centering
\includegraphics[width=\linewidth]{../figures/pent_05rad.pdf}
\end{subfigure}%
\begin{subfigure}{0.37\textwidth}
\includegraphics[width=\linewidth]{../figures/pent_1rad.pdf}
\end{subfigure}
\begin{subfigure}{0.37\textwidth}
\includegraphics[width=\linewidth]{../figures/pent_165rad.pdf}
\end{subfigure}%
\begin{subfigure}{0.37\textwidth}
\includegraphics[width=\linewidth]{../figures/pent_3rad.pdf}
\end{subfigure}
\end{figure}



584 Project - Reachability in 2D with SpaceEx
=============================================


\centering code generation for given polygon and bounce angle


\begin{tikzpicture}[->,>=stealth',auto,node distance=2.5cm,
  thick,main node/.style={circle,draw,minimum size = 1.7cm, font=\scriptsize}]
\node[main node] (x0)   [align=center] {$\dot{x} = v_x$\\$\dot{y} =v_y$};

\path[]
    (x0) edge [loop above,thick] node {$e_1$} (x0)
    (x0) edge [loop right,thick] node {$e_2$} (x0)
    (x0) edge [loop left,thick] node {$e_3$} (x0)
    (x0) edge [loop below,thick] node {$e_4$} (x0);

\end{tikzpicture}



References
==========

\tiny

