# nf-core/configs: Engaging mag specific configuration

Extra specific configuration for mag pipeline

## Usage

To use, run the pipeline with `-profile engaging`.

This will download and launch the mag specific [`engaging.config`](../../../conf/pipeline/mag/engaging.config) which has been pre-configured to use a different partition on the Engaging cluster for the assembly steps.

Example: `nextflow run nf-core/mag -profile engaging`

## mag specific configurations for engaging

Specific configurations for engaging has been made for mag, primarily adjusting the parition that is used for the assembly steps. This is done so that more computational resources can be used for the intensive assembly steps.
