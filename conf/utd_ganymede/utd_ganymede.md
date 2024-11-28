# nf-core/configs: UTD Ganymede Configuration

All nf-core pipelines have been successfully configured for use on the [Ganymede HPC cluster](https://docs.circ.utdallas.edu/user-guide/systems/ganymede.html) at [The Univeristy of Texas at Dallas](https://www.utdallas.edu/).

To use, run the pipeline with `-profile utd_ganymede`. This will download and launch the [`utd_ganymede.config`](../conf/utd_ganymede.config) which has been pre-configured with a setup suitable for Ganymede.

Before running the pipeline you will need to load Singularity using the environment module system on Ganymede. You can do this by issuing the commands below:

```bash
## Singularity environment modules
module purge
module load singularity
```

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.

> [!NOTE]
> You will need an account to use the HPC cluster on Ganymede in order to run the pipeline.
> https://docs.circ.utdallas.edu/user-guide/accounts/index.html
> Nextflow will need to submit the jobs via SLURM to the HPC cluster and as such the commands above will have to be executed on the login node.
> If in doubt contact CIRC.
