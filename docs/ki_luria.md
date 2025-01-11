# nf-core/configs: KI at MIT Luria Configuration

All nf-core pipelines have been successfully configured for use on the [KI at MIT Luria Cluster](https://igb.mit.edu/computing-resources/luria-cluster).

To use, run the pipeline with `-profile ki_luria`. This will download and launch the [`ki_luria.config`](../conf/ki_luria.config) which has been pre-configured with a setup suitable for the Luria Cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Below are non-mandatory information e.g. on modules to load etc

Before running the pipeline you will need to activate the Nextflow conda environment and load Singularity using the environment module system on Luria Cluster. You can do this by issuing the commands below:

```bash
module add miniconda3/v4
source /home/software/conda/miniconda3/bin/condainit
conda activate /home/charliew/.conda/envs/nf-core_Oct24
module add singularity/3.10.4
```

> NB: You will need an account to use the HPC cluster on Lura in order to run the pipeline.
> NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes.
