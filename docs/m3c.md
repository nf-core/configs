# nf-core/configs: M3C Configuration

All nf-core pipelines have been successfully configured for use on the M3 cluster at the [M3 Research Center](https://www.medizin.uni-tuebingen.de/de/das-klinikum/einrichtungen/zentren/m3) here.

To use, run the pipeline with `-profile m3c`. This will download and launch the [`m3c.config`](../conf/m3c.config) which has been pre-configured with a setup suitable for the M3 cluster. Using this profile, for DSL1 pipelines a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline. For pipelines in DSL2, the individual Singularity images will be downloaded.

Before running the pipeline you will need to install Nextflow on the M3 cluster. You can do this by following the instructions [here](https://www.nextflow.io/).

A local copy of the [AWS-iGenomes](https://registry.opendata.aws/aws-igenomes/) resource has been made available on M3C so you should be able to run the pipeline against any reference available in the `igenomes.config` specific to the nf-core pipeline. You can do this by simply using the `--genome <GENOME_ID>` parameter.

This config includes the necessary parameters for estimating the CO2 footprint via the [nf-co2footprint plugin](https://github.com/nextflow-io/nf-co2footprint) of any pipeline run on the cluster. The parameters are the cluster-specific power usage effectiveness (PUE) and the location of the cluster in Germany(`DE`).

> [!Note]
> You will need an account to use the M3 HPC cluster in order to run the pipeline. If in doubt contact IT.
> [!Note]
> Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
> [!Note]
> Each group needs to configure their singularity cache directory.
