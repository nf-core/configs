# nf-core/configs: CREATE HPC Configuration

All nf-core pipelines have been successfully configured for use on the King's Computational Research, Engineering and Technology Environment (CREATE) HPC cluster at e-Research, King's College London.

To use this profile, run the pipeline with `-profile create`. This will download and launch the [`create.config`](../conf/create.config) which has been pre-configured with a setup suitable for the CREATE HPC cluster.

Before running the pipeline you will need to load Nextflow using the environment module system on CREATE HPC. You can do this with the following command:

```bash
module load nextflow
```

> NB: You will need an account to use the CREATE HPC cluster in order to run the pipeline. If in doubt contact IT.
