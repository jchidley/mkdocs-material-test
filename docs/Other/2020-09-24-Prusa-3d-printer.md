---
date: "2020-09-24"
title: "Prusa 3d Printer"
---
<!-- markdownlint-disable MD025 -->
### Prusa Mk3S
<!-- markdownlint-enable MD025 -->

<!-- markdownlint-disable MD034 -->

## Setup

Z Level - currently about -1.1mm. Raised on the left by 20 microns, probably needs to be reaised at the front.

[Bed Level Correction](https://help.prusa3d.com/article/bed-level-correction_2267#how-to-use-bed-level-correction)

Using Maker's Muse Clearance Castle models (Clearance card and drawbridge) and Califlower/Calilantern from Vector 3D.

## Designing for 3D printing

Chamfer bottom/top edges to avoid foot (say 1 layer thickness) for dimensional accuracy.

[5 3D Printing Tips the ELITES don't want you to know... #3DP101](https://www.youtube.com/watch?v=9-6tIkTrcwA)

[Printing tips - including TPU](https://www.youtube.com/watch?v=iWZw7RO2Sks) 
[How to 3D Print like a Pro using Custom Modifier Meshes!](https://www.youtube.com/watch?v=iziTcOLKfFc)

* support for holes, with single filaments or single layer, or stepped layers
* G10 sheet
* Food dehydrator
* Bed adhesion: prit stick and alcohol in a single layer
* Slice from STEP files

[How-to Design for Mass Production 3D Printing](https://www.youtube.com/playlist?list=PLkUv8_afCbJ9zfaZxqL4AHBrGHqTaU9lo) a whole stack of useful 3D printing design tips (chamfers, surface effects, printing on edge, etc)

### Printer Settings

[5 3D Printing Tips the ELITES don't want you to know... #3DP101](https://www.youtube.com/watch?v=9-6tIkTrcwA)

[5 Slicer defaults I ALWAYS change #3DP101](https://www.youtube.com/watch?v=mE521Q4H6aY)

[Advanced Slicer Settings using Custom Modifier Meshes!](https://www.youtube.com/watch?v=iziTcOLKfFc)

Layers and Perimeters, Vertical shells, Perimiters: 3
Layers and Perimiters, Advanced, Seam position: Aligned
Infill, Fill pattern: either Adaptive Cubic or Gyroid

### Filaments

Need to test printer with actual filament

Temperature testing (for stringing and overhangs).

Maker's Muse Clearance Castle models (not the full castle). See [Can you Conquer the Clearance Castle?](https://www.youtube.com/watch?v=hueVDUQUQng)

[Print in Place Engine Benchmark - The Bengine](https://www.printables.com/model/212989-print-in-place-engine-benchmark-the-bengine) with [video](https://www.youtube.com/watch?v=DFjD8iOUx0I)

Size, skew and tolerances, useful to see shrinkage for particular filaments [Califlower for 2D](https://www.youtube.com/watch?v=QZtND2D1U1A) which is quicker than the more comprehensive [Calilantern 3D toleraaces](https://www.youtube.com/watch?v=5c4K7kiPNrg). Prusa does the scaling and skew automatically, but the filament needs measuring too.

[Calibration Cubes: More Harm Than Good?](https://www.youtube.com/watch?v=H7OsnMLDIMw)

[7 super satisfying 3D printing torture tests](https://youtu.be/m25NEKcUwuI?si=hz3EKKGi34qgJOaw)

### Filamentie rPETg

I added brims to ensure the first layer stuck properly, gyroid fill in, 10C difference between first and subsequent layers, 215C overall temp (225C first).

### OctoPi

[Octoprint](https://octoprint.org/)
[OctoPi setup for Original Prusa i3 MK3](https://www.youtube.com/watch?v=_XACqEA1hHU)
[Octoprint Raspberry 4B + 4K webcam guide and the latest great plugins](https://www.youtube.com/watch?v=h--RLbvQKYc)
[Top Must Have OctoPrint Plugins For Your 3D Printer](https://www.youtube.com/watch?v=ndE91ls-ruQ&t=251s)
[PrusaSlicer](https://www.prusa3d.com/prusaslicer/)

<!-- markdownlint-enable MD034 -->
