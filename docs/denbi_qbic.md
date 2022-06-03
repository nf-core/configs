# nf-core/configs: de.NBI QBIC Configuration

All nf-core pipelines have been successfully configured for use on the de.NBI Cloud cluster. This is a virtual cluster that has been set up using the [virtual cluster setup scripts](https://github.com/MaximilianHanussek/virtual_cluster_local_ips).

To use, run the pipeline with `-profile denbi_qbic`. This will download and launch the [`denbi_qbic.config`](../conf/denbi_qbic.config) which has been pre-configured with a setup suitable for the automatically created cluster. Using this profile, a Docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

> NB: You will need an account to use de.NBI Cluster in order to run the pipeline. If in doubt contact IT.
> NB: Nextflow will need to submit the jobs via the job scheduler to the cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
