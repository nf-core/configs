# nf-core/configs: CRUK-MI sarek specific configuration

Extra specific configuration for sarek pipeline

## Usage

To use, run the pipeline with `-profile crukmi`.

This will download and launch the sarek specific [`crukmi.config`](../../../conf/pipeline/sarek/munin.config) which has been pre-configured with a setup suitable for the Cancer Research UK Manchester Institute cluster (phoenix).

Example: `nextflow run nf-core/sarek -profile crukmi`

## Sarek specific configurations for CRUK-MI

Specific configurations for `CRUK-MI` has been made for sarek.

- Initial requested resources for SAMTOOLS_MPILEUP are only 5GB and 1 core.
