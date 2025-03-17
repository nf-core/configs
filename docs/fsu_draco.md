# nf-core/configs: PROFILE Configuration

All nf-core pipelines have been successfully configured for use on the Draco HPC at the [Friedrich Schiller University (FSU), Jena](https://www.uni-jena.de/).

To use, run the pipeline with `-profile fsu_draco`. This will download and launch the [`fsu_draco.config`](../conf/fsu_draco.config) which has been pre-configured with a setup suitable for the FSU Draco cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Before running the pipeline you will need to install Nextflow into a Conda environment and activate it for each job submission. For that, first activate Conda using the environment module system on Draco HPC and create a new Conda environment. Also, the proxy server for connecting to the internet has to be specified. You can do this by issuing the commands below:

```bash
## Create a Conda environment for using Nextflow
module load anaconda3/
conda create -n nextflow -c bioconda nextflow

## Specify the cluster's proxy server connection to use for Nextflow.
## You can use below lines for your sbatch script.
export NXF_OPTS='-Dhttp.proxyHost=http://internet4nzm.rz.uni-jena.de:3128 -Dhttps.proxyHost=http://internet4nzm.rz.uni-jena.de:3128'

## Activate the Conda environment to have nextflow available. 
eval "$(conda shell.bash hook)"
conda activate nextflow

## Run your pipeline now like:
## nextflow run <pipeline name> -profile fsu_draco <parameters>

conda deactivate
```

Singularity is installed on all nodes. Feel free to read about additional mount points/file systems of Draco HPC to use for example for cache directories in [this tutorial](https://zaki-eah.gitpages.uni-jena.de/informationssammlung/Tutorials/HPC_HandsOn/#14-filesystems).

Example sbatch script specifying the `long` partition which is suited for jobs that run for up to 14 days (e.g. the long-running Nextflow manager job which spawns jobs to the compute nodes):

```
#!/bin/bash

#SBATCH --job-name=funcscan
#SBATCH --time=96:00:00
#SBATCH --ntasks=1          # num of processes/MPI
#SBATCH --cpus-per-task=8   # each MPI gets 40 CPUs
#SBATCH --mem=16GB
#SBATCH --partition=long
#SBATCH --error=funcscan.err

export NXF_OPTS='-Dhttp.proxyHost=http://internet4nzm.rz.uni-jena.de:3128 -Dhttps.proxyHost=http://internet4nzm.rz.uni-jena.de:3128'

eval "$(conda shell.bash hook)"

conda activate nextflow 

nextflow run nf-core/funcscan \
       -r 2.1.0 \
       -profile fsu_draco,test \
       --outdir ./results/ \

conda deactivate
```

:::note
You will need an account and VPN access to use the Draco HPC cluster in order to run the pipeline. If in doubt contact IT.
:::

:::note
Nextflow will need to submit the jobs via the job scheduler SLURM to the Draco HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
:::

:::note
Note: All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully (or use `cleanup = true` in a custom configuration file) because it can get quite large and all of the main output files will be saved in the `results/` directory anyway.
:::