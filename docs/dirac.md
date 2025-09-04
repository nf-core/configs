# nf-core/configs: Novo Nordisk's Dirac Configuration

## Using the Dirac config profile

Before running any pipeline in Novo Nordisk's Dirac cluster, `Nextflow` will need to be loaded as a module
(`module load nextflow`) or installed in the conda environment being used.

To use, run the pipeline with `-profile dirac` (one hyphen).
This will download and launch the [`dirac.config`](../conf/dirac.config)
which has been pre-configured with a setup suitable for the Dirac server.
It will enable `Nextflow` to manage the pipeline jobs via the `Slurm` job scheduler.

Using this profile, Docker image(s) containing required software(s) will be downloaded
from the in-house Docker repository, and converted to `Apptainer` image(s) if needed before execution of the pipeline.

## Below are information on required modules on HPC and Nextflow environment variables

Before running the pipeline you will need to have a working Nextflow installation
and load apptainer using the environment module system on the Dirac cluster. You can do this by doing for example:

```bash
# Load apptainer environment modules
module load nextflow
module load apptainer
```

It is best practices to set the environment variables when running on the HPC,
by adding the following to your `~./bashrc` profile:

```bash
export NXF_CACHE_DIR=/scratch/${USER}
export NXF_WORK=/scratch/${USER}
export APPTAINER_CACHEDIR=/scratch/${USER}
export NXF_APPTAINER_CACHEDIR=$APPTAINER_CACHEDIR
```
