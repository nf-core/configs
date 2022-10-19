# nf-core/configs: Sheffield Bioinformatics Core Facility ShARC Configuration

## Using the SBC_ShARC Institutional Configuration Profile

To use [`sbc_sharc.config`](../conf/sbc_sharc.config), run nextflow with an nf-core pipeline using `-profile sbc_sharc` (note the single hyphen).

This will download and launch [`sbc_sharc.config`](../conf/sbc_sharc.config) which has been pre-configured with a setup suitable for the ShARC cluster and will automatically load the appropriate pipeline-specific configuration file.

The following nf-core pipelines have been successfully configured for use on the the [University of Sheffield ShARC cluster](https://docs.hpc.shef.ac.uk/en/latest/index.html):

- [nf-co.re/atacseq](https://nf-co.re/atacseq)
- [nf-co.re/chipseq](https://nf-co.re/chipseq)
- [nf-co.re/rnaseq](https://nf-co.re/rnaseq)
- [nf-co.re/sarek](https://nf-co.re/sarek)

When using [`sbc_sharc.config`](../conf/sbc_sharc.config) with the pipelines listed above, the appropriate configuration file from the list below will be loaded automatically:

- [atacseq sbc_sharc.config](../conf/pipeline/atacseq/sbc_sharc.config)
- [chipseq sbc_sharc.config](../conf/pipeline/chipseq/sbc_sharc.config)
- [rnaseq sbc_sharc.config](../conf/pipeline/rnaseq/sbc_sharc.config)
- [sarek sbc_sharc.config](../conf/pipeline/sarek/sbc_sharc.config)

The [`sbc_sharc.config`](../conf/sbc_sharc.config) configuration file might work with other nf-core pipelines as it stands but we cannot guarantee they will run without issue. We will be continuing to create, test and optimise configurations for new pipelines in the future.

## A Note on Singularity Containers

The [`sbc_sharc.config`](../conf/sbc_sharc.config) configuration file supports running nf-core pipelines with Singularity containers; Singularity images will be downloaded automatically before execution of the pipeline.

When you run nextflow for the first time, Singularity will create a hidden directory `.singularity` in your `$HOME` directory `/home/$USER` which has very very limited (10GB) space available. It is therefore a good idea to create a directory somewhere else (e.g., `/data/$USER`) with more room and link the locations. To do this, run the following series of commands:

```shell
# change directory to $HOME
cd $HOME

# make the directory that will be linked to
mkdir /data/$USER/.singularity

# link the new directory with the existing one
ln -s /data/$USER/.singularity .singularity
```
