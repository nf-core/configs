# nf-core/configs: iPOP-UP Configuration

All nf-core pipelines have been successfully configured for use on the iPOP-UP cluster.

To use, run the pipeline with `-profile ipop_up`. This will download and launch the [`ipop_up.config`](../conf/ipop_up.config) which has been pre-configured with a setup suitable for the iPOP-UP cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Request an account

You will need an account to use iPOP-UP HPC cluster in order to run the pipeline, please refer to [https://parisepigenetics.github.io/bibs/cluster/ipopup/](https://parisepigenetics.github.io/bibs/cluster/ipopup/#/cluster/).

## Running the workflow on the iPOP-UP cluster

Guidelines to start nf-core workflows are provided at [https://parisepigenetics.github.io/bibs/edctools/workflows/nf-cores](https://parisepigenetics.github.io/bibs/edctools/workflows/nf-cores/#/edctools/).

In brief, Nextflow is installed on the iPOP-UP cluster and you need to activate it like this:

```bash
module load nextflow
```

Nextflow manages each process as a separate job that is submitted to the cluster by using the sbatch command.
Nextflow shouldn't run directly on the submission node but on a compute node. We recommand using a sbatch script:

> nfcore-atac.sh

```bash
#!/bin/bash
#SBATCH --partition=ipop-up
#SBATCH --mem=4G

module purge
export JAVA_LD_LIBRARY_PATH=/shared/software/conda/envs/nextflow-21.04.0/lib/server
export JAVA_HOME=/shared/software/conda/envs/nextflow-21.04.0
module load nextflow/21.04.0

nextflow run nf-core/atacseq  -profile ipop_up -params-file nf-params.json
```

Launch on the cluster with sbatch:

```bash
sbatch nfcore-atac.sh
```

### Test dataset

nf-core provides some test for each workflow:

```bash
#!/bin/bash
#SBATCH --partition=ipop-up
#SBATCH --mem=4G

module purge
export JAVA_LD_LIBRARY_PATH=/shared/software/conda/envs/nextflow-21.04.0/lib/server
export JAVA_HOME=/shared/software/conda/envs/nextflow-21.04.0
module load nextflow/21.04.0

nextflow run nf-core/atacseq  -profile ipop_up,test
```

## Databanks

A local copy of several genomes are available in `/shared/banks/` directory.
