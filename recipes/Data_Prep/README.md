# Data Preparation with Data-Prep-Kit (DPK)

We can use data-prep-kit to prepare data for finetuning granite models.

## Overview

Effective data preparation is a critical precursor to both training and fine-tuning workflows in machine learning pipelines. Proper preprocessing, which
includes deduplication, filtering, and cleaning of datasets, ensures that the models trained on this data are robust and perform well on real-world tasks.

## Utilizing DPK while Finetuning Granite Models

Data-Prep-Kit (DPK) is an open-source toolkit designed to facilitate the preparation of unstructured datasets specifically tailored for training/finetuning large language models (LLMs). By leveraging a suite of over 20 preprocessing modules, DPK supports various data types and enables developers to perform intricate tasks such as ingestion, document annotation, filtering, and redaction with ease.

This [sample notebook](./sample-notebook.ipynb) shows some data pre-processing steps that can be used to prepare data for finetuning granite code models.


### Key Features:

- **Modular Design**: Over 20 preprocessing modules for code and natural language tailored to LLM requirements.
- **Framework Compatibility**: Built on Spark and Ray frameworks, ensuring versatility across different computing environments.
- **Community Project**: A collaborative effort aimed at democratizing the preparation of unstructured data for LLM applications.
- **Scalability**: Supports scalable execution through common runtime frameworks such as Python, Ray (local and distributed), Spark, and Kubeflow Pipelines.
- **Customization**: Offers APIs and configurations that allow developers to create custom modules, enhancing the data preparation pipeline for specific use
cases.

### How DPK Streamlines Data Preparation:

DPK's comprehensive library of transforms—or preprocessing modules—offers a foundational set of tools for developers aiming to construct end-to-end data
pipelines, from initial ingestion to final tokenization stages. These have been rigorously tested during the creation of pre-training datasets for Granite's
open models. The integration with Spark and Ray frameworks facilitamoes scalability across diverse computing infrastructures, ensuring a robust foundation for LLM development projects.





