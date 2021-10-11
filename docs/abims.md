# nf-core/configs: ABiMS Configuration

All nf-core pipelines have been successfully configured for use on the ABiMS cluster.

To use, run the pipeline with `-profile abims`. This will download and launch the [`abims.config`](../conf/abims.config) which has been pre-configured with a setup suitable for the ABiMS cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Request an account

You will need an account to use the HPC cluster on ABiMS in order
to run the pipeline. If in doubt see [http://abims.sb-roscoff.fr/account](http://abims.sb-roscoff.fr/account).

## Running the workflow on the ABiMS cluster

Nextflow is installed on the ABiMS cluster.

You need to activate it like this:

```bash
module load nextflow slurm-drmaa graphviz
```

Nextflow manages each process as a separate job that is submitted to the cluster by using the sbatch command.
Nextflow shouldn't run directly on the submission node but on a compute node. Run nextflow from a compute node:

```bash
# Load the dependencies if not done before
module load nextflow slurm-drmaa graphviz

# Run a downloaded/git-cloned nextflow workflow from
srun nextflow run \
/path/to/nf-core/workflow \
-profile abims \
--email my-email@example.org  \
-c my-specific.config
...

# Or use let nf-core client download the workflow
srun nextflow run nf-core/rnaseq -profile abims ...

# To launch in background
sbatch --wrap "nextflow run nf-core/rnaseq -profile abims ..."
```

Or write a sbatch script

> nfcore-rnaseq.sh

```bash
#!/bin/bash
#SBATCH -p fast
#SBATCH --mem=4G

module load nextflow slurm-drmaa graphviz
nextflow run nf-core/rnaseq -profile abims ...
```

Launch on the cluster with sbatch:

```bash
sbatch nfcore-rnaseq.sh
```

### Hello, world

nf-core provides some test for each workflow:

```bash
module load nextflow slurm-drmaa graphviz
nextflow run nf-core/rnaseq -profile abims,test
```

## Singularity images mutualized directory

To reduce the disk usage, nf-core images can be stored in a mutualized directory: `/shared/software/singularity/images/nf-core/`

The environment variable `NXF_SINGULARITY_CACHEDIR: /shared/data/cache/nextflow` will indicate this directory to nextflow.

## Databanks

A local copy of several genomes are available in `/shared/bank/` directory.
