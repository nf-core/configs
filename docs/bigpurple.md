# nf-core/configs: BigPurple Configuration

## nf-core pipelines that use this repo

All nf-core pipelines that use this config repo (which is most), can be run on BigPurple. **Before** running a pipeline for the first time, go into an interactive slurm session on a compute node (`srun --pty --time=02:00:00 -c 2`), as the docker image for the pipeline will need to be pulled and converted. Once in the interactive session:

```bash
module load singularity/3.1
module load squashfs-tools/4.3
```

Now, run the pipeline of your choice with `-profile bigpurple`. This will download and launch the bigpurple.config which has been pre-configured with a setup suitable for the BigPurple cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a singularity image before execution of the pipeline.
An example commandline:

`nextflow run nf-core/<pipeline name> -profile bigpurple <additional flags>`

## nf-core pipelines that do not use this repo

If the pipeline has not yet been configured to use this config, then you will have to do it manually.
git clone this repo, copy the `bigpurple.config` from the conf folder and then you can invoke the pipeline like this:

`nextflow run nf-core/<pipeline name> -c bigpurple.config <additional flags>`

> NB: You will need an account to use the HPC cluster BigPurple in order to run the pipeline. If in doubt contact MCIT.
> NB: You will need to install nextflow in your home directory - instructions are on nextflow.io (or ask the writer of this profile). The reason there is no module for nextflow on the cluster, is that the development cycle of nextflow is rapid and it's easy to update yourself: `nextflow self-update`
