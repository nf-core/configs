# nf-core/configs: TIGEM Configuration

All nf-core pipelines have been successfully configured for use on the TIGEM SLURM cluster.  
To use, run the pipeline with `-profile tigem`. This will download and launch the [`tiegm.config`](../conf/tigem.config) which has been pre-configured
with a setup suitable for the TIGEM cluster. Using this profile, either a docker image containing all of the required software will be downloaded,
and converted to a Singularity image or a Singularity image downloaded directly before execution of the pipeline.

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline
has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.

> NB: You will need an VPN account to use the TIGEM cluster in order to run the pipeline. If in doubt contact @giusmar.
