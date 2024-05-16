# nf-core/configs: Cancer Research UK Manchester Institute Configuration

All nf-core pipelines have been successfully configured for the use on the HPC (griffin) at Cancer Research UK Manchester Institute.

To use, run the pipeline with `-profile crukmi`. This will download and launch the [`crukmi.config`](../conf/crukmi.config) which has been pre-configured with a setup suitable for the Griffin HPC. Using this profile, Apptainer/Singularity images will be downloaded to run on the cluster and stored in a centralised location.

Before running the pipeline you will need to load Nextflow using the environment module system, for example via:

```bash
## Load Nextflow environment modules
module purge
module load apps/nextflow
```

The pipeline should always be executed inside a workspace on the `/scratch/` system. All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large.
