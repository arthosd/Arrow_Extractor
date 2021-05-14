# Arrow Extractor

This project is an extention of Dr. Laurent Wendling works on Medical Arrow detector for medical purposes.

## Getting Started

Before running the project you'll need to install run the following commands to install all the necessary dependencies.

### Dependencies

```bash
pip3 install -U opencv-python
pip3 install -U scikit-learn
pip3 install -U numpy
```

### Configuration files

You'll need to configure the project by assigning a target directory and the source directory in the src/Config/config.cfg.

- **_Only use data that are arrange in subdirectories. You can checkcRESJPG's structure to create your own directory's structure._**

- **_For evaluation use RESJPG directory._**

The following explains the different parameters of the config file.

```cfg
[RESSOURCES]
target_directory = ------- > Directory where result are stored
src_directory = ------- > Directory from where are the data to cluster

[GFD]
rad = 6 ---> Radian frenquency
ang = 6 ---> Angular frenquency

[CLUSTER]
nombre_cluster = 2 ---> Number of cluster for clustering data

[FILTRE]
si = 500 --> Minimal surface to accept component
ss = 1000 --> Maximal surface to accept component
```

## Running the project

When all librairies are installed run the following command **_project's root_** to run the project.

```
python3 src/init.py
```
