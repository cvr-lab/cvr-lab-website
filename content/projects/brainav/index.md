---
title: BRAINAV - BRAIn-inspired visual processing for real-time energy-efficient autonomous NAVigation
summary: BRAINAV builds on the integration of visual processing pipelines for energy-efficient edge processing using neuromorphic strategies, for the application of autonomous navigation. First, visual processing is crucial in perception system components and specifically, for scene awareness in navigation applications. Robotic agents require understanding their context to plan and make decisions accordingly. This is even more relevant in applications such as robotics. However, computer vision is a very demanding task in terms of resources, and effective navigation requires low latencies to close perception-action loops in real-time. Second, regarding 3D perception and scene understanding, state-of-the-art solutions are focused on accuracy performance but other qualities such as energy consumption must be also taken into account. BRAINAV has developed and validated bio-inspired perception and autonomous navigation pipelines based on neuromorphic event cameras, efficient embedded AI, and onboard processing. The project culminated in autonomous UAV demonstrators integrating event and conventional cameras, inertial sensing, GNSS and LiDAR, with all perception, planning and control running onboard.
date: '2023-01-19T00:00:00Z'
lastmod: '2026-08-31T00:00:00Z'
tags:
- Neuromorphic
- Real-time systems
- Autonomous navigation
- Drones
- Machine Learning
- Computer vision
- Edge AI
authors:
- Francisco Barranco
links:
- type: code
  url: https://github.com/orgs/cvr-lab/repositories
  label: Code
  icon: brands/github
image:
  caption: ''
  focal_point: Smart
---

* This work was supported by the National Project PID2022-141466OB-I00 funded by MICIU/AEI/10.13039/501100011033 and by ERDF/EU.
{{< figure src="aei_logo.png" id="AEI_logo" >}}

## Summary
BRAINAV aims at developing bio-inspired pipelines for real-time energy-efficient visual navigation that operates in the real-world in optimized platforms embedded onboard mobile robots. First, we need the development of a new paradigm for computer vision that allows us to effectively work with asynchronous neuromorphic sensors that imitate visual retinas and the development of high-performance architectures for reaching real-time performance with them. Then, we also require efficient ML networks for reaching low-energy inference and eventually, to propose new bio-inspired components to solve mapping, localization, and path planning for exploration. We are committed to prove the potential of our energy-efficient vision pipelines and therefore, we propose the use case of autonomous navigation using mobile robots.

Video processing is crucial in perception due for environment understanding. However, computer vision is a very demanding task and in robotics it requires to close perception-action loops in real-time. Moreover, distributed local mobile nodes need low-energy operation since they run on batteries. Power consumption vs. performance is a challenging trade-off, especially in distributed environments, given the number of sensors, the heterogeneity of the system, their autonomy or their need of high performance. Our hypothesis is that biologically-inspired strategies will help us achieve energy-efficient solutions that reach good levels of accuracy while operating in real-time in real scenarios.

The final demonstrators consist of UAV platforms equipped with event and conventional cameras, inertial sensors, telemetry and GNSS, with one configuration additionally including LiDAR. All perception, planning and control components run onboard using an NVIDIA Jetson Orin. Real outdoor experiments validated autonomous flight, trajectory tracking at speeds up to 8 m/s, detection of other UAVs, autonomous obstacle perception and avoidance, and simple LiDAR-based mapping. BRAINAV contributes directly to the thematic priority "Digital World, Industry, Space and Defence" through advances in artificial intelligence, autonomous robotics, neuromorphic vision and embedded processing. 


## Objectives

The main general objective of BRAINAV is the development of a bio-inspired pipeline for real-time
energy-efficient visual navigation that operates in the real-world in optimized platforms embedded in
mobile robots. First, we need the development of a new paradigm for computer vision that allows us
to effectively work with these asynchronous neuromorphic sensors and the development of high-
performance architectures for reaching real-time performance. Then, we also require efficient ML
networks for reaching low-energy inference and eventually, to propose new bio-inspired components
to solve mapping, localization, and path planning for exploration. Finally, we also propose to prove
the potential of our energy-efficient vision pipelines for autonomous navigation using mobile robots.

Our specific objectives (SO) are detailed next:

*SO1. To develop of event-driven perception for navigation tasks.*
As mentioned before in the state of the art, some works have addressed the task previously with event-
based sensors [BAR14a, BAR21, VID18]. However, their results are still very poor, reaching only low
performance. In our previous work, we have thoroughly studied alternative knowledge-based methods
for 3D perception, mainly image motion and 3D motion estimation. In BRAINAV, we
propose to study new methods based on Machine Learning solutions [DEN23, ISE23] to achieve
better accuracy performance. Also, most of the previous methods build images out of accumulation of
events for prefixed time intervals and apply classic methods to these artificial images. This severely
harms the performance and does not take advantage of the main feature of neuromorphic sensors, their
high-temporal resolution or low latency. We propose the development and evaluation of event-driven
methods for motion and 3D geometry estimation [BAR21]. Lastly, the accuracy of our solution will be
evaluated using novel benchmarks and datasets that integrate both events and images using the motion
capture system available in our lab. Moreover, we are committed to the Open Science principles and
will release the datasets for the community. This is crucial for the adv ancement of neuromorphic
engineering, due the current lack of datasets and their relevance for Machine Learning techniques.

