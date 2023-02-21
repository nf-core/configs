# nf-core/configs: Super Computing Wales configuration

A base configuration file for running nf-core pipelines has been set up for use with [Super Computing Wales](https://supercomputing.wales) (SCW). To use this profile, the pipeline can be run with the option `-profile scw`, which will download the [`scw.config`](../conf/scw.config) config file. This config file by default runs pipelines using Singularity, and runs all jobs on the _htc_ partition.

To run an nf-core pipeline, you will first need to activate Nextflow. You can do this with the following command:

```bash
module load nextflow
## you might want to load a specific nextflow version for reproducibility - find them under /apps/modules/tools
module avail
module load nextflow/21.10.6
```

## Downloading pipelines for offline use

To download an nf-core pipeline for offline use, you will have to install the nf-core tool in a conda environment:

```bash
wget https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh
bash Mambaforge-Linux-x86_64.sh -b -p /scratch/$USER/mambaforge
eval "$(/scratch/$USER/mambaforge/bin/conda shell.bash hook)"
chmod u+w ~/.bashrc
conda init
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
conda config --set channel_priority strict

mamba create -n nf-core
mamba activate nf-core
mamba install nextflow nf-core
```

By default, Nextflow will download Singularity containers to a cache directory within the pipeline directory. To reduce storage space and to reuse containers between pipelines, you should create a directory on the /scratch partition where the containers will be downloaded and set the environment variable NXF_SINGULARITY_CACHEDIR in your ~/.myenv file:

```bash
mkdir /scratch/$USER/singularity-containers
echo NXF_SINGULARITY_CACHEDIR=/scratch/$USER/singularity-containers >> ~/.myenv
```

Then you can download the pipeline of your choice to run:

```bash
nf-core download pipeline_name
```

The pipeline can then be run with the following:

```bash
nextflow run /path/to/download/nf-core-pipeline/workflow/ -profile scw
```

More detailed instructions are available on the [nf-core website](https://nf-co.re/tools/#downloading-pipelines-for-offline-use).

## Configuring modules to use different partitions

SCW provides a number of different partitions for different use cases. By default this config file uses HTC, but it is simple to change this for specific modules. Simply create a new config file, and specify a new `queue` for each module you wish to change. For example, to run SPADEs on the `highmem` partition in the nf-core/mag pipeline, create a config file (e.g. `pipeline_options.config`) with the following:

```
process {
  withName: SPADES {
    cpus = 40
    memory = 360.GB
    queue = "highmem"
  }
```

And specify this config when running the pipeline with `-c pipeline_options.config`
