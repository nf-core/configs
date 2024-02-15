# nf-core/configs: New York Genome Center Configuration

To use, run a pipeline with `-profile nygc`. This will download and launch the [`nygc.config`](../conf/nygc.config) which has been
pre-configured with a setup suitable for the New York Genome Center cluster. Using this profile, container images with all required software will be pulled before execution of a job requiring that software.

## Module Requirements

In order to run a pipeline on the NYGC cluster, you will need to load the following modules:

```bash
module load singularity/3.8.6
module load nextflow/22.10.4
```

Note: All of the intermediate files generated from running a pipeline will be stored in the `work/` subdirectory of where the pipeline was launched. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the defined output directory as well.
