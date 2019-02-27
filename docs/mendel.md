# nf-core/configs: MENDEL Configuration

All nf-core pipelines have been successfully configured for use on the MENDEL CLUSTER at the Gregor Mendel Institute (GMI).

To use, run the pipeline with `-profile conda,mendel`. This will download and launch the [`mendel.config`](../conf/mendel.config) which has been pre-configured with a setup suitable for the MENDEL cluster. A Conda environment will be created automatically and software dependencies will be downloaded from ['bioconda'](https://bioconda.github.io/).

Theoretically, using `-profile singularity,mendel` would download a docker image containing all of the required software, and convert it to a Singularity image before execution of the pipeline. However, there is a regression in the Singularity deployment on MENDEL which renders containers downloaded from public repositories unusable because they lack the /lustre mountpoint.

If you want to run the pipeline containerized anyway you will have to build the image yourself (on a machine where you have root access) using the provided `Singularity` file in the pipeline repository:

```bash
cd /path/to/pipeline-repository
echo 'mkdir /lustre > Singularity'
singularity build nf-core-methylseq-custom.simg Singularity
```

After you copied the container image to the cluster filesystem, make sure to pass the path to the image to the pipeline with `-with-singularity /path/to/nf-core-methylseq-custom.simg`

Before running the pipeline you will need to load Nextflow and Conda using the environment module system on MENDEL. You can do this by issuing the commands below:

```bash
## Load Nextflow and Conda environment modules
module purge
module load Nextflow
module load Miniconda3 # not needed if using Singularity
```

>NB: You will need an account to use the HPC cluster in order to run the pipeline. If in doubt contact the HPC team.

>NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact the HPC team.
