# nf-core/configs: Crick eager specific configuration

Extra specific configuration for eager pipeline

## Pipeline specific profiles

Specific-pipeline profiles exist for the following pipelines, and will be automatically loaded when supplying `-profile crick` to your command:

- eager

## Usage

To use, run the pipeline with `-profile crick`.

This will download and launch the eager specific [`crick.config`](../../../conf/pipeline/eager/crick.config) which is adapted to data generated at the Crick and
processed on the Crick's HPC.

Example: `nextflow run nf-core/eager -profile crick`

### screening

- Low coverage data.

### production

- High coverage data.

### external

- External higher coverage data.
