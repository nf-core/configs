# nf-core/configs: GIS Aquila Configuration

All nf-core pipelines have been successfully configured for use on the cluster of the GIS (Genome Institute of Singapore (Aquila)).

To use, run the pipeline with `-profile gis`. This will download and launch the [`gis.config`](../conf/gis.config) which has been pre-configured with a setup suitable for the GIS Aquila cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## How to use on GIS core

Before running the pipeline you will need to load Nextflow using the environment module system on GIS Aquila. You can do this by issuing the commands below:

```bash
# Login to a compute node
srun --pty bash

## Load Nextflow and Singularity environment modules
module purge
source /mnt/projects/rpd/rc/init.2017-04
module load miniconda3


# Run a nextflow pipeline with dependencies bundled in a conda environment
set +u
source activate nfcore-rnaseq-1.0dev
set -u

# Run a downloaded/git-cloned nextflow workflow from
nextflow run \\
nf-core/workflow \\
-resume \\
-profile gis \\
--email my-email@example.org  \\
-c my-specific.config
...


# Or use the nf-core client
nextflow run nf-core/rnaseq ...

```

## Databanks

A local copy of several genomes are available in `/mnt/projects/rpd/genomes.testing/S3_igenomes/` directory.

> NB: You will need an account to use the HPC cluster on GIS in order to run the pipeline. If in doubt contact IT or go to [Andreas Wilm](https://github.com/andreas-wilm)
