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

Various tasks will be run inside of Singularity containers and all temp files typically written to `/tmp` and `/var/tmp` are instead written to the path pointed to by the `USER_SCRATCH` environment variable. This means that these temp files are stored in a user specific location, making them inaccessible to other users for pipeline reruns. Some of these temp files can be large and cleanup is also the responsibility of the user.

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.

> NB: You will need an account to use the HPC cluster on Cheaha in order to run the pipeline. If in doubt contact UAB IT Research Computing.</br></br>
> NB: Nextflow will need to submit the jobs via SLURM to the HPC cluster and as such the commands above will have to be executed on one of the login nodes (or alternatively in an interactive partition, but be aware of time limit). If in doubt contact UAB IT Research Computing.</br></br>
> NB: Instead of using `module load Nextflow`, you may instead create a conda environment (e.g: `conda create -p $USER_DATA/nf-core_nextflow_env nf-core nextflow`) if you would like to have a more personalized environment of Nextflow (versions which may not be modules yet) and nf-core tools. This **requires** you to instead do the following:

```bash
module purge
module load Singularity
module load Anaconda3
# change path/enviroment name if according to what you created
conda activate $USER_DATA/nf-core_nextflow_env
```

> NB: while the jobs for each process of the pipeline are sent to the appropriate nodes, the current session must remain active while the pipeline is running. We recommend to use `screen` prior to loading any modules/environments. Once the pipeline starts you can detach the screen session by typing `Ctrl-a d` so you can safely logout of HPC, while keeping the pipeline active (and you may resume the screen session with `screen -r`). Other similar tools (e.g. `tmux`) may also be used.
