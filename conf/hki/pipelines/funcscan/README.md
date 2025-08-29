# nf-core/configs: hki funcscan specific configuration

Extra specific configuration for the funcscan pipeline

## Usage

To use, run the pipeline with `-profile hki`.

This will download and launch the HKI specific [`hki.config`](../../../conf/pipeline/funcscan/hki.config) which has been pre-configured with a setup suitable for the MPI-EVA cluster.

Example: `nextflow run nf-core/funcscan -profile hki`

## funcscan specific configurations for hki

No specific settings are applied for this profile currently - it is a 'dummy' profile to allow activation of pipeline-specific institutional profiles in the funcscan pipeline.
