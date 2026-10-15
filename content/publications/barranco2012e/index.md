---
title: Vector disparity sensor with vergence control for active vision systems
authors:
- Francisco Barranco
- Javier Díaz
- Agostino Gibaldi
- Silvio P Sabatini
- Eduardo Ros
date: '2012-09-01T00:00:00Z'
publication_types:
- article-journal
publication:
  name: Sensors
abstract: This paper presents an architecture for computing vector disparity for active vision systems as used on robotics applications. The control of the vergence angle of a binocular system allows us to efficiently explore dynamic environments, but requires a generalization of the disparity computation with respect to a static camera setup, where the disparity is strictly 1-D after the image rectification. The interaction between vision and motor control allows us to develop an active sensor that achieves high accuracy of the disparity computation around the fixation point, and fast reaction time for the vergence control. In this contribution, we address the development of a real-time architecture for vector disparity computation using an FPGA device. We implement the disparity unit and the control module for vergence, version, and tilt to determine the fixation point. In addition, two on-chip different alternatives for the vector disparity engines are discussed based on the luminance (gradient-based) and phase information of the binocular images. The multiscale versions of these engines are able to estimate the vector disparity up to 32 fps on VGA resolution images with very good accuracy as shown using benchmark sequences with known ground-truth. The performances in terms of frame-rate, resource utilization, and accuracy of the presented approaches are discussed. On the basis of these results, our study indicates that the gradient-based approach leads to the best trade-off choice for the integration with the active vision system.
links:
- type: pdf
  url: http://www.mdpi.com/1424-8220/12/2/1771/htm
  label: PDF
  icon: document-text
featured: false
---
