# nf-core/configs: WUSTL High Throughput Computing Facility Configuration

Forked from the prince configuration.

<!-- https://github.com/nf-core/configs/blob/master/docs/prince.md -->

## nf-core pipelines that use this repo

All nf-core pipelines that use this config repo (which is most), can be run on the HTCF. **Before** running a pipeline for the first time, go into an interactive slurm session on a compute node (`srun --pty --time=02:00:00 -c 2`), as the docker images for the pipeline will need to be pulled and converted.

Now, run the pipeline of your choice with `-profile wustl_htcf`. This will download and launch `wustl_htcf.config` which has been pre-configured with a setup suitable for the HTCF cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a singularity image before execution of the pipeline. This step **takes time**!!
An example commandline:

```bash
nextflow run nf-core/<pipeline name> -profile wustl_htcf <additional flags>
```

## nf-core pipelines that do not use this repo

If the pipeline has not yet been configured to use the nf-core/configs repository, then you will have to do it manually. Add the following lines to the end of the pipeline's `nextflow.config`

```
// Allow the use of nf-core/configs configuration files
includeConfig "https://raw.githubusercontent.com/nf-core/configs/master/nfcore_custom.config"
```
