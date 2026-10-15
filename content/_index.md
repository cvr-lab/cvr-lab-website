---
title: ''
date: 2026-10-15
type: landing

sections:
  - block: hero
    content:
      title: Computer Vision and Robotics Lab
      text: The Computer Vision and Robotics Lab is a research group for active vision, real-time processing, neuromorphic engineering, and robotics.
      media:
        src: hero.jpg
      primary_action:
        text: Our projects
        url: projects/
      secondary_action:
        text: Meet the team
        url: people/
    design:
      layout: split-left

  - block: markdown
    id: about
    content:
      title: About the lab
      text: |-
        Welcome to the Computer Vision and Robotics Lab, part of the [Department of Computer Engineering, Automation and Robotics](https://icar.ugr.es/) at the [University of Granada](https://www.ugr.es). The Computer Vision and Robotics Lab focuses on the research on active vision, autonomous navigation, neuromorphic vision, control, perception - action loops, collaboration and robotics. We are not interested on passive vision sensors but rather on sensors that can actively change their point of view or perspective, the way they perceive their environment by adaptation or select the most important information driven by the task assuming that allows for smart decision making. To enable active vision, our research is also focused on architectures that achieve real-time performance.

        We have long expertise on low-level image processing: we have done optical flow algorithms (energy based, gradient based, block matching, etc.) and similar approaches for stereo models; we have also models for foreground/background subtraction (in surveillance applications) and local contrast descriptors (pixel wise orientation, energy, intrinsic dimensionality, etc.). We are also interested in multi-perspective vision, autonomous navigation, or structure from motion, specially any processing from motion that can be achieved in real-time. We have worked in different fields bus specially on ADAS (Advanced Driving Assistance Systems for cars), autonomous navigation with UAVs, video-surveillance applications, robotics.
    design:
      columns: '1'

  - block: portfolio
    id: projects
    content:
      title: Projects
      count: 6
      filters:
        folders:
          - projects
      buttons:
        - name: All
          tag: '*'
        - name: Robotics
          tag: Robotics
        - name: Neuromorphic
          tag: Neuromorphic
        - name: Deep Learning
          tag: Deep Learning
        - name: FPGA
          tag: FPGA
        - name: Drones
          tag: Drones
      default_button_index: 0
      archive:
        link: /projects/
        text: All projects
    design:
      columns: 3
      fallback_icon: cpu-chip

  - block: collection
    id: news
    content:
      title: Latest News
      count: 5
      filters:
        folders:
          - blog
      order: desc
      archive:
        enable: true
        link: /blog/
        text: All news
    design:
      view: date-title-summary
---
