# nf-core/configs: ChIP-Seq Specific Configuration - Sheffield Bioinformatics Core Facility ShARC

Specific configuration for [nf-co.re/chipseq](https://nf-co.re/chipseq) pipeline

## Usage

To use, run nextflow with the pipeline using `-profile sbc_sharc` (note the single hyphen).

This will download and launch the chipseq specific [`sbc_sharc.config`](../../../conf/pipeline/chipseq/sbc_sharc.config) which has been pre-configured with a setup suitable for the [University of Sheffield ShARC cluster](https://docs.hpc.shef.ac.uk/en/latest/index.html) and will automatically load the appropriate pipeline-specific configuration file.

Example: `nextflow run nf-core/chipseq -profile sbc_sharc`
