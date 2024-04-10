# nf-core/configs: UTD Europa Configuration

All nf-core pipelines have been successfully configured for use on the [Europa HTC cluster](https://docs.circ.utdallas.edu/user-guide/systems/europa.html) at [The Univeristy of Texas at Dallas](https://www.utdallas.edu/).

To use, run the pipeline with `-profile utd_europa`. This will download and launch the [`utd_europa.config`](../conf/utd_europa.config) which has been pre-configured with a setup suitable for Europa.

Before running the pipeline you will need to load Apptainer using the environment module system on Europa. You can do this by issuing the commands below:

```bash
## Singularity environment modules
module purge
module load apptainer
```

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.

> [!NOTE]
> You will need an account to use Europa.
> To join, fill out our short survey at https://utd.link/trecis-lcars-signup.
> Nextflow will need to submit the jobs via SLURM to the HTC cluster and as such the commands above will have to be executed on the login node.
> If in doubt contact CIRC.
