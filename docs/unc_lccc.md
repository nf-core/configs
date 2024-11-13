# nf-core/configs: PROFILE Configuration

nf-core pipelines have been successfully configured for use on the Lineberger Bioinformatics Group cluster at the University of North Carolina at Chapel Hill Lineberger Comprehensive Cancer Center.

To use, run the pipeline with `-profile unc_lccc` in the `nextflow run [...]` command. This will download and launch the [`unc_lccc.config`](../conf/unc_lccc.config) which has been pre-configured with a setup suitable for the LBG cluster. Using this profile, Docker images containing all of the required software will be downloaded, and converted to a Apptainer/Singularity image during execution of the pipeline.

## Below are non-mandatory information

Before running pipelines you should login to a compute node and install `nextflow` into your home directory.  Directions at the following link: https://www.nextflow.io/. There is a copy of the `nextflow` executable in our default setup, but it tends to lag behind the released versions, so may or may not work with a given workflow.  

> NB: You will need an account to use the in order to run the pipelines and the `nextflow` commands will need to run on compute nodes, not a login node. If in doubt contact <informaticshelp@unc.edu>.

