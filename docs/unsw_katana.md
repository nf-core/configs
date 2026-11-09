# nf-core/configs: UNSW Katana HPC Configuration

nf-core pipelines have been successfully configured for use on the [UNSW Katana](https://docs.restech.unsw.edu.au/) at the University of New South Wales, Sydney, Australia.

To run an nf-core pipeline at UNSW Katana, run the pipeline with `-profile singularity,unsw_katana`. This will download and launch the [`unsw_katana.config`](../conf/unsw_katana.config) which has been pre-configured with a setup suitable for the unsw katana HPC cluster. Using this profile, a Singularity image containing all of the required software will be used for the pipeline.

## Launch an nf-core pipeline on Katana

### Prerequisites

Before running the pipeline you will need to load Nextflow and Java, both of which are globally installed modules on Katana. You can do this by running the commands below:

```bash
module purge
module load nextflow java
```

### Execution command

```bash
nextflow run <nf-core_pipeline>/main.nf \
    -profile singularity,unsw_katana \
    <additional flags>

# Replace `<nf-core_pipeline>` with the name of the nf-core pipeline you want to run, e.g., `nf-core/proteinfold`.

### Queue limits

This config is defined in line with the [UNSW Katana queue limits](https://docs.restech.unsw.edu.au/using_katana/running_jobs/#job-queue-limits-summary).
```
