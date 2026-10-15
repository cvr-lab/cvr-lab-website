---
title: Real-time architecture for a robust multi-scale stereo engine on FPGA
authors:
- Matteo Tomasi
- Mauricio Vanegas
- Francisco Barranco
- Javier Díaz
- Eduardo Ros
date: '2012-09-01T00:00:00Z'
publication_types:
- article-journal
publication:
  name: IEEE Transactions on Very Large Scale Integration (VLSI) Systems
abstract: In this work, we present a real-time implementation of a stereo algorithm on field-programmable gate array (FPGA). The approach is a phase-based model that allows computation with sub-pixel accuracy. The algorithm uses a robust multi-scale and multi-orientation method that optimizes the estimation extraction with respect to the local image structure support. With respect to the state of the art, our work increases the on-chip power of computation compared to previous approaches in order to obtain a good accuracy of results with a large disparity range. In addition, our approach is specially suited for unconstrained environments applications thanks to the robustness of the phase information, capable of dealing with severe illumination changes and with small affine deformation between the image pair. This work also includes the rectification images circuitry in order to exploit the epipolar constraints on the chip. The dedicated circuit can rectify and process images of VGA resolution at a frame rate of 57 fps. The implementation uses a fine pipelined method (also with superscalar units) and multiple user defined parameters that lead to a high working frequency and a good adaptability to different scenarios. In the paper, we present different results and we compare them with state of the art approaches.
links:
- type: pdf
  url: http://ieeexplore.ieee.org/abstract/document/6071001/
  label: PDF
  icon: document-text
featured: false
---
