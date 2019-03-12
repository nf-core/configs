# nf-core/configs: MENDEL Configuration

All nf-core pipelines have been successfully configured for use on the MENDEL CLUSTER at the Gregor Mendel Institute (GMI).

To use, run the pipeline with `-profile conda,mendel`. This will download and launch the [`mendel.config`](../conf/mendel.config) which has been pre-configured with a setup suitable for the MENDEL cluster. A Conda environment will be created automatically and software dependencies will be resolved via [bioconda](https://bioconda.github.io/).

Before running the pipeline you will need to load Conda using the environment module system on MENDEL. You can do this by issuing the commands below:

```bash
## Load Nextflow and Conda environment modules
module purge
module load Nextflow
module load Miniconda/4.6.7
```

>NB: You will need an account to use the HPC cluster in order to run the pipeline. If in doubt contact the HPC team.

>NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact the HPC team.
