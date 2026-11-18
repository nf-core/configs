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

Set both of these environment variables before running the pipeline, or Singularity will fill up your `$HOME` quota:

- `NXF_SINGULARITY_CACHEDIR`: Nextflow's cache of converted `.sif` images. Left unset, Nextflow caches them per work directory instead, re-downloading on every new run.
- `SINGULARITY_CACHEDIR`: Singularity's own cache, used while pulling/converting images - unrelated to the Nextflow setting above. Left unset, it defaults to `$HOME/.singularity/cache`, which is usually quota-limited and the actual cause of most `$HOME`-filling-up issues.

```bash
export NXF_SINGULARITY_CACHEDIR=/work_ikmb/<username>/singularity_cache
export SINGULARITY_CACHEDIR=/work_ikmb/<username>/singularity_cache
## or, if your group uses work_beegfs instead:
# export NXF_SINGULARITY_CACHEDIR=/work_beegfs/<username>/singularity_cache
# export SINGULARITY_CACHEDIR=/work_beegfs/<username>/singularity_cache
```

> NB: Access to the caucau cluster is restricted. Please talk to Georg Hemmrich-Stanisak to get access (@ghemmrich).
