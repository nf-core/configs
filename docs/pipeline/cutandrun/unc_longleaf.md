# nf-core/configs: UNC's Longleaf CUT&RUN specific configuration

Extra specific configuration for cutandrun pipeline

## Pipeline specific profiles

Specific-pipeline profiles exist for the following pipelines, and will be automatically loaded when supplying `-profile unc_longleaf` to your command:

- cutandrun

## Usage

To use, run the pipeline with `-profile unc_longleaf`.

This will download and launch the eager specific [`unc_longleaf.config`](../../../conf/pipeline/cutandrun/unc_longleaf.config) which is adapted to data generated at UNC-CH and processed on the Longleaf HPC.

Example: `nextflow run nf-core/cutandrun -profile unc_longleaf`

### Specifics

This custom config adds extra memory to the FRAG_LEN_HIST and DEEPTOOLS_PLOTHEATMAP_GENE_ALL as the jobs kept failing with default memory limits
