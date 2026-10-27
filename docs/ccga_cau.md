# nf-core/configs: CCGA CAU Cluster Configuration

Deployment and testing of nf-core pipelines at the CCGA cau cluster is on-going.

To use, run the pipeline with `-profile ccga_cau`. This will download and launch the [`ccga_cau.config`](../conf/ccga_cau.config) which has been pre-configured with a setup suitable for the caucluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Before running the pipeline you will need to load Nextflow and Singularity using the environment module system on the cluster. You can do this by issuing the commands below:

```bash
## Load Nextflow and Singularity environment modules
module load gcc12-env
module load nextflow
module load singularity
```

This profile does not set a shared Singularity cache directory, so you must set your own `NXF_SINGULARITY_CACHEDIR` pointing to a location in your own work directory before running the pipeline. If left unset, Singularity will cache downloaded container images under `$HOME/.singularity/cache` by default, which has limited, quota-restricted space and will fill up quickly.

A shared, institute-wide cache directory is deliberately not set here: users would still need write access to a subdirectory of it, and permissions on a shared location like that are easy to get wrong (or to leave too open). Point it at your own writable work storage instead - which workspace that is depends on your institute/group, e.g. `/work_ikmb/<username>/` or `/work_beegfs/<username>/`:

```bash
## Point the Singularity cache to your own work directory
export NXF_SINGULARITY_CACHEDIR=/work_ikmb/<username>/singularity_cache
## or, if your group uses work_beegfs instead:
# export NXF_SINGULARITY_CACHEDIR=/work_beegfs/<username>/singularity_cache
```

> NB: Access to the caucau cluster is restricted. Please talk to Georg Hemmrich-Stanisak to get access (@ghemmrich).
