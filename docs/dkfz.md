# nf-core/configs: DKFZ configuration

This configuration specifies hardware and infrastructure access at the Deutsches Krebsforschungszentrum (DKFZ) HPC cluster in Heidelberg / Germany.

To use, run the pipeline with `-profile dkfz`. This will download and launch the dkfz.config which has been pre-configured with a setup suitable for the cluster. Using this profile, either Singularity containers are pulled from public repositories or a Docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

> :warning: Before using the confuguratiron, add Singularity environment options (SINGULARITY_CACHEDIR and SINGULARITY_LIBRARYDIR) to `env`

> :warning: Before running the pipeline you will need to load Nextflow using the environment module system. Please check the main README of the pipeline to make sure that the version of Nextflow is compatible with that required to run the pipeline. You can do this by issuing the commands below:

```bash
module load Nextflow/21.04.0
```

> Note: All of the intermediate files required to run the pipeline will be stored in the work/ directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the results/ directory anyway.
