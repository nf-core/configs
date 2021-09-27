# nf-core/configs: Hasta Configuration

## Using the Hasta config profile

Before running the pipeline `Nextflow` will need to be install in the conda environment being used.

To use, run the pipeline with `-profile hasta` (one hyphen).
This will download and launch the [`hasta.config`](../conf/hasta.config) which has been pre-configured with a setup suitable for the hasta servers.
It will enable `Nextflow` to manage the pipeline jobs via the `Slurm` job scheduler.
Using this profile, `Docker` image(s) containing required software(s) will be downloaded, and converted to `Singularity` image(s) if needed before execution of the pipeline.

Recent version of `Nextflow` also support the environment variable `NXF_SINGULARITY_CACHEDIR` which can be used to supply images. A use case: `NXF_SINGULARITY_CACHEDIR=/path/to/images; export NXF_SINGULARITY_CACHEDIR` before running the pipeline.

## Development and production config

Each user on hasta has a priority based on their allocated team, either development or production. To enable this when submitting a job to Slurm, submit with `-profile hasta,dev_prio` or `-profile hasta,prod_prio`. This overwrites certain parts of the config and submits the job based on different priorities.
