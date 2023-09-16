# nf-core/configs: Sheffield Bioinformatics Core Facility Stanage Configuration

## Using the tuos_stanage Institutional Configuration Profile

To use [`tuos_stanage.config`](../conf/tuos_stanage.config), run nextflow with an nf-core pipeline using `-profile tuos_stanage` (note the single hyphen).

This will download and launch [`tuos_stanage.config`](../conf/tuos_stanage.config) which has been pre-configured with a setup suitable for the ShARC cluster and will automatically load the appropriate pipeline-specific configuration file.

The following nf-core pipelines have been successfully configured for use on the the [University of Sheffield ShARC cluster](https://docs.hpc.shef.ac.uk/en/latest/index.html):

- [nf-co.re/atacseq](https://nf-co.re/atacseq)
- [nf-co.re/chipseq](https://nf-co.re/chipseq)
- [nf-co.re/rnaseq](https://nf-co.re/rnaseq)
- [nf-co.re/sarek](https://nf-co.re/sarek)

When using [`tuos_stanage.config`](../conf/tuos_stanage.config) with the pipelines listed above, the appropriate configuration file from the list below will be loaded automatically:

- [atacseq tuos_stanage.config](../conf/pipeline/atacseq/tuos_stanage.config)
- [chipseq tuos_stanage.config](../conf/pipeline/chipseq/tuos_stanage.config)
- [rnaseq tuos_stanage.config](../conf/pipeline/rnaseq/tuos_stanage.config)
- [sarek tuos_stanage.config](../conf/pipeline/sarek/tuos_stanage.config)

The [`tuos_stanage.config`](../conf/tuos_stanage.config) configuration file might work with other nf-core pipelines as it stands but we cannot guarantee they will run without issue. We will be continuing to create, test and optimise configurations for new pipelines in the future.

## A Note on Singularity Containers

The [`tuos_stanage.config`](../conf/tuos_stanage.config) configuration file supports running nf-core pipelines with Singularity containers; Singularity images will be downloaded automatically before execution of the pipeline.

When you run nextflow for the first time, Singularity will create a hidden directory `.singularity` in your `$HOME` directory `/users/$USER` which has limited (75GB) space available. It may therefore a good idea to create a directory somewhere else (e.g., `/mnt/parscratch/users/$USER`) with more room and link the locations. To do this, run the following series of commands:

```shell
# change directory to $HOME
cd $HOME

# make the directory that will be linked to
mkdir /mnt/parscratch/users/$USER/.singularity

# link the new directory with the existing one
ln -s /mnt/parscratch/users/$USER/.singularity .singularity
```