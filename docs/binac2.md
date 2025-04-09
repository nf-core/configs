# nf-core/configs: BinAC 2 Configuration

All nf-core pipelines have been successfully configured for use on the BinAC 2 at the University of Tübingen.

To use, run the pipeline with `-profile binac2`. This will download and launch the [`binac2.config`](../conf/binac2.config) which has been pre-configured with a setup suitable for the BinAC 2 cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Below are non-mandatory information e.g. on modules to load etc

Before running the pipeline you will need to install Nextflow on BinAC 2. You can do this by issuing the commands below:

```bash
## Load Miniforge and create a Conda environment with Nextflow installed
module purge
module load devel/miniforge
conda create --name nextflow nextflow
conda activate nextflow
```

Apptainer is installed on every login and compute node.

## Below are non-mandatory information on iGenomes specific configuration

A local copy of the iGenomes resource has been made available on BinAC 2 so you should be able to run the pipeline against any reference available in the `igenomes.config` specific to the nf-core pipeline.
You can do this by simply using the `--genome <GENOME_ID>` parameter.

:::note
You will need an account on BinAC 2 in order to run the pipeline. If in doubt contact IT.
:::

:::note
Nextflow will need to submit the jobs via the SLURM job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
:::
