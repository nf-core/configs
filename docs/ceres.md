# nf-core/configs: USDA SCINet Ceres HPC Configuration

> **NB:** You will need an [account](https://scinet.usda.gov/about/signup) to use the Ceres cluster to run the pipeline.

All nf-core pipelines have been successfully configured for use on the Ceres cluster at the United States Department of Agriculture (USDA) Agricultural Research Service (ARS) Scientific Computing Network (SCINet).

To use, run the pipeline with `-profile ceres`. The will download and launch the [`ceres.config`](../conf/ceres.config) which has been pre-configured with a setup suitable for the Ceres cluster. Using this profile will configure Nextflow to download all required software as Singularity images as they are required in the pipeline.

Before running the pipeline, you will need to load Singularity and Nextflow using the environment module system on Ceres. You can do this by issuing the command:

```bash
module load singularity/3.10.2
module load nextflow/22.04.3
```

## File storage recommendations

All of the intermediate files required to run the pipeline will be stored in the `work/` directory by default. As [`/project`](https://scinet.usda.gov/guide/storage/#project-directories) directories have a limited quota, it is recommended to store raw data in `/project` and use Nextflow's [`-work-dir`](https://nextflow.io/docs/latest/cli.html#run) parameter to place intermediate files in a [`/90daydata`](https://scinet.usda.gov/guide/storage/#large-short-term-storage) directory instead, e.g.

```bash
nextflow run nf-core/mag -profile ceres,test -w /90daydata/shared/$USER/.nextflow/work
```

Storage in `/90daydata` does not count against your account, but it is deleted 90 days after creation, giving an effective short-term cache for intermediate files in case you wish to re-run a pipeline. All of the main output files will be saved to the directory you specify with `--outdir`.

> **NB:** Nextflow will need to submit the jobs via SLURM to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt, contact [VRSC](https://scinet.usda.gov/support/vrsc/).
