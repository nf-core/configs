# nf-core/configs: AWS Tower Demultiplex specific configuration

Extra specific configuration for demultiplex pipeline

## Usage

To use, run the pipeline with `-profile aws_tower`.

This will download and launch the demultiplex specific [`aws_tower.config`](../../../conf/pipeline/demultiplex/aws_tower.config) which has been pre-configured with a setup suitable for AWS batch through tower.

Example: `nextflow run nf-core/demultiplex -profile aws_tower`

## eager specific configurations for eva

Specific configurations for AWS has been made for demultiplex.

### General profiles

- The general AWS Tower profile runs with default nf-core/demultiplex parameters, but with modifications to account file transfer speed and optimized bases2fastq resources.
