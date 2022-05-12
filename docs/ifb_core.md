# nf-core/configs: IFB core Configuration

All nf-core pipelines have been successfully configured for use on the cluster of the IFB (Institut Francais de Bioinformatique).

To use, run the pipeline with `-profile ifb_core`. This will download and launch the [`ifb_core.config`](../conf/ifb_core.config) which has been pre-configured with a setup suitable for the IFB core cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## How to use on IFB core

Here is [the link to the cluster's documentation](https://ifb-elixirfr.gitlab.io/cluster/doc/quick-start/).
Before running the pipeline you will need to load Nextflow and other dependencies using the environment module system on IFB core. You can do this by issuing the commands below:

```bash
# Login to a compute node
srun --pty bash

## Load Nextflow and Singularity environment modules
module purge
module load nextflow
module load singularity
module load openjdk


# Run a downloaded/git-cloned nextflow workflow from
nextflow run \\
nf-core/workflow \\
-resume
-profile ifb_core \\
--email my-email@example.org  \\
-c my-specific.config
...


# Or use the nf-core client
nextflow run nf-core/rnaseq ...

```

## Databanks

A local copy of several genomes are available in `/shared/bank` directory. See
our [databank page](https://ifb-elixirfr.gitlab.io/cluster/doc/banks/)
to search for your favorite genome.

> NB: You will need an account to use the HPC cluster on IFB core in order to run the pipeline. If in doubt contact IT or go to [account page](https://my.cluster.france-bioinformatique.fr/manager2/login).
