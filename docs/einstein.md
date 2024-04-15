# nf-core/configs: Novo Nordisk's Einstein Configuration

## Using the Einstein config profile

Before running any pipeline in Novo Nordisk's Einstein cluster, `Nextflow` will need to be installed in the conda environment being used.

To use, run the pipeline with `-profile einstein` (one hyphen).
This will download and launch the [`einstein.config`](../conf/einstein.config) which has been pre-configured with a setup suitable for the einstein server.
It will enable `Nextflow` to manage the pipeline jobs via the `Slurm` job scheduler.

Using this profile, `Docker` image(s) containing required software(s) will be downloaded, and converted to `Singularity` image(s) if needed before execution of the pipeline.

## Below are non-mandatory information on e.g., required modules

Before running the pipeline you will need to have a working Nextflow installation and load Singularity using the environment module system on the Einstein cluster. You can do this by doing for example:

```bash
# Load Singularity environment modules
module load singularity/3.8.1
```
