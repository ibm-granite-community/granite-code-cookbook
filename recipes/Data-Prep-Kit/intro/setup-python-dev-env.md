# Setup a Local Python Dev Environment

## Step-1: Anaconda Python environment

You can install Anaconda by following the [guide here](https://www.anaconda.com/download/).

## Step-2: Create a custom environment

We will create an environment for this workshop with all the required libraries installed.


```bash
conda create -n data-prep-kit-1 -y python=3.11
```

Activate the new conda environment

```bash
conda activate data-prep-kit-1
```

Make sure env is swithced to data-prep-kit-1.

**Make sure python version is 3.11**

```bash
python --version
```

**Note**: If you are on a linux system install these too

```bash
conda install gcc_linux-64

conda install gxx_linux-64
```

Get the repo

```bash
git   clone  https://github.com/ibm-granite-community/granite-code-cookbook/
```

```bash
cd    recipes/Data-Prep-Kit/intro/
```

install all needed packages

```bash
pip install -r requirements.txt
```

Install a custom kernel 

```bash
python -m ipykernel install --user --name=data-prep-kit --display-name "dataprepkit"
```


## Start-3: Start Jupyter

```bash
jupyter lab
```

## Troubleshooting

### If libraries are not loading in Jupyter:  Select custom Kernel


When running Jupyter notebooks, if data prep kit libraries are not found, try selecting the custom kernel you created (`dataprepkit`)