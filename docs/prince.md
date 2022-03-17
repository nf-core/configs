# nf-core/configs: Prince Configuration

## nf-core pipelines that use this repo

All nf-core pipelines that use this config repo (which is most), can be run on prince. **Before** running a pipeline for the first time, go into an interactive slurm session on a compute node (`srun --pty --time=02:00:00 -c 2`), as the docker image for the pipeline will need to be pulled and converted.

Now, run the pipeline of your choice with `-profile prince`. This will download and launch the prince.config which has been pre-configured with a setup suitable for the prince cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a singularity image before execution of the pipeline. This step **takes time**!!
An example commandline:

`nextflow run nf-core/<pipeline name> -profile prince <additional flags>`

## nf-core pipelines that do not use this repo

If the pipeline has not yet been configured to use this config, then you will have to do it manually.
git clone this repo, copy the `prince.config` from the conf folder and then you can invoke the pipeline like this:

`nextflow run nf-core/<pipeline name> -c prince.config <additional flags>`

> NB: You will need an account to use the HPC cluster Prince in order to run the pipeline. If in doubt contact the HPC admins.
> NB: Rather than using the nextflow module, I recommend you install nextflow in your home directory - instructions are on nextflow.io (or ask the writer of this profile). The reason this is better than using the module for nextflow on the cluster, is that the development cycle of nextflow is rapid and it's easy to update your installation yourself: `nextflow self-update`.
