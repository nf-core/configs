# University of Washington Hyak Profile for the Department of Pediatrics

All nf-core pipelines have been successfully configured for use on the University of Washington's Hyak cluster, with this profile specific to the Department of Pediatrics partition.

To use, run the pipeline with `-profile uw_hyak_pedslabs`. This will download and launch the [`uw_hyak_pedslabs.config`](../conf/uw_hyak_pedslabs.config) which has been pre-configured with a setup suitable for the Hyak cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Running the workflow on the Pasteur cluster

Nextflow is not installed by default on Hyak.

- Install Nextflow : [here](https://www.nextflow.io/docs/latest/getstarted.html#)

Nextflow manages each process as a separate job that is submitted to the cluster by using the `sbatch` command.
Nextflow shouldn't run directly on the submission node but on a compute node.

To install and use Nextflow, the following process can be used:

1. Install mamba and create a mamba environment containing nextflow and nf-core

```bash
wget https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh
bash Mambaforge-Linux-x86_64.sh -b -p $HOME/mambaforge
mamba create -n nextflow -c bioconda -c conda-forge python=3.8 nf-core nextflow -y -q
```

2. Run nextflow on a compute node:

```bash
# create a screen
screen -S nextflow
# request a compute node (mem and time requests can be modified)
salloc -A pedslabs -p compute-hugemem -N 1 -c 1 --mem=16GB --time=12:00:00
# load the nextflow environment
mamba activate nextflow
# Run nextflow workflow
nextflow run \\
<nf-core-pipeline-name> \\
-resume
-profile uw_hyak_pedslabs \\
--email <uw-net-id>@uw.edu
```