*SO2. To optimize for real-time energy-efficient processing engines.*
In an effort to reduce the computational complexity of the prop osed solutions, we will explore
different mechanisms for low-energy computation. First, we propose the use of optimization
techniques on ANNs such as: model quantization [LIA21] shortening bit widths for inference to reduce
computational complexity; pruning [VAD22], that removes connections with smaller values in
networks; and distillation [DEN23], that allows transferring knowledge from teacher complex models
to student simpler ones. Second, we are also interested in exploring new techniques based on Spiking
Neural Networks. These are biologically-plausible neural architectures do take into account energy
consumption [DAV21] doing learning with sparse data. We also propose the exploration of brain-like
structures to build new navigation methods that imitate their functionalities. 

*SO3. To implement real-time processing on embedded platforms with neuromorphic sensors.*
Dealing with a real-world application imposes restrictions such as real-time performance for closing
our perception-action loops for autonomous navigation. We will consider different hardware
accelerators such as GPUs or FPGAs, using the latest advancements for the development of fine-
tuning pipelines (e.g. DeepStream) and for optimized hardware datapaths (e.g. Vitis AI). The selected
hardware accelerator will impose different non-functional requirements on the implementations
developed for SO1 and functionally optimized for SO2, for performance, latency and power
consumption. This objective also pursues the effective integration of the asynchrono us sensors into
von Neumann architectures which is by itself, an additional challenge.

*SO4. To demonstrate embedded autonomous navigation onboard mobile robots*
Finally, this objective aims at the validation of the proposed models and architectures considered in
the SO1-SO3, with different demonstrators for autonomous navigation tasks in real-world
environments. This application allows us to demonstrate the maximum potential of our optimized bio-
inspired pipelines and downstream processing, while ensuring the overall optimization in the
exploration task relying mainly on learning models. Our goal in SO4 is to develop a first semi-
autonomous platform to perform first localization and mapping. This prototype will have a minimum
intervention of a human pilot, and will be used to validate the mentioned tasks in unknown scenarios.
The second prototype will show the final autonomous explorer that will be enabled with additional
downstream applications such as the detection of other mobile robots in the scenario and possibly
tracking them, or finding specific targets.

## Final autonomous navigation demonstrator

The final BRAINAV demonstrator integrates the main scientific and technological results of the project into a real autonomous UAV. The platform combines:

- Neuromorphic event cameras
- Conventional cameras
- Inertial sensing
- GNSS and telemetry
- LiDAR in one of the configurations
- NVIDIA Jetson Orin onboard processing
- ROS-based perception, planning and control

All computation is performed onboard the UAV. The platform was validated through real outdoor flights at the Cubillas test area.

{{< figure src="brainav_flight_test.jpg" caption="UAV platform and outdoor autonomous flight experiments at the Cubillas test area." >}}

## Background references
* [BAR14a] F. Barranco, C. Fermüller, Y. Aloimonos. "Contour motion estimation for asynchronous event-driven cameras." Proceedings of the IEEE 102, no. 10 (2014): 1537-1556.

* [BAR21] F. Barranco, C. Fermüller, Y. Aloimonos, E. Ros. "Joint direct estimation of 3D geometry and 3D motion using spatio temporal gradients." Pattern Recognition, 113, 2021.

* [DAV21] S. Davidson, S. B. Furber. "Comparison of artificial and spiking neural networks on digital hardware." Frontiers in Neuroscience 15 (2021): 651141.

* [DEN23] D. Deniz, J. Isern, J. Solanti, P. Jääskeläinen, P. Hnětynka, L. Bulej, E. Ros, F. Barranco. "Efficient reconfigurable CPS for monitoring the elderly at home via Deep Learning." Journal of Signal Processing Systems, (2023). 

* [ISE23] J. Isern, G. Jimenez-Perera, L. Medina-Valdés, P. Chaves, D.Pampliega F. Ramos, F. Barranco. "A Cyber-Physical System for integrated remote control and protection of smart grid critical infrastructures.", Journal of Signal Processing Systems, 2023.

* [LIA21] T. Liang, J. Glossner, L. Wang, S. Shi, X. Zhang. "Pruning and quantization for deep neural network acceleration: A survey." Neurocomputing 461 (2021): 370 -403.

* [VAD22] S. Vadera, S. Ameen. "Methods for pruning deep neural networks." IEEE Access 10 (2022): 63280-63300.

* [VID18] A. Vidal, H. Rebecq, T. Horstschaefer, D. Scaramuzza. "Ultimate SLAM? Combining events, images, and IMU for robust visual SLAM." IEEE Robotics and Automation 3, no. 2 (2018).

## Lists of contributions: publications, datasets, and code repositories

