# nf-core/configs: Purdue RCAC Negishi

The `purdue_negishi` profile configures nf-core pipelines to run on the Negishi cluster operated by the Rosen Center for Advanced Computing (RCAC) at Purdue University.

Negishi is an AMD EPYC 7763 (Milan) cluster with 128 cores and 256 GB RAM per standard node, plus 1 TB highmem nodes. See the [RCAC Negishi user guide](https://www.rcac.purdue.edu/knowledge/negishi/gateway) for hardware and policy details.

## Prerequisites

```bash
module purge
module load nextflow
module load apptainer
```

Apptainer is the actual container runtime on Negishi (`/usr/bin/singularity` is a symlink to `apptainer`). The profile uses an `apptainer {}` block accordingly.

## Required parameter: `--cluster_account`

RCAC Slurm jobs must specify an account. List yours with `slist`, then pass it to Nextflow:

```bash
slist

nextflow run nf-core/<pipeline> \
    -profile purdue_negishi \
    --cluster_account <your_account> \
    --input samplesheet.csv \
    --outdir results
```

The profile will refuse to submit jobs if `--cluster_account` is unset.

## Partition routing

The profile routes each task dynamically based on its memory request:

| Memory request | Partition | Walltime cap | Notes                                                  |
| -------------- | --------- | ------------ | ------------------------------------------------------ |
| `<= 256 GB`    | `cpu`     | 14 d         | Default for most pipeline steps                        |
| `> 256 GB`     | `highmem` | 24 h         | Slurm requires `>= 65 cores` per job on this partition |

If a pipeline step requests more than 256 GB RAM but fewer than 65 cores, Slurm will reject the submission. Raise the step's CPU request in a pipeline-level config, or lower its memory request if the real need is below 256 GB.

GPU partitions on Negishi are AMD MI210 (ROCm) and are **not exposed** by this profile because nf-core GPU pipelines are CUDA-only.

## Standby queue (optional)

Negishi offers a 4 h standby QoS with higher throughput for short jobs:

```bash
nextflow run ... -profile purdue_negishi --use_standby true ...
```

Jobs are routed through standby only when they fit within the QoS limits (<= 4 h walltime, <= 256 GB memory). Longer or larger steps automatically fall back to the normal QoS.

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
