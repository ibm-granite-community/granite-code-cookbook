# Running the Granite Code Recipe Notebooks Locally
How to run the Granite Code recipe Jupyter notebooks on your computer.

## Clone the Granite Code Cookbook Repository

Clone the repo and cd into the repo directory.


```python
git clone git@github.com:ibm-granite-cookbooks/granite-code-cookbook.git

cd granite-code-cookbook
```

## Create and Activate a Virtual Environment

Use a [python virtual environment](https://docs.python.org/3/library/venv.html) for installed libraries. Open a terminal, and from the command line, run:


```python
python -m venv .venv
```

Activate the virtual environment in the by running:


```python
source ./.venv/bin/activate
```

## Install and Run Jupyter

For more detail, see the installation Instructions at [Jupyter.org](https://jupyter.org/install)

Install jupyter notebook with pip in the virtual environment:


```python
pip install notebook
```

## Open a Recipe in Jupyter Notebook

To open a recipe notebook in jupyter, from the virtual environment, run:

```jupyter notebook <recipe-notebook-file-path>```

To run the "Text to Shell" recipe from the repository root, for example:


```python
jupyter notebook ./recipes/Text_to_Shell/Text_to_Shell.ipynb
```

You should see the notebook in your browser now!

## Extra: Jupyter Lab

[Jupyter Lab](https://jupyter.org/try-jupyter/lab/) provides a web-based notebook IDE, for interactive development of Jupyter notebooks.


```python
pip install jupyterlab

jupyter lab
```
