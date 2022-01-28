# nf-core/configs: Cheaha (UAB HPC) Configuration

All nf-core pipelines have been successfully configured for use on the Cheaha HPC cluster at the [The University of Alabama at Birmingham](https://www.uab.edu/home/).

To use, run the pipeline with `-profile cheaha`. This will download and launch the [`cheaha.config`](../conf/cheaha.config) which has been pre-configured with a setup suitable for the Cheaha HPC cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Before running the pipeline you will need to load Singularity and Nextflow using the environment module system on Cheaha. You can do this by issuing the commands below:

```bash
## Singularity environment modules
module purge
module load Singularity
module load Nextflow
```

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.

>NB: You will need an account to use the HPC cluster on Cheaha in order to run the pipeline. If in doubt contact UAB IT Research Computing.
>NB: Nextflow will need to submit the jobs via SLURM to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact UAB IT Research Computing.
