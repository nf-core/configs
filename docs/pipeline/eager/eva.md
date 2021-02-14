# nf-core/configs: eva eager specific configuration

Extra specific configuration for eager pipeline

## Usage

To use, run the pipeline with `-profile eva`.

This will download and launch the eager specific [`eva.config`](../../../conf/pipeline/eager/eva.config) which has been pre-configured with a setup suitable for the MPI-EVA cluster.

Example: `nextflow run nf-core/eager -profile eva`

## eager specific configurations for eva

Specific configurations for eva has been made for eager.

### General profiles

- The general MPI-EVA profile runs with default nf-core/eager parameters, but with modifications to account for issues SGE have with Java tools.

#### big_data

- This defines larger base computing resources for when working with very deep sequenced or high-endogenous samples.

### Contextual profiles

#### Human Pop-Gen

- `human`: optimised for mapping of human aDNA reads (i.e. bwa aln defaults as `-l 16500, -n 0.01`)

#### Pathogen

- `pathogen_loose`: optimised for mapping of human aDNA reads (i.e. bwa aln defaults as `-l 16 -n 0.01`)
- `pathogen_strict`: optimised for mapping of human aDNA reads (i.e. bwa aln defaults as `-l 32, -n 0.1`)
