# nf-core/configs: ABiMS Configuration

All nf-core pipelines have been successfully configured for use on [the ABiMS cluster](https://abims-sbr.gitlab.io/cluster/doc/).

To use, run the pipeline with `-profile abims`. This will download and launch the [`abims.config`](../conf/abims.config) which has been pre-configured with a setup suitable for the ABiMS cluster.

## Request an account

You will need an account to use the HPC cluster on ABiMS in order
to run the pipeline. If in doubt see [https://my.sb-roscoff.fr](https://my.sb-roscoff.fr).

## Running the workflow on the ABiMS cluster

Nextflow is installed on the ABiMS cluster.

### Launch it using `srun`

You need to activate it like this:

```bash
module load nextflow slurm-drmaa graphviz
```

Nextflow manages each process as a separate job that is submitted to the cluster by using the sbatch command in background.
Even if the job won't run directly on the login node, please launch Nextflow on a compute node:

```bash
# Load the dependencies if not done before
module load nextflow slurm-drmaa graphviz

# Run Nextflow, it will submit the jobs with the resources needed on the cluster
srun nextflow run nf-core/rnaseq -r 3.10.1 -profile abims ...

# To launch in background
sbatch --wrap "nextflow run nf-core/rnaseq -r 3.10.1 -profile abims ..."
```

### Or write a `sbatch` script

> nfcore-rnaseq.sh

```bash
#!/bin/bash
#SBATCH -p fast
#SBATCH --mem=4G

module load nextflow slurm-drmaa graphviz
nextflow run nf-core/rnaseq -r 3.10.1 -profile abims ...
```

Launch on the cluster with sbatch:

```bash
sbatch nfcore-rnaseq.sh
```

### Hello, world

nf-core provides some test for each workflow:

```bash
module load nextflow slurm-drmaa graphviz
srun nextflow run nf-core/rnaseq -r 3.10.1 -profile abims,test
```

## Singularity images mutualized directory

To reduce the disk usage, nf-core images can be stored in a mutualized directory: `/shared/software/singularity/images/nf-core/`

The `abims` profil includes the dedicade environment variable `NXF_SINGULARITY_CACHEDIR` to indicate the cache directory to nextflow.

If you need more images, please contact the [support team](https://abims-sbr.gitlab.io/cluster/doc/support/)

## Databanks

A local copy of several genomes are available in `/shared/bank/` directory.
