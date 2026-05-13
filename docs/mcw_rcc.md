# nf-core/configs: MCW RCC Configuration

The [Medical College of Wisconsin Research Computing Center
(RCC)](https://www.mcw.edu/departments/clinical-and-translational-science-institute/research-services/research-computing)
runs a SLURM-managed HPC cluster (login hosts `ln*`, scratch on
`qfs1.rcc.mcw.edu:/scratchfs`).

## Important: keep everything on `/scratch`, not `/group`

The `/scratch` filesystem (`qfs1.rcc.mcw.edu:/scratchfs`) is mounted on
both login nodes and compute nodes. The `/group` filesystem
(`qfs2.rcc.mcw.edu:/groupfs`) is **mounted on login nodes only** —
compute nodes cannot see it.

A Nextflow run reads its samplesheet, container cache, and reference
files from compute nodes, not from the login node where you launched
`nextflow`. Anything under `/group` will appear missing or empty to
running tasks and the pipeline will fail in confusing ways.

Concretely, before launching a pipeline:

- `-work-dir` must point under `/scratch/g/<user>/...`
- `--outdir` must point under `/scratch/g/<user>/...`
- `--input` (samplesheet) and any local reference files (FASTA, GTF,
  …) must live under `/scratch/g/<user>/...`

`-profile mcw_rcc` only binds `/scratch` and `/hpc` into containers,
not `/group`, so this constraint is enforced for image-level access
too.

To use, run the pipeline with `-profile mcw_rcc`. This loads
[`mcw_rcc.config`](../conf/mcw_rcc.config), which is pre-configured for
this cluster's SLURM partitions, per-core memory limits, and Apptainer
container runtime.

## Prerequisites

Load **both** Nextflow and Apptainer in your submission script:

```bash
module load nextflow/25.10.2
module load apptainer/1.4.1
```

Apptainer must be loaded in the driver script (not just inside tasks)
because Nextflow pulls each container image **from its own driver
process** before launching any task — at that point, no
`process.beforeScript` has had a chance to run. The profile still adds
`module load apptainer/1.4.1` to every task's `beforeScript`, so once
the driver-side pull succeeds, individual tasks find apptainer
correctly too.

## Partitions and auto-routing

The profile picks a SLURM partition per task based on the task's
declared resources:

| Partition | Nodes × CPU × Memory       | Max walltime | When this profile uses it                                            |
| --------- | -------------------------- | ------------ | -------------------------------------------------------------------- |
| `normal`  | 60 × 48 CPU × 360 GB       | 7 days       | Default for any task at ≤ 7.5 GB / core and ≤ 360 GB / node          |
| `bigmem`  | 2 × 48 CPU × 1.5 TB        | 7 days       | Auto-selected when memory > 360 GB or memory / cpus > 7.5 GB         |
| `gpu`     | 11 mixed V100 / A40 / L40S | 7 days       | Tasks labeled `process_gpu`; one GPU is requested via `--gres=gpu:1` |

The `normal` partition rejects allocations with more than 7680 MB per
CPU. Rather than letting those submissions fail, the profile routes
them to `bigmem`. If you find a process is being sent to `bigmem` more
aggressively than you want, lower its memory request or raise its CPU
request (e.g. via `withName: '<PROC>' { memory = '...' }` in a custom
`-c` config).

## Container images and caching

`-profile mcw_rcc` enables Apptainer with `autoMounts = true` and binds
`/scratch` and `/hpc` into every container. Apptainer 1.x is fully
compatible with images built for Singularity, so nf-core images pull
and run unchanged.

**You must point two apptainer cache variables at `/scratch` before
launching Nextflow.** Home directories on this cluster are ~94 GB and
typically near-full; the OCI → SIF conversion that apptainer performs
during a fresh image pull writes multi-gigabyte temp blobs and will
exhaust home in a single run if not redirected.

```bash
# Apptainer's own blob cache and temp dir (used during pull/build):
export APPTAINER_CACHEDIR=/scratch/g/$USER/.apptainer/cache
export APPTAINER_TMPDIR=/scratch/g/$USER/.apptainer/tmp

# Create them once — apptainer fails if APPTAINER_TMPDIR doesn't exist:
mkdir -p "$APPTAINER_CACHEDIR" "$APPTAINER_TMPDIR"
```

The profile already sets `apptainer.cacheDir` (the persistent `.img`
store, equivalent to `NXF_APPTAINER_CACHEDIR`) to
`/scratch/g/$USER/nf-apptainer-cache`, so you do not need to export
that one. The two variables above must still be exported in your
submission script, because the driver-side pull happens before
Nextflow's `env { }` scope takes effect.

## Running on a compute node, not the login node

`nextflow` itself coordinates the run and must stay alive for hours to
days. Submit it as a SLURM job rather than running it on a login node.
A minimal submission script:

```bash
#!/bin/bash
#SBATCH --job-name=nf-driver
#SBATCH --partition=normal
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=72:00:00

module load nextflow/25.10.2
module load apptainer/1.4.1

export APPTAINER_CACHEDIR=/scratch/g/$USER/.apptainer/cache
export APPTAINER_TMPDIR=/scratch/g/$USER/.apptainer/tmp
mkdir -p "$APPTAINER_CACHEDIR" "$APPTAINER_TMPDIR"

nextflow run nf-core/<pipeline> \
    -profile mcw_rcc \
    --input /scratch/g/$USER/samplesheet.csv \
    --outdir /scratch/g/$USER/results \
    -work-dir /scratch/g/$USER/work
```

Keep `-work-dir` under `/scratch` (large, fast GPFS) rather than under
your home directory.

## Notes

- The cluster previously offered a `singularity` module; it was
  replaced by `apptainer/1.4.1`. Existing scripts that ran with
  `-profile singularity` plus `module load singularity` should switch
  to `-profile mcw_rcc`.
- GPU support is provided via the `process_gpu` label. Pipelines that
  do not declare GPU labels will not use GPU nodes.
- Open-OnDemand sessions run on the `ood` partition (12 h max) and are
  not used by this profile for pipeline workloads.
