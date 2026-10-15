---
title: Contour motion estimation for asynchronous event-driven cameras
authors:
- Francisco Barranco
- Cornelia Fermüller
- Yiannis Aloimonos
date: '2014-09-01T00:00:00Z'
publication_types:
- article-journal
publication:
  name: Proceedings of the IEEE
abstract: This paper compares image motion estimation with asynchronous event-based cameras to Computer Vision approaches using as input frame-based video sequences. Since dynamic events are triggered at significant intensity changes, which often are at the border of objects, we refer to the event-based image motion as “contour motion.” Algorithms are presented for the estimation of accurate contour motion from local spatio-temporal information for two camera models, the dynamic vision sensor (DVS), which asynchronously records temporal changes of the luminance, and a family of new sensors which combine DVS data with intensity signals. These algorithms take advantage of the high temporal resolution of the DVS and achieve robustness using a multiresolution scheme in time. It is shown that, because of the coupling of velocity and luminance information in the event distribution, the image motion estimation problem becomes much easier with the new sensors which provide both events and image intensity than with the DVS alone. Experiments on synthesized data from computer vision benchmarks show that our algorithm on combined data outperforms computer vision methods in accuracy and can achieve real-time performance, and experiments on real data confirm the feasibility of the approach. Given that current image motion (or so-called optic flow) methods cannot estimate well at object boundaries, the approach presented here could be used complementary to optic flow techniques, and can provide new avenues for computer vision motion research
links:
- type: pdf
  url: http://ieeexplore.ieee.org/abstract/document/6895239/
  label: PDF
  icon: document-text
featured: false
---
