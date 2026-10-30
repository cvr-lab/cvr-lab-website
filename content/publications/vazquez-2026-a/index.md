---
title: Remote handling operation for IFMIF-DONES supported by time-sensitive networking
authors:
- Víctor Vázquez
- E. Valenzuela
- Ricardo Shepstone
- Carlos Megías
- Gioacchino Miccichè
- E. Ros
- Francisco Barranco
date: '2026-01-01'
publishDate: '2026-10-30T08:35:23.862317Z'
publication_types:
- article-journal
publication: '*Nuclear Fusion*'
doi: 10.1088/1741-4326/ae511e
abstract: Abstract Experimental fusion research facilities, such as the International
  Fusion Materials Irradiation Facility-DEMO Oriented Neutron Source (IFMIF-DONES),
  require advanced remote handling (RH) systems to perform maintenance and inspection
  tasks in a safe and reliable manner, due to their intrinsic high-radiation nature.
  The mixed-criticality requirements of the data streams used in these systems force
  the deployment of separate networks and communication technologies. Commonly, it
  includes fieldbuses for traffic control, standard Ethernet for video and general-purpose
  traffic, and dedicated networks for the most critical safety-related signals. This
  fragmentation leads to complex and costly deployments and also prevents the application
  of models for predictive maintenance or advanced monitoring. The time-sensitive
  networking (TSN) technology stack aims to provide deterministic behaviour for data
  transmission over standard Ethernet, allowing for convergence on a single network
  and ensuring bounded latencies for critical traffic. In this work, we propose a
  design and validate the TSN-based communication architecture for the RH system of
  IFMIF-DONES. The design ensures bounded delivery times for safety-critical interlock
  signals, achieving a worst-case delay under 30 μ s , even under high network load.
  The proposed network is also validated in a real robotic teleoperation task, where
  artificial intelligence is applied for object detection and tracking, using mixed-criticality
  video streams. Our results show that TSN traffic shapers are essential in providing
  the necessary latency and bandwidth guarantees for such teleoperation tasks, enabling
  network convergence in this kind of deployments.
---
