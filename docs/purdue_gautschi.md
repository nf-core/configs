# nf-core/configs: Purdue RCAC Gautschi

The `purdue_gautschi` profile configures nf-core pipelines to run on the Gautschi cluster operated by the Rosen Center for Advanced Computing (RCAC) at Purdue University.

Gautschi is an AMD EPYC 9654 (Genoa) cluster with 192 cores and 384 GB RAM per standard CPU node, plus NVIDIA L40 and H100 GPU partitions. See the [RCAC Gautschi user guide](https://www.rcac.purdue.edu/knowledge/gautschi) for hardware and policy details.

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

| nf-core label         | Partition                    | Notes                                                                                 |
| --------------------- | ---------------------------- | ------------------------------------------------------------------------------------- |
| _default_             | `cpu`                        | 192 cores, 384 GB, up to 14 d                                                         |
| `process_long`        | `cpu`                        | 14 d max; always uses normal QoS (standby has a 4 h limit)                            |
| `process_high_memory` | `highmem`                    | 1.5 TB nodes, 24 h cap; profile claims full node (192 cores) to satisfy the >48 floor |
| `process_gpu`         | `smallgpu` (default) or `ai` | NVIDIA L40 (24 h) or H100 (14 d); see below                                           |

## GPU jobs

By default, `process_gpu` routes to the `smallgpu` partition (2x NVIDIA L40 per node, 24 h walltime). To use the `ai` partition (8x NVIDIA H100 per node, 14 d walltime), pass:

```bash
nextflow run ... -profile purdue_gautschi --gpu_partition ai ...
```

The profile derives `--gres=gpu:N` from each task's `accelerator.request` directive, so multi-GPU workflows work without further configuration. Pipelines that don't set `accelerator` get 1 GPU by default. `ai` nodes are scarce; use `smallgpu` unless your workflow specifically needs H100 throughput, NVLink, or > 48 GB GPU memory.

The `profiling` partition is intended for hardware performance work and is not exposed by this profile.

## Standby queue (optional)

Gautschi offers a 4 h standby QoS for short CPU jobs:

```bash
nextflow run ... -profile purdue_gautschi --use_standby true ...
```

`standby` does not apply to `highmem`, `process_long`, or GPU jobs.

## Reference data

A shared iGenomes mirror is mounted at `/depot/itap/datasets/igenomes` and the profile sets `params.igenomes_base` accordingly. Use the standard nf-core `--genome` keys (e.g. `--genome GRCh38`).

To use your own reference instead, pass the relevant pipeline parameters explicitly (`--fasta`, `--gtf`, etc.).

## Container cache and work directory

```bash
export NXF_SINGULARITY_CACHEDIR=$RCAC_SCRATCH/.apptainer/cache
nextflow run ... -w $RCAC_SCRATCH/nextflow-work ...
```

## Tested with

- Nextflow 25.10.4
- nf-core/demo 1.1.0 (`-profile test,purdue_gautschi`)
- Apptainer (system, `/usr/bin/apptainer`)
- Last validated: 2026-04-13

## Contact

- Arun Seetharam, [@aseetharam](https://github.com/aseetharam), <aseethar@purdue.edu>
- [RCAC support](https://www.rcac.purdue.edu/about/contact)
