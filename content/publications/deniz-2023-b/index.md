---
title: Event-based Vision for Early Prediction of Manipulation Actions
authors:
- Daniel Deniz
- Cornelia M. Fermuller
- Eduardo Ros
- José Manuel Rodríguez Álvarez
- Francisco Barranco
date: '2023-01-01'
publishDate: '2026-10-30T08:35:23.823982Z'
publication_types:
- manuscript
doi: 10.48550/arxiv.2307.14332
abstract: Neuromorphic visual sensors are artificial retinas that output sequences
  of asynchronous events when brightness changes occur in the scene. These sensors
  offer many advantages including very high temporal resolution, no motion blur and
  smart data compression ideal for real-time processing. In this study, we introduce
  an event-based dataset on fine-grained manipulation actions and perform an experimental
  study on the use of transformers for action prediction with events. There is enormous
  interest in the fields of cognitive robotics and human-robot interaction on understanding
  and predicting human actions as early as possible. Early prediction allows anticipating
  complex stages for planning, enabling effective and real-time interaction. Our Transformer
  network uses events to predict manipulation actions as they occur, using online
  inference. The model succeeds at predicting actions early on, building up confidence
  over time and achieving state-of-the-art classification. Moreover, the attention-based
  transformer architecture allows us to study the role of the spatio-temporal patterns
  selected by the model. Our experiments show that the Transformer network captures
  action dynamic features outperforming video-based approaches and succeeding with
  scenarios where the differences between actions lie in very subtle cues. Finally,
  we release the new event dataset, which is the first in the literature for manipulation
  action recognition. Code will be available at https://github.com/DaniDeniz/EventVisionTransformer.
---
