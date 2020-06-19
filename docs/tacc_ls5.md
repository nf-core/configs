# nf-core/configs: TACC LS5 Configuration

All nf-core pipelines have been successfully configured for use on the Lonestar 5(LS5) HPC cluster at the [Texas Advanced Computing Center (TACC)](https://www.tacc.utexas.edu/).

To use, run the pipeline with `-profile tacc_ls5`. This will download and launch the [`tacc_ls5.config`](../conf/tacc_ls5.config) which has been pre-configured with a setup suitable for the LS5 HPC cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Before running the pipeline you will need to load Singularity using the environment module system on ls5. You can do this by issuing the commands below:

```bash
## Singularity environment modules
module restore
module load tacc
```

:warning: Due to the resource limit of users on the login nodes, and not being able to submit jobs from compute nodes you have to call the `NXF_OPTS` in the same line as the nextflow command. All of this even though the ulimit claims 8GB of virtual memory. Setting it in your `.bashrc` causes it to still fail. It may also run out of memory while building the singularity image and you can download it before running. For how to do that see the  [nf-core offline docs](https://nf-co.re/usage/offline)

```bash
NXF_OPTS='-Xms2G -Xmx2G -Xss228K' nextflow run nf-core/... -profile tacc_ls5
```

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.

>NB: You will need an account to use the HPC cluster on TACC in order to run the pipeline. If in doubt contact TACC.
>NB: Nextflow will need to submit the jobs via SLURM to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt open a consulting ticket in the TACC User Portal.
