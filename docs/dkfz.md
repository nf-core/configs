# nf-core/configs: DKFZ configuration

To use, run the pipeline with `-profile dkfz`. This will download and launch the [`dkfz.config`](../conf/dkfz.config), pre-configured for the Deutsches Krebsforschungszentrum (DKFZ) / ODCF LSF cluster in Heidelberg, Germany.

This configuration is tested with Nextflow 25.10.0 (available on the cluster as a module).

The profile only configures the cluster itself (LSF executor, dynamic queue selection, scratch, resource limits and the `/omics` bind-mount). Pick a container engine on the command line, e.g. `-profile dkfz,apptainer` or `-profile dkfz,conda`.

> :warning: **Use Apptainer/Singularity (or Conda), not Docker.** On the ODCF cluster Docker is only available through LSF's `docker-generic` application profile. Nextflow's `docker` executor runs `docker run` directly on the node, which this setup does not allow, so `-profile dkfz,docker` will not work. Use `-profile dkfz,apptainer` instead.

## Before you use this profile

1. Load Nextflow via the environment module system on a submission host. Check the pipeline's README for the required Nextflow version:

   ```bash
   module load Nextflow/25.10.0
   ```

2. Submit from a submission host (`bsub01.lsf.dkfz.de` / `bsub02.lsf.dkfz.de`). Do **not** run heavy work on the login/worker nodes. Wrap the Nextflow driver itself in a `bsub` job (see below).

3. The shared `/omics` filesystem is bind-mounted into every container automatically. If your inputs or references live elsewhere, point `NXF_APPTAINER_CACHEDIR` / `NXF_SINGULARITY_CACHEDIR` at a path under `/omics` so images are cached on shared storage:

   ```bash
   export NXF_APPTAINER_CACHEDIR=/omics/groups/<your-group>/.../apptainer_cache
   ```

## Queues

Queue selection is automatic, based on each task's requested `time` and `memory`:

| Queue      | Selected when                       | Limit             |
| ---------- | ----------------------------------- | ----------------- |
| `short`    | no time given, or `time <= 10.min`  | 10 min            |
| `medium`   | `time <= 1.h`                       | 1 hour            |
| `long`     | `time <= 10.h`                      | 10 hours          |
| `verylong` | `time > 10.h`                       | no hard limit     |
| `highmem`  | `memory > 200.GB`                   | up to ~4 TB       |

Note: `highmem` is the only queue that accepts requests above 200 GB (and it rejects requests below 200 GB).

## Resource limits, retries and containers

- Every task is capped to what the cluster can provide via `process.resourceLimits` (64 CPUs, 1000 GB memory, 720 h). Requests above these are capped automatically.
- Unlabelled processes default to a safe 1 CPU / 6 GB / 10 min.
- The shared `/omics` filesystem is bound into every container via `containerOptions`, with `--nv` added for accelerator tasks. **If one of your modules sets its own `containerOptions`, re-add `--bind /omics` there.**

## Enable GPU support

This profile turns any task that requests a GPU through Nextflow's standard [`accelerator` directive](https://www.nextflow.io/docs/latest/reference/process.html#accelerator) into a correct DKFZ GPU submission. It selects the GPU queue, builds the LSF `-gpu num=<n>:j_exclusive=yes[:gmem=<n>G]` request, and adds `--nv` so the GPU is visible inside the container.

How a task acquires an `accelerator` request depends on the pipeline:

- **nf-core pipelines** mark GPU-capable processes with the `process_gpu` label and only switch the accelerator on when the run includes the `gpu` profile. So add `gpu` to your profile list:

  ```bash
  nextflow run <pipeline> -profile dkfz,gpu,apptainer --input ... --outdir ...
  ```

- **Custom / non-nf-core pipelines** just declare `accelerator` on the GPU process:

  ```nextflow
  process MY_GPU_TASK {
      accelerator 1
      container 'docker://nvcr.io/...'

      script:
      "my_gpu_tool ..."
  }
  ```

  ```bash
  nextflow run main.nf -profile dkfz,apptainer --outdir ...
  ```

Tasks without an `accelerator` request are unaffected and run on the normal CPU queues.

### Choosing the GPU queue

The `--dkfz_gpu_queue` parameter selects which GPU queue all GPU jobs are submitted to (default `gpu`):

- `gpu` — default (RTX 2080 Ti … V100/A100-DGX), 72 h wall time
- `gpu-lowprio` — same nodes as `gpu` but low priority; use for large job batches
- `gpu-pro` — high-end A100/H200/L40S/GH200, 142 h wall time — **requires a separate access application to the DKFZ Data Science Board**

### Number of GPUs and GPU memory per process

The profile builds the LSF request as `-gpu num=<n>:j_exclusive=yes[:gmem=<n>G]` (DKFZ requires `j_exclusive=yes` and rejects `mode=exclusive_process`). Two things are tunable per process:

- **Number of GPUs** — the [`accelerator` directive](https://www.nextflow.io/docs/latest/reference/process.html#accelerator) (default 1).
- **GPU memory (optional)** — set `ext.gpu_memory` to a Nextflow memory value to pin the job to GPUs with at least that much VRAM. When `ext.gpu_memory` is unset, `gmem` is omitted and LSF assigns any free GPU.

Approximate values to target each GPU tier (request at or just below the card's usable VRAM):

| `ext.gpu_memory` | Targets                         | Queue              |
| ---------------- | ------------------------------- | ------------------ |
| `10.GB`          | RTX 2080 Ti (11 GB)             | `gpu`              |
| `15.GB`          | V100 16 GB                      | `gpu`              |
| `23.GB`          | TITAN RTX / Quadro RTX (24 GB)  | `gpu`              |
| `31.GB`          | V100 32 GB                      | `gpu`              |
| `40.GB`          | A100 40 GB                      | `gpu-pro` only     |
| `46.GB`          | L40S                            | `gpu-pro` only     |
| `98.GB`          | GH200                           | `gpu-pro` only     |
| `141.GB`         | H200                            | `gpu-pro` only     |

Set these directly on the process, or per process name from config (e.g. nf-core's `conf/modules.config`):

```nextflow
process {
    // 2 GPUs, any free GPU (no gmem constraint)
    withName: 'FOO:BAR:ALIGN_GPU' {
        accelerator = 2
    }
    // 1 big-memory GPU
    withName: 'FOO:BAR:FOLD' {
        accelerator    = 1
        ext.gpu_memory = 40.GB   // -> A100/L40S/H200; also set --dkfz_gpu_queue gpu-pro
    }
}
```

> :warning: Requesting `40.GB` or more only works on `gpu-pro`. On the plain `gpu` queue such a request hangs in `PEND` forever. Use at most 12 CPUs and ~45 GB host RAM per GPU (DKFZ GPU usage policy).

## Running Nextflow on the cluster

Run the Nextflow driver inside an LSF job rather than on a submission host directly. Make a script and submit it with `bsub < my_script.sh`:

```bash
#!/bin/bash
#BSUB -J nf_pipeline
#BSUB -o nf_pipeline.%J.log
#BSUB -q long
#BSUB -n 2
#BSUB -R "rusage[mem=8G]"
#BSUB -W 10:00

module load Nextflow/25.10.0

# Cache images on shared storage so worker nodes can reach them:
export NXF_APPTAINER_CACHEDIR=/omics/groups/<your-group>/.../apptainer_cache

nextflow run <pipeline> \
    -profile dkfz,apptainer \
    --input samplesheet.csv \
    --outdir results
```

Add `gpu` to `-profile` (e.g. `-profile dkfz,gpu,apptainer`) to send `process_gpu` tasks to a GPU queue.

