# nf-core/configs: Tufts HPC Configuration

nf-core pipelines have been configured for use on the Tufts HPC clusters operated by Research Technology at Tufts University.

To use Tufts's profile, run the pipeline with `-profile tufts`.

Example: `nextflow run <pipeline> -profile tufts`

Users can also put the `nextflow ...` command into a batch script and submit the job to computing nodes by `sbatch` or launch interative jobs to computing nodes by `srun`. Using this way, both nextflow manager processes and tasks will run on the allocated compute nodes using the `local` executor. It is recommended to use `-profile singularity`

Example: `nextflow run <pipeline> -profile singularity`

By default, the `batch` partition is used for job submission. Other partitions can be specified using the `--partition <PARTITION NAME>` argument to the run.

## Environment module

Before running the pipeline, you will need to load the Nextflow module by:

```bash
module purge ## Optional but recommended
module load nextflow singularity
```
