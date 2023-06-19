# nf-core/configs: Crick (CAMP HPC) Configuration

All nf-core pipelines have been successfully configured for use on the CAMP HPC cluster at the [The Francis Crick Institute](https://www.crick.ac.uk/).

To use, run the pipeline with `-profile crick`. This will download and launch the [`crick.config`](../conf/crick.config) which has been pre-configured with a setup suitable for the CAMP HPC cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Before running the pipeline you will need to load Nextflow and Singularity using the environment module system on CAMP. Please check the main README of the pipeline to make sure that the version of Nextflow is compatible with that required to run the pipeline. You can do this by issuing the commands below:

```bash
## Load Nextflow and Singularity environment modules
module purge
module load Nextflow/22.10.3
module load Singularity/3.6.4
```

A local copy of the [AWS-iGenomes](https://github.com/ewels/AWS-iGenomes) resource has been made available on CAMP so you should be able to run the pipeline against any reference available in the `igenomes.config` specific to the nf-core pipeline. You can do this by simply using the `--genome <GENOME_ID>` parameter. Some of the more exotic genomes may not have been downloaded onto CAMP so have a look in the `igenomes_base` path specified in [`crick.config`](../conf/crick.config), and if your genome of interest is not present please contact [BABS](mailto:bioinformatics@crick.ac.uk).

Alternatively, if you are running the pipeline regularly for genomes that arent available in the iGenomes resource, we recommend creating a config file with paths to your reference genome indices (see [`reference genomes documentation`](https://nf-co.re/usage/reference_genomes) for instructions).

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.

> NB: You will need an account to use the HPC cluster on CAMP in order to run the pipeline. If in doubt contact IT.
> NB: Nextflow will need to submit the jobs via SLURM to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.

## Pipeline specific profiles

Specific pipeline profiles exist for the following pipelines, and will be automatically loaded when supplying `-profile crick` to your command:

- eager
