---
title: A multi-resolution approach for massively-parallel hardware-friendly optical flow estimation
authors:
- Francisco Barranco
- Javier Díaz
- Begoña Pino
- Eduardo Ros
date: '2012-09-01T00:00:00Z'
publication_types:
- article-journal
publication:
  name: Journal of Visual Communication and Image Representation
abstract: This paper presents a novel hardware-friendly motion estimation for real-time applications such as robotics or autonomous navigation. Our approach is based on the well-known Lucas & Kanade local algorithm, whose main problem is the unreliability of its estimations for large-range displacements. This disadvantage is solved in the literature by adding the sequential multiscale-with-warping extension, although it dramatically increases the computational cost. Our choice is the implementation of a multiresolution scheme that avoids the warping computation and allows the estimation of large-range motion. This alternative allows the parallel computation of the scale-by-scale motion estimation which makes the whole computation lighter and significantly reduces the processing time compared with the multiscale-with-warping approach. Furthermore, this last fact also means reducing the hardware resource cost for its potential implementation in digital hardware devices such as GPUs, ASICs, or FPGAs. In the discussion, we analyze the speedup of the multiresolution approach compared to the multiscale-with-warping scheme. For an FPGA implementation, we obtain a reduction of latency between 40% and 50% and a resource reduction of 30%. The final solution copes with large-range motion estimations with a simplified architecture very well-suited for customized digital hardware datapath implementations as well as current multicore architectures.
links:
- type: pdf
  url: https://www.sciencedirect.com/science/article/pii/S1047320312001472
  label: PDF
  icon: document-text
featured: false
---
