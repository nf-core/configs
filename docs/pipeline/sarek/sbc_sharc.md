# nf-core/configs: Sarek Specific Configuration - Sheffield Bioinformatics Core Facility ShARC

Specific configuration for [nf-co.re/sarek](https://nf-co.re/sarek) pipeline

## Usage

To use, run nextflow with the pipeline using `-profile sbc_sharc` (note the single hyphen).

This will download and launch the sarek specific [`sbc_sharc.config`](../../../conf/pipeline/sarek/sbc_sharc.config) which has been pre-configured with a setup suitable for the [University of Sheffield ShARC cluster](https://docs.hpc.shef.ac.uk/en/latest/index.html) and will automatically load the appropriate pipeline-specific configuration file.

Example: `nextflow run nf-core/sarek -profile sbc_sharc`
