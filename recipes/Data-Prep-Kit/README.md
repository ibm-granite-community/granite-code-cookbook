# Data Prep Kit (DPK) Examples and Recipes

[Data Prep Kit](https://github.com/IBM/data-prep-kit/) is an open source library to help with data preperation for LLM applications.

This folder contains examples of the DPK.

## Running the code

Some of the notebooks can be run on Google Colab environmenet.  Some of them require a local python development environment setup.

Please follow these [instructions](./setup-python-dev-env.md) to setup your local python dev env.

## DPK Intro

This example will demonstrate some of the modules (transformations) available in DPK.

We will show how to process PDF files.

`PDFs ---> text ---> chunks --->   exact dedupe ---> fuzzy dedupe ---> embeddings`

[python version](dpk_intro_1_python.ipynb)  &nbsp;   |   &nbsp;  [ray version](dpk_intro_1_ray.ipynb)
