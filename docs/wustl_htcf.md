# nf-core/configs: WUSTL High Throughput Computing Facility Configuration

Forked from https://github.com/nf-core/configs/blob/master/docs/prince.md

## nf-core pipelines that use this repo

All nf-core pipelines that use this config repo (which is most), can be run on the HTCF. **Before** running a pipeline for the first time, go into an interactive slurm session on a compute node (`srun --pty --time=02:00:00 -c 2`), as the docker image for the pipeline will need to be pulled and converted.

Now, run the pipeline of your choice with `-profile wustl_htcf`. This will download and launch `wustl_htcf.config` which has been pre-configured with a setup suitable for the HTCF cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a singularity image before execution of the pipeline. This step **takes time**!!
An example commandline:

`nextflow run nf-core/<pipeline name> -profile wustl_htcf <additional flags>`

## nf-core pipelines that do not use this repo

If the pipeline has not yet been configured to use this config, then you will have to do it manually.
git clone this repo (https://github.com/nf-core/configs), copy the `wustl_htcf.config` from the conf folder and then you can invoke the pipeline like this:

`nextflow run nf-core/<pipeline name> -c wustl_htcf.config <additional flags>`

> NB: Make sure to keep spack up-to-date, as most workflows will require the most up-to-date stable version of nextflow.
