# nf-core/configs: Unity HPC Configuration

All nf-core pipelines have been successfully configured for use on the Unity HPC.

To use, run the pipeline with `-profile unity`. This will download and launch the [`unity.config`](../conf/unity.config) which has been pre-configured with a setup suitable for the UNITY cluster. Using this profile, an Apptainer image containing all of the required software will be downloaded, and converted to an Apptainer image before execution of the pipeline.

## Running the pipeline

Before running the pipeline you will need to load Nextflow and Apptainer using the environment module system on UNITY CLUSTER. You can do this by issuing the commands below:

```bash
## Load Nextflow and Apptainer environment modules
module purge
module load nextflow/24.04.3
module load apptainer/latest

nextflow run <pipeline_name> -profile unity
```

Apptainer module will look for a cache directory with the name `.apptainer/cache` in your `/home` or `/work` directory. Please create the cache directory in `/work/pi_<pi_name>/.apptainer/cache` or `/work/pi_<pi_name>/<username>/.apptainer/cache` to prevent apptainer filling your HOME directory.

## iGenome database

A local copy of the iGenomes resource has been made available on UNITY CLUSTER so you should be able to run a pipeline supporting this against any reference available in the `igenomes.config` specific to the nf-core pipeline.
You can do this by simply using the `--genome <GENOME_ID>` parameter.

:::note
You will need an account to use the HPC cluster on UNITY CLUSTER in order to run the pipeline. If in doubt contact `hpc@umass.edu`.
:::
