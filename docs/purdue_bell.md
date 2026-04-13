# nf-core/configs: Purdue RCAC Bell

The `purdue_bell` profile configures nf-core pipelines to run on the Bell cluster operated by the Rosen Center for Advanced Computing (RCAC) at Purdue University.

Bell is an AMD EPYC 7662 (Rome) cluster with 128 cores and 256 GB RAM per standard node. See the [RCAC Bell user guide](https://www.rcac.purdue.edu/compute/bell) for hardware and policy details.

## Prerequisites

```bash
module purge
module load nextflow
```

The `nextflow` module pulls in a compatible JDK (`openjdk/17.0.2_8` is available on Bell). Apptainer is system-wide; `/usr/bin/singularity` is a symlink to `apptainer`.

## Required parameter: `--cluster_account`

RCAC Slurm jobs must specify an account. List yours with `slist`, then pass it to Nextflow:

```bash
slist

nextflow run nf-core/<pipeline> \
    -profile purdue_bell \
    --cluster_account <your_account> \
    --input samplesheet.csv \
    --outdir results
```

The profile will refuse to submit jobs if `--cluster_account` is unset.

## Partition routing

| nf-core label         | Partition | Notes                                            |
| --------------------- | --------- | ------------------------------------------------ |
| _default_             | `cpu`     | 128 cores, 256 GB, up to 14 d                    |
| `process_long`        | `cpu`     | 14 d max                                         |
| `process_high_memory` | `highmem` | 1 TB nodes, jobs forced to >= 65 cores, 24 h cap |

GPU partitions on Bell are AMD MI50 (`gpu`) and MI60 (`multigpu`), both ROCm-based. They are **not exposed** by this profile because nf-core GPU pipelines are CUDA-only.

## Standby queue (optional)

Bell offers a 4 h standby QoS for short jobs. Opt in with:

```bash
nextflow run ... -profile purdue_bell --use_standby true ...
```

`standby` is not permitted on `highmem`, so high-memory steps remain on the normal QoS even when this flag is set.

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
- nf-core/demo 1.1.0 (`-profile test,purdue_bell`)
- Apptainer (system, `/usr/bin/apptainer`)
- Last validated: 2026-04-13

## Contact

- Arun Seetharam, [@aseetharam](https://github.com/aseetharam), <aseethar@purdue.edu>
- [RCAC support](https://www.rcac.purdue.edu/about/contact)
