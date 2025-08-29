# nf-core/configs: Imperial scflow Specific Configuration

Extra specific configuration for the scflow pipeline

## Usage

To use, run the pipeline with `-profile imperial` or `-profile imperial_mb`.

This will download and launch the scflow specific [`imperial.config`](../../../conf/pipeline/scflow/imperial.config) which has been pre-configured with a setup suitable for the Imperial HPC cluster.

Example: `nextflow run nf-core/scflow -profile imperial`

## scflow specific configurations for Imperial

Specific configurations for Imperial have been made for scflow.

- Singularity `enabled` and `autoMounts` set to `true`
- Singularity `cacheDir` path set to an RDS location
- Singularity `runOptions` path set to bind (`-B`) RDS paths with container paths.
- Params `ctd_folder` set to an RDS location.
- Parms `ensembl_mappings` set to an RDS location.
