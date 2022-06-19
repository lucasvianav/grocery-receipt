# Final Project

The aim of the final project is to use image processing techniques to solve a problem that has an image as input and that outputs image(s) and, optionally, additional information. Remember this course is about image processing, not machine/deep learning/neural networks. A significant part of the project must be composed of image processing methods. A machine/deep learning model may be a step on the pipeline, but not the main one.

You don't need to achieve great results. The objective is to LEARN in practice how to solve an image processing task even if the final result is not perfect. If the final report/presentation reveals that the group learned something in the way, then the objective is achieved! Reporting the cases of failure/success is valuable in this scenario.


This activity is in groups of 2 up to 4 undergraduate students.

The following are deliverables (all subject to grading) of this project:

    1. Proposal (deadline 22 May)
    2. Partial Report (deadline 15 June)
    3. Final Report and repository commit (11 July)
    4. Presentations (06 and 13 July)

## Proposal

The proposal comprises:
(a) responding to a form (only one response per group)
(a) creating a Git repository to host the project,
(b) creating a README at the respository with project title, name of the student(s), an abstract that includes the objective of your project, the main image processing tasks involved (such as: image restoration, image segmentation, image description, etc.) and the application (medical imaging, biometry, steganalysis, computational photography, etc.), examples of images that are going to be the input for the intended application
This proposal can be modified/adjusted later, but it is important to define it earlier to allow for better guidance


Some ideas (based on previous projects):

    - Braille to Text Translator
    - Image colorization (from Grayscale to RGB) - OBS: a simple UNet is not valid
    - Image colorization (from non-visible bands to RGB) - OBS: a simple UNet is not valid
    - Combining global/local contrast adjustment using adaptive histograms (HDR)
    - Implementing and Comparing Anti-aliasing Algorithms
    - Pixelizer / Depixelizer of Images - OBS: a simple UNet is not valid
    - Business Card Recognition - OBS: using only CNN / Yolo is not valid
    - Role of pre-processing stages when detecting objects/segmenting images/etc.
    - Segmenting and counting cells in microscope images
    - Segmenting grocery store products and classifying brands - OBS: using only CNN / Yolo is not valid
    - Segmentation of Forest Areas in Google Maps Aerial Images - OBS: using only CNN / Unet etc. is not valid
    - Segmentation of Roads from Google Maps Aerial Images - OBS: using only CNN / Unet /etc. is not valid
    - Skin detection - OBS: using only CNN / Unet /etc. is not valid


---

## Partial Report

The report must update the repository with the final proposal that the group is going to pursuit. It must include an update at the git repository, in particular in the README file for:

    1. The main objective of the project (3 pts),
    2. The description of input images (with examples) including the source of the images --- website, paper, acquired by the student(s) (3 pts),
    3. Description of steps to reach the objective, including the methods that are intented to be used (e.g., image enhancement, edge-detection, morphology, segmentation, texture analysis, color analysis, keypoint detection etc.). (2 pts)
    4. Initial code with first results (tests with basic algorithms in at least one image) (2 pts)

 Commits after the deadline will not be considered as partial report

---

## Final Report and Code Repository

The report can be either a markdown (md) or a notebook (ipynb) file, and must include:

    1. The requirements 1 and 2 for the partial report, updated,
    2. Description of steps and methods used in the project,
    3. Results obtained discussing cases of success and failures,
    4. Names and descriptions of the roles of every student in the project (this will also be assessed via code commits).

The code must include:

    1. The documented/commented source code,
    2. A demo using a jupyter notebook, that allows to run a small instance/example of your project.

OBS1: the report and demo can be written either in English or Portuguese.
OBS2: we prefer Python, but you may use any programming language or package. When using a programming language without support to jupyter notebook, a demo program that runs for an instance of the problem must be provided.

---

## Presentation

The group has to provide a video with a maximum of 8 minutes including, as best as possible the following items:
1. a clear description of the problem in terms of image processing (not a pure machine/deep learning problem), what are the input and output/target images?
2. the source of the images used in the project
3. the methods used during the project (it can include examples of both failure and success) - you don't have to fully explain the methods, but at least mention the steps
4. show results: examples of input-output images, if possible running your demo prepared for the final report
5. what have the group learned about the problem?

This video has to be uploaded at Google Drive and given access to both the professor (moacir@icmc.usp.br) and Teaching Assistant. The video will be played during the session.

Presentation sessions:
-

To receive the grade for presentation, members of the group have to participate in the video and during the session of presentation in order to answer questions.
