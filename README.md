# Groceries Receipt Recognition and Splitting

Repository for the "SCC0251 - Digital Image Processing" course's project offered for Computer Science undergraduates at ICMC - USP, by professor Moacir Antonelli Ponti.

For a quick guide of how to setup the project, see [docs/SETUP.md](./docs/SETUP.md).

## Group

- Abner Ignacio Melin Leite - 10415165
- Antônio Pedro Medrado - 10748389
- Lucas Henrique Sant'Anna - 10748521
- Lucas Viana Vilela - 10748409

## Abstract

The project's proposal is to build a practical means of splitting a grocery store purchase between a group of friends, in which different arbitrary subgroups of people can buy together the various items. The system will make use of image enhancement, restoration and segmentation (as well as OCR) in order to digitalize photos of grocery receipts (input images shot by the group) and provide the user with an interface for splitting the items between a group of people. The system will perform the calculations of how much each individual should pay and then output these values.

The grocery receipt will be segmented out of the picture and image enhancement and restoration will be used to make it more readable (less noise/motion blur, better perspective, higher contrast, etc), making it easier for the OCR functionality to recognize the text in it.

A more detailed report can be found in [docs/REPORT.md](./docs/REPORT.md) and the assignment can be found in [docs/ASSIGNMENT.md](./docs/ASSIGNMENT.md).
