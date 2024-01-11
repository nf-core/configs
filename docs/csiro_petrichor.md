# nf-core/configs: CSIRO Petrichor HPC Configuration

To run an nf-core pipeline at CSIRO Petrichor HPC, execute with `-profile singularity,csiro_petrichor`. This will download and launch the [`csiro_petrichor.config`](../conf/csiro_petrichor.config) which has been pre-configured with a setup suitable for the CSIRO Petrichor HPC cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Access to CSIRO Petrichor HPC

Please be aware that you will need to have an active CSIRO HPC User Account in order to use this infrastructure. If you need help getting started, please see the [guide for new users](https://confluence.csiro.au/x/JJEPG).

## Launch an nf-core pipeline on Petrichor

### Prerequisites

Before running the pipeline you will need to load Nextflow and Singularity, both of which are globally installed modules. You can do this by running the commands below:

```bash
module purge
module load nextflow singularity
```

### Cluster considerations

Before running an nf-core pipeline you will need to set your project code as a Slurm environment variable:

```bash
export SBATCH_ACCOUNT=OD-012345
```

You can retrieve a list of projects your ident is associate with using:

```bash
get_project_codes
```

### Execution command

```bash
module load nextflow
module load singularity

nextflow run <nf-core_pipeline>/main.nf \
  -profile singularity,csiro_petrichor \
  <additional flags>
```
