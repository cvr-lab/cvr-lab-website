---
title: On-chip semidense representation map for dense visual features driven by attention processes
authors:
- Sara Granados
- Francisco Barranco
- Sonia Mota
- Javier Díaz
- Eduardo Ros
date: '2014-09-01T00:00:00Z'
publication_types:
- article-journal
publication:
  name: Journal of Real-Time Image Processing
abstract: We describe an intelligent scheme to condense dense vision features, efficiently reducing the size of representation maps and keeping relevant information for further processing during subsequent stages. We have integrated our condensation algorithm in a low-level-vision system that obtains several vision-features in real-time working on an FPGA. Within this framework, our condensation algorithm allows for the transfer of information from the FPGA device (or processing chip) to any co-processor (from embedded ones to external PCs or DSPs) under technological constraints (such as bandwidth, memory and performance ones). Our condensation core processes 1024 × 1024 resolution images at up to 90 fps. Hence, our condensation module performs this process introducing an insignificant delay in the vision system. A hardware implementation usually implies a simplified version of the vision-feature extractor. Therefore, our condensation process inherently regularizes low-level-vision features, effectively reducing discontinuities and errors. The semidense representation obtained is compatible with mid-/high-level-vision modules, usually implemented as software components. In addition, our versatile semidense map is ready to receive feedback from attention processes, integrating task-driven attention (i.e. top-down information) in real time. Thus, the main advantages of this core are real-time throughput, versatility, inherent regularization, scalability and feedback from other stages.
links:
- type: pdf
  url: https://link.springer.com/article/10.1007/s11554-012-0320-3
  label: PDF
  icon: document-text
featured: false
---
