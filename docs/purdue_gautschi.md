# nf-core/configs: Purdue RCAC Gautschi

The `purdue_gautschi` profile configures nf-core pipelines to run on the Gautschi cluster operated by the Rosen Center for Advanced Computing (RCAC) at Purdue University.

Gautschi is an AMD EPYC 9654 (Genoa) cluster with 192 cores and 384 GB RAM per standard CPU node, 1.5 TB highmem nodes, plus NVIDIA L40 and H100 GPU partitions. See the [RCAC Gautschi user guide](https://www.rcac.purdue.edu/knowledge/gautschi) for hardware and policy details.

## Prerequisites

```bash
module purge
module load nextflow
```

The `nextflow` module pulls in a compatible JDK (`openjdk/17.0.2_8` is available on Gautschi). Apptainer is system-wide; `/usr/bin/singularity` is a symlink to `apptainer`.

## Required parameter: `--cluster_account`

```bash
slist

nextflow run nf-core/<pipeline> \
    -profile purdue_gautschi \
    --cluster_account <your_account> \
    --input samplesheet.csv \
    --outdir results
```

The profile will refuse to submit jobs if `--cluster_account` is unset.

## Partition routing

CPU and high-memory jobs are routed dynamically based on the task's memory request:

| Memory request | Partition | Walltime cap | Notes                                                  |
| -------------- | --------- | ------------ | ------------------------------------------------------ |
| `<= 384 GB`    | `cpu`     | 14 d         | Default for most pipeline steps                        |
| `> 384 GB`     | `highmem` | 24 h         | Slurm requires `>= 49 cores` per job on this partition |

If a pipeline step requests more than 384 GB RAM but fewer than 49 cores, Slurm will reject the submission. Raise the step's CPU request in a pipeline-level config, or lower its memory request if the real need is below 384 GB.

GPU-labelled steps (`process_gpu`) route to the `smallgpu` partition by default. The `profiling` partition is intended for hardware performance work and is not exposed by this profile.

## GPU jobs

By default, `process_gpu` routes to the `smallgpu` partition (2x NVIDIA L40 per node, 24 h walltime). To use the `ai` partition (8x NVIDIA H100 per node, 14 d walltime), pass:

```bash
nextflow run ... -profile purdue_gautschi --gpu_partition ai ...
```

The profile derives `--gres=gpu:N` from each task's `accelerator.request` directive, so multi-GPU workflows (e.g. parabricks) work without further configuration. Pipelines that don't set `accelerator` get 1 GPU by default. `ai` nodes are scarce; use `smallgpu` unless your workflow specifically needs H100 throughput, NVLink, or > 48 GB GPU memory.

## Standby queue (optional)

Gautschi offers a 4 h standby QoS for short CPU jobs:

```bash
nextflow run ... -profile purdue_gautschi --use_standby true ...
```

Jobs are routed through standby only when they fit within the QoS limits (<= 4 h walltime, <= 384 GB memory). Longer, larger, or GPU steps automatically fall back to the normal QoS.

## Reference data

A shared iGenomes mirror is mounted at `/depot/itap/datasets/igenomes` and the profile sets `params.igenomes_base` accordingly. Use the standard nf-core `--genome` keys (e.g. `--genome GRCh38`) in supported pipelines.

To use your own reference instead, pass the relevant pipeline parameters explicitly (`--fasta`, `--gtf`, etc.).

## Container cache and work directory

```bash
export NXF_SINGULARITY_CACHEDIR=$RCAC_SCRATCH/.apptainer/cache
nextflow run ... -w $RCAC_SCRATCH/nextflow-work ...
```

## Contact

- Arun Seetharam, [@aseetharam](https://github.com/aseetharam), <aseethar@purdue.edu>
- [RCAC support](https://www.rcac.purdue.edu/about/contact)
