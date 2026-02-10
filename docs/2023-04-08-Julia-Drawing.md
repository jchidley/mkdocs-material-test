---
date: "2023-04-08"
title: "Julia Drawing"
tags:
  - julia
  - cad
  - graphics
---
<!-- markdownlint-disable MD025 -->
# Drawing with Julia 
<!-- markdownlint-enable MD025 -->

## Introduction

Smsh based on either its own model or [Open CASCADE](https://dev.opencascade.org/doc/overview/html/index.html), does modeling in Julia and mesh building (2D and 3D). Pretty sophisticaed.

Other Julia interfaces for building things include [OpticSim.jl ](https://microsoft.github.io/OpticSim.jl/dev/csg/), [ConstructiveGeometry.jl](https://github.com/plut/ConstructiveGeometry.jl), [Descartes.jl](https://github.com/JuliaGeometry/Descartes.jl/blob/master/docs/src/design.md)

## GMSH

Just output the geo files to the correct format with the right extensino.

* [gmsh web site](https://gitlab.onelab.info/gmsh/gmsh) — Gmsh is an open-source 3D finite element mesh generator with built-in pre- and post-processing facilities, hosted on GitLab as the main project rep...
* [GMSH build, install](https://gitlab.onelab.info/gmsh/gmsh/-/tree/master/) — This is a bot detection/security checkpoint page for GitLab, not actual content. The page is verifying the user is human before allowing access to ...
* [gmesh Julia Tutorials](https://gitlab.onelab.info/gmsh/gmsh/-/tree/master/tutorials/julia) — This is a GitLab repository page for Gmsh's Julia language tutorials, containing example files that demonstrate how to use the Gmsh finite element ...
* [gmsh documentation](http://gmsh.info/dev/doc/texinfo/gmsh.html) — Gmsh is an open-source 3D finite element mesh generator with CAD-like geometry creation, meshing algorithms, and post-processing visualization capa...

## FEM

* [SymFEL.jl contains several functions useful for the implementation of the finite elements method (FEM), uses SymPy, Gmsh](https://lmbp.uca.fr/~cindea/software/SymFEL.jl/) — SymFEL.jl is a Julia package for implementing the finite element method (FEM), using SymPy for symbolic computation of Lagrange and Hermite basis f...
* [FEM MeshGmshFromShape](https://wiki.freecad.org/FEM_MeshGmshFromShape) — This is a Cloudflare-style bot protection page for the FreeCAD wiki, showing a security check loading screen rather than actual content about FEM m...

## Links

* [Novice Guide](https://dev.opencascade.org/doc/overview/html/samples__novice_guide.html) — This is a beginner's guide to Open CASCADE Technology (OCCT), an object-oriented C++ framework for building CAD/CAM/CAE applications, explaining it...
* [GMSH Tutorial/information](https://bthierry.pages.math.cnrs.fr/tutorial/gmsh/) — A tutorial page explaining how to install and configure GMSH, an open-source 2D/3D mesh and data visualization software, including instructions for...