# nf-core/configs: binac ampliseq specific configuration

Extra specific configuration for the ampliseq pipeline.

## Usage

To use, run the pipeline with `-profile binac`.

This will download and launch the ampliseq specific [`binac.config`](../../../conf/pipeline/ampliseq/binac.config) which has been pre-configured with a setup suitable for the BINAC cluster.

Example: `nextflow run nf-core/ampliseq -profile binac`

## ampliseq specific configurations for binac

Specific configurations for BINAC has been made for ampliseq.

- Specifies the `TZ` `ENV` variable to be `Europe/Berlin` to fix a QIIME2 issue
