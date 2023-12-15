# Cow Identification Using Deep Learning

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage Instructions](#usage-instructions)
- [How it Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Biometric systems use various methods for identifying humans, and this approach can be effectively applied to cows. Traditionally, cows have been identified using methods like ear tags, tattoos, and electronic chips, which can cause health concerns. This project leverages Artificial Intelligence, specifically deep learning, to develop a non-invasive, efficient, and reliable model for identifying cows using their muzzleprint images, similar to facial and fingerprint recognition in humans.

## Installation
This codebase is designed to work in Google Colab. Follow these steps to set it up:

Clone the repository:

Via HTTPS: `git clone https://github.com/Nschadrack/Cattle-Identification-MP.git`
Via SSH: `git clone git@github.com:Nschadrack/Cattle-Identification-MP.git`
Create a virtual environment:

With virtualenv: `virtualenv venv`

Activate it:

Windows: `source path-to-venv/scripts/activate`
Mac/Linux: `source path-to-venv/bin/activate`
With Conda:

Create: `conda create -n venv-name`
Activate: `conda activate venv-name`
Install required packages:

Navigate to the project's root directory.
Run `pip install -r requirements.txt` (Windows) or `pip3 install -r requirements.txt` (Mac/Linux).

## Usage Instructions
To run the project, you need access to the dataset and must modify the data-path in the scripts. The environment requires Python 3.7+. For notebook usage, upload them to Google Colab or a similar platform supporting Jupyter Notebooks. The model training in Google Colab requires a minimum of 32GB RAM and a 16GB GPU, with a batch size of 32 and a model of 35M parameters.

## How it Works
This project implements two methods: Dot Product Approach and SIAMESE Network.

The notebooks folder contains all notebooks and python files contains scripts we used for generating low quality images from original dataset using different image preprocessing techinques. 

### 1. Dot Product
  A novel approach involving a CNN model trained to extract features from images.
We use Resnet50 as the CNN feature extractor, removing the fully connected network and replacing it with Dot Product.
   ### Model Architecture
   ![image](https://github.com/Nschadrack/Cattle-Identification-MP/assets/50202646/44f6ca9f-aa04-4500-a74a-202182a303e2)

   ### Training and Prediction Processes
    ![image](https://github.com/Nschadrack/Cattle-Identification-MP/assets/50202646/bbe37caa-720b-4b4a-ad46-e2835c1dadad)


### 2. SIAMSE Netowrk
   
   Utilizes pairwise similarity checks between two images.
   
   ![image](https://github.com/Nschadrack/Cattle-Identification-MP/assets/50202646/900148a8-335b-4648-9c77-2bf24d58b671)


   ### Pipeline for Making the Prediction
   
   Flow chart showing how we predict a cow identity given an image.
   
   ![image](https://github.com/Nschadrack/Cattle-Identification-MP/assets/50202646/24725a2c-4454-46e7-bf48-fe742b314909)

   #### Pipeline for Adding a New Cow to the Model
   Flow chart showing how the model works by adding images of a new cow without retraining.  
    ![image](https://github.com/Nschadrack/Cattle-Identification-MP/assets/50202646/da81ad32-83b7-48da-9d62-3f2cfa0aaed9)

   You can read more from our [Paper](www.google.com)

## Contributing
We are exploring improvements to the dot product approach, particularly in maintaining model stability and accuracy when adding more cows. Contributions are welcome. To contribute, clone the repository and create a pull request (PR).


