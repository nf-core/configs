# nf-core/configs: Cambridge HPC Configuration

All nf-core pipelines have been successfully configured for use on the Cambridge HPC cluster at the [The University of Cambridge](https://www.cam.ac.uk/).  
To use, run the pipeline with `-profile cambridge`. This will download and launch the [`cambridge.config`](../conf/cambridge.config) which has been pre-configured
with a setup suitable for the Cambridge HPC cluster. Using this profile, either a docker image containing all of the required software will be downloaded,
and converted to a Singularity image or a Singularity image downloaded directly before execution of the pipeline.

### Install Nextflow

The latest version of Nextflow is not installed by default on the Cambridge HPC cluster CSD3. You will need to install it into a directory you have write access to.
Follow [these instructions](https://www.nextflow.io/docs/latest/getstarted.html#) from the Nextflow documentation.

```
# move to desired directory on HPC
cd /home/<username>/path/to/dir
# get the newest version
wget -qO- https://get.nextflow.io | bash
```
Alternatively, install Nextflow with conda

```
module load miniconda/3

# set up Bioconda according to the Bioconda documentation, notably setting up channels
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge

# create the environment env_nf, and install the tool nextflow
conda create --name env_nf nextflow

# activate the environment containing nextflow
conda activate env_nf

# once done with the environment, deactivate
conda deactivate
```

### Obtain updated java version

The java version on the HPC needs updating.

```
cd ~/
wget https://download.oracle.com/java/20/latest/jdk-20_linux-x64_bin.tar.gz
tar xvfz jdk-20_linux-x64_bin.tar.gz
# add these lines to .bashrc
export JAVA_HOME=/home/ef479/jdk-20.0.1
export PATH=/home/ef479/jdk-20.0.1/bin:$PATH
# Once above is done “java --version” should return:
java --version
java 20.0.1 2023-04-18
```

### Set up Singularity

Singularity allows the use of containers. You also needs to make a directory to store Singularity cache.

```
module load singularity
# make a directory for the cache
mkdir -p /home/<username>/rds/hpc-work/path/to/cache/dir
```

### Run Nextflow

Here is an example with the nf-core pipeline sarek ([read documentation here](https://nf-co.re/sarek/3.3.2)).
The user includes the project name, the node and the cache directory for Singularity.

```
# create a working directory in rds/hpc-work
mkdir /home/<username>/rds/hpc-work/dir/to/test
cd /home/<username>/rds/hpc-work/dir/to/test

# Launch the nf-core pipeline for a test database
# with the Cambridge profile
nextflow run nf-core/sarek -profile test,cambridge.config --partition "cclake" --project "NAME-SL3-CPU" --cacheDir "/home/<username>/rds/hpc-work/path/to/cache/dir" --outdir nf-sarek-test
```

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline
has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.

> NB: You will need an account to use the Cambridge HPC cluster in order to run the pipeline. If in doubt contact IT.
> NB: Nextflow will need to submit the jobs via SLURM to the Cambridge HPC cluster and as such the commands above will have to be executed on one of the login
> nodes. If in doubt contact IT.
