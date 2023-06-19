# nf-core/configs: CFC Configuration

All nf-core pipelines have been successfully configured for use on the CFC cluster at the [Quantitative Biology Center](https://uni-tuebingen.de/forschung/forschungsinfrastruktur/zentrum-fuer-quantitative-biologie-qbic/) here.

To use, run the pipeline with `-profile cfc`. This will download and launch the [`cfc.config`](../conf/cfc.config) which has been pre-configured with a setup suitable for the CFC cluster. Using this profile, for DSL1 pipelines a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline. For pipelines in DSL2, the individual Singularity images will be downloaded.

Before running the pipeline you will need to install Nextflow on the CFC cluster. You can do this by following the instructions [here](https://www.nextflow.io/).

> NB: You will need an account to use the HPC cluster CFC in order to run the pipeline. If in doubt contact IT.
> NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
