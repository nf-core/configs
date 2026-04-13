# nf-core/configs: Purdue RCAC Negishi

The `purdue_negishi` profile configures nf-core pipelines to run on the Negishi cluster operated by the Rosen Center for Advanced Computing (RCAC) at Purdue University.

Negishi is an AMD EPYC 7763 (Milan) cluster with 128 cores and 256 GB RAM per standard node. See the [RCAC Negishi user guide](https://www.rcac.purdue.edu/knowledge/negishi/gateway) for hardware and policy details.

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

| nf-core label         | Partition | Notes                                                                               |
| --------------------- | --------- | ----------------------------------------------------------------------------------- |
| _default_             | `cpu`     | 128 cores, 256 GB, up to 14 d                                                       |
| `process_long`        | `cpu`     | 14 d max; always uses normal QoS (standby has a 4 h limit)                          |
| `process_high_memory` | `highmem` | 1 TB nodes, 24 h cap; profile claims full node (128 cores) to satisfy the >64 floor |

GPU partitions on Negishi are AMD MI210 (ROCm) and are **not exposed** by this profile because nf-core GPU pipelines are CUDA-only.

## Standby queue (optional)

Negishi offers a 4 h standby QoS with higher throughput for short jobs. Opt in with:

```bash
nextflow run ... -profile purdue_negishi --use_standby true ...
```

`standby` is not applied to `highmem` or `process_long` labels (their walltime exceeds the 4 h QoS cap), so those steps remain on the normal QoS even when this flag is set. Use this flag when every step fits inside 4 h, e.g. iterative development on small datasets.

## Reference data

A shared iGenomes mirror is mounted at `/depot/itap/datasets/igenomes` and the profile sets `params.igenomes_base` accordingly. Use the standard nf-core `--genome` keys (e.g. `--genome GRCh38`).

To use your own reference instead, pass the relevant pipeline parameters explicitly (`--fasta`, `--gtf`, etc.).

## Container cache

Apptainer image cache defaults to `$RCAC_SCRATCH/.apptainer/cache`. To override:

```bash
export NXF_SINGULARITY_CACHEDIR=/path/to/your/cache
```

## Work directory

Place Nextflow's `work/` directory on scratch:

```bash
nextflow run ... -w $RCAC_SCRATCH/nextflow-work ...
```

## Tested with

- Nextflow 25.10.4
- nf-core/demo 1.1.0 (`-profile test,purdue_negishi`)
- Apptainer (system, `/usr/bin/apptainer`)
- Last validated: 2026-04-13

## Contact

- Arun Seetharam, [@aseetharam](https://github.com/aseetharam), <aseethar@purdue.edu>
- [RCAC support](https://www.rcac.purdue.edu/about/contact)
