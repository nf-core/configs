# nf-core/configs: Tufts HPC Configuration

nf-core pipelines have been configured for use on the Tufts HPC clusters operated by Research Technology at Tufts University.

To use Tufts's profile, run the pipeline with `-profile tufts`.

Example:

`nextflow run <pipeline> -profile tufts`

Users can also put the `nextflow ...` command into a batch script and submit the job to computing nodes using `sbatch`, or launch interactive jobs on computing nodes using `srun`. When running on allocated compute nodes this way, both the Nextflow manager process and tasks will run on the compute nodes using the `local` executor. It is recommended to use `-profile singularity`.

Example:

`nextflow run <pipeline> -profile singularity`

By default, the `batch` partition is used for job submission. Other partitions can be specified using the `--partition <PARTITION NAME>` argument to the run.

## GPU partition

Some tools / pipeline steps require GPUs (for example, Parabricks-based workflows). On Tufts HPC, GPU jobs should run on the `gpu` partition.

This profile routes GPU-enabled processes to the GPU partition using a process label:

- Processes with the label `process_gpu` are submitted to the `gpu` partition
- GPU resources are requested via Slurm `--gres=gpu:1`

### Example usage

If the pipeline (or your custom config) marks GPU steps with the `process_gpu` label, you can run normally and those steps will be scheduled on the GPU nodes:

`nextflow run <pipeline> -profile tufts`

If you need to override the GPU partition name:

`nextflow run <pipeline> -profile tufts --gpu_partition <GPU_PARTITION_NAME>`

> Note: Whether GPU jobs are used depends on the pipeline and tool configuration. Many nf-core pipelines are CPU-only unless explicitly configured to run GPU-enabled tools.

## Debugging (keep `work/` directory)

By default, this profile enables Nextflow cleanup on successful completion, which removes intermediate files in the `work/` directory to save space.

To keep the `work/` directory for debugging, disable cleanup:

`nextflow run <pipeline> -profile tufts --disable_cleanup true`

This is useful if you need to inspect intermediate files, reproduce errors, or re-run specific steps manually.

## Environment module

Before running the pipeline, you will need to load the Nextflow module by:

```bash
module purge ## Optional but recommended
module load nextflow singularity
```