* [DEN24] Deniz, D., Ros, E., Ortigosa, E. M., & Barranco, F. (2024). **Optimized edge-cloud system for activity monitoring using knowledge distillation.** Electronics, 13(23), 4786. [DOI](https://doi.org/10.3390/electronics13234786)

* [NOV24] Novo, A., Lobon, F., Garcia de Marina, H., Romero, S., & Barranco, F. (2024). **Neuromorphic perception and navigation for mobile robots: a review.** ACM Computing Surveys, 56(10), 1-37. [DOI](https://doi.org/10.1145/3656469)

* [DEN25] Deniz, D., Isern, J., Solanti, J., Jääskeläinen, P., Hnětynka, P., Bulej, L., Ros, E., & Barranco, F. (2025). **Efficient reconfigurable system for home monitoring of the elderly via action recognition.** Engineering Applications of Artificial Intelligence, 158, 111383. [DOI](https://doi.org/10.1016/j.engappai.2025.111383)

* [JIM25] Jimenez-Perera, G., Valencia-Vidal, B., Luque, N. R., Ros, E., & Barranco, F. (2025). **Informed Federated Learning to Train a Robotic Arm Inverse Dynamic Model.** IEEE Robotics and Automation Letters, 10(10), 11022-11029. [DOI](https://doi.org/10.1109/LRA.2025.3608659)

* [VAZ26] Vázquez, V., Valenzuela, E., Shepstone, R., Megías, C., Miccichè, G., Ros, E., & Barranco, F. (2026). **Remote handling operation for IFMIF-DONES supported by time-sensitive networking.** Nuclear Fusion, 66, 046029. [DOI](https://doi.org/10.1088/1741-4326/ae511e)

* [NOV25a] Novo, A., Fermüller, C., Rodríguez-Álvarez, M., Romero, S., & Barranco, F. (2026). **On ego-motion estimation from event-inertial-aided normal flow fields.** Computer Vision and Image Understanding. Under review.

* [NOV25b] Novo, A., Fermüller, C., Romero, S., Rodríguez-Álvarez, M., & Barranco, F. (2026). **Event-based vision for online inference of fine-grained manipulation actions.** Engineering Applications of Artificial Intelligence. Under review (second round).

### Other scientific contributions

* [SAL25-CONG] Salinas, I., Romero, S. F., Molero, J. A., Gutiérrez de León, B., Banqueri, J., & Barranco, F. (2025). **Clasificación de UAS basado en Inteligencia Artificial para dar soporte a sistemas de defensa antiaérea.** XII Congreso Nacional de I+D en Defensa y Seguridad, Zamora, Spain, pp. 105-106. ISBN 978-84-1083-073-8. Premio Antonio Torres al mejor trabajo (ISDEFE).

* [HER25] Heredia, A. J., Pérez, F. V., Novo, A., Romero, S. F., García Imbernón, G., Ortega, J. F., García, V., Albaladejo, D., Méndez, M., & Barranco, F. (2025). **Automatización inteligente del sostenimiento en buques mediante sensórica avanzada e IA.** XII Congreso Nacional de I+D en Defensa y Seguridad, Zamora, Spain, pp. 167-168. ISBN 978-84-1083-073-8.

* [CUA23] Cuadrado, J., Barranco, F., & Masquelier, T. (2023). **Optical flow estimation from event- and frame-based camera fusion.** Biocomp Colloque 2023, Toulouse, France.

### Datasets and open-source resources

* **IndoorActionDataset** — Dataset associated with [DEN24]. 
  [DATA](https://github.com/DaniDeniz/IndoorActionDataset)

* **CIAV Dataset** — Dataset associated with [DEN25].
  [DATA](https://github.com/DaniDeniz/CIAV-dataset)

* **Efficient action recognition models** — Code and neural-network weights associated with [DEN25]. 
  [CODE](https://github.com/DaniDeniz/efficient-action-recognition-for-home-monitoring)

* **Baxter robot dataset for learning dynamic models** — Dataset associated with [JIM25], released under CC BY 4.0. 
  [DATA](https://zenodo.org/records/17035193) 
  [CODE](https://github.com/GabriJP/ifl_baxter.git)

* **E-MAD — Event-based Manipulation Action Dataset** — Dataset associated with [NOV25b]. The dataset is currently under embargo during the publication process and will be released under CC BY 4.0 after publication.

* **Event-inertial ego-motion code** — Code associated with [NOV25a]. The repository will be made public after publication of the corresponding article.


## Authors

* **Francisco Barranco** - Principal Investigator, University of Granada, CVRLab / CITIC-UGR

## Acknowledgments

* This work was supported by the National Project PID2022-141466OB-I00 funded by MICIU/AEI/10.13039/501100011033 and by ERDF/EU.
{{< figure src="aei_logo.png" id="AEI_logo" >}}

## License

Software, datasets and other research outputs associated with BRAINAV are distributed under the licenses indicated in their corresponding repositories.

Unless otherwise stated, the contents of this website are provided for scientific dissemination purposes. Please refer to each publication, dataset or software repository for its specific copyright and licensing conditions.
