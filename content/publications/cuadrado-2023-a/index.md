---
title: Optical flow estimation from event-based cameras and spiking neural networks
authors:
- Javier Cuadrado
- Ulysse Rançon
- Benoit R. Cottereau
- Francisco Barranco
- Timothée Masquelier
date: '2023-01-01'
publishDate: '2026-10-30T08:35:23.828219Z'
publication_types:
- article-journal
publication: '*Frontiers in Neuroscience*'
doi: 10.3389/fnins.2023.1160034
abstract: Event-based cameras are raising interest within the computer vision community.
  These sensors operate with asynchronous pixels, emitting events, or \"spikes\",
  when the luminance change at a given pixel since the last event surpasses a certain
  threshold. Thanks to their inherent qualities, such as their low power consumption,
  low latency, and high dynamic range, they seem particularly tailored to applications
  with challenging temporal constraints and safety requirements. Event-based sensors
  are an excellent fit for Spiking Neural Networks (SNNs), since the coupling of an
  asynchronous sensor with neuromorphic hardware can yield real-time systems with
  minimal power requirements. In this work, we seek to develop one such system, using
  both event sensor data from the DSEC dataset and spiking neural networks to estimate
  optical flow for driving scenarios. We propose a U-Net-like SNN which, after supervised
  training, is able to make dense optical flow estimations. To do so, we encourage
  both minimal norm for the error vector and minimal angle between ground-truth and
  predicted flow, training our model with back-propagation using a surrogate gradient.
  In addition, the use of 3d convolutions allows us to capture the dynamic nature
  of the data by increasing the temporal receptive fields. Upsampling after each decoding
  stage ensures that each decoder's output contributes to the final estimation. Thanks
  to separable convolutions, we have been able to develop a light model (when compared
  to competitors) that can nonetheless yield reasonably accurate optical flow estimates.
---
