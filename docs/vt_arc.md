# nf-core/configs: Virginia Tech ARC TinkerCliffs Configuration

nf-core pipelines have been configured for use on the TinkerCliffs cluster at [Virginia Tech Advanced Research Computing (ARC)](https://arc.vt.edu).

To use, run the pipeline with `-profile vt_arc` and your ARC allocation account:

```bash
module load Nextflow/25.10.4 apptainer/1.4.0
cd /scratch/$USER
nextflow run nf-core/<pipeline> -profile vt_arc --arc_account <account> --outdir /scratch/$USER/<run>
```

The profile submits each process as a SLURM job to the `normal_q` partition and runs it in an Apptainer container. Images are cached in `/scratch/$USER/.apptainer/nxf` (override with `NXF_APPTAINER_CACHEDIR`). Launch from `/scratch/$USER` so the `work/` directory lands on scratch rather than in your home quota.

## Account

`--arc_account` is required. List the accounts you belong to with:

```bash
sacctmgr -nP show assoc user=$USER format=Account | sort -u
```

## Running the head job

Run the Nextflow head job inside an allocation rather than on a login node, for example:

```bash
#!/bin/bash
#SBATCH --partition=normal_q
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=7-00:00:00
module load Nextflow/25.10.4 apptainer/1.4.0
cd /scratch/$USER
nextflow run nf-core/<pipeline> -profile vt_arc --arc_account "$SLURM_JOB_ACCOUNT" --outdir /scratch/$USER/<run>
```

Submit it with `sbatch --account=<account> run.sbatch`. The head job asks for the full 7-day limit of `normal_q` because the pipeline stops when the head job does; if it is stopped anyway, add `-resume` to the `nextflow run` line in the script and submit it again.

## Resource limits

`resourceLimits` is set to the largest `normal_q` node (128 cores, 1000 GB) and the 7-day wall time of the default QoS. A site profile takes precedence over the `test` profile's limits, so `-profile test,vt_arc` runs test tasks at their normal resource requests.

:::note
You need an ARC account and an allocation to use this profile. See <https://arc.vt.edu> for access.
:::
