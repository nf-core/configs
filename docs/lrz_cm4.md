# nf-core/configs: LRZ CM4 Configuration

## About

All nf-core pipelines have been successfully configured for use on the CoolMuc4 cluster that is provided by the [Leibniz Rechenzentrum (LRZ)](https://lrz.de/) of the Bavarian Academy of Sciences, located in Garching, Germany..

> NB: You will need an account to use the LRZ Linux cluster.

## Usage

To use, run the pipeline with `-profile lrz_cm4`. This will download and launch the [`lrz_cm4.config`](../conf/lrz_cm4.config).

We recommend using nextflow >= 25.04.2 with apptainer (1.3.4) for containerization.
These are available as modules (please confirm the module name using `module avail`):

```bash
## Load Nextflow and apptainer environment modules
module load nextflow/25.04.2 apptainer/1.3.4
```

## Details

> NB: Please note that running nextflow on a login node is not permitted.

> NB: Please note that it is not possible to run nextflow with the SLURM executor in a job, compute nodes cannot submit jobs.

Instead of having `nextflow` run on a login node and submit jobs to the `SLURM` scheduler, the `nextflow` head job, coordinating the workflow, has to run inside a `SLURM`-job and job scheduling is done 'inside' the `SLURM` job using the `flux` or `local` executors. This is outlined [here](https://doku.lrz.de/job-farming-with-slurm-11481293.html) and implemented in `-profile lrz_cm4`. By default, this uses the `flux` executor, if you would prefer to use the `local` executor, please use `-profile lrz_cm4,local`. Independent of the executor used, task memory limits will be set through apptainer.

### Serial / cm4_tiny / terramem

Run nextflow inside a SLURM job using either `local` or `flux` for job scheduling within the SLURM allocation.
In case the `cm4_tiny` partition of the `cm4` cluster, the `serial` partition of `serial` cluster, or `terramem` partition of the `inter` cluster is to be used (i.e. if the job requires less 1 full node) please prepare a script similar to the one below:

> NB: This config assumes that memory is not requested explicitly, and computes the memory resourceLimit as 4.5GB * number of CPUs

```bash
#! /bin/bash
#SBATCH -D .
#SBATCH -J nextflow_run
#SBATCH --get-user-env
#SBATCH -M cm4                  # for serial: serial here; for terramem: inter
#SBATCH -p cm4_tiny             # for serial: serial here; for terramem: terramem_inter
#SBATCH --cpu-per-task=100      # Please see https://doku.lrz.de/job-processing-on-the-linux-cluster-10745970.html for partition limits
#SBATCH --ntasks=1
#SBATCH --export=NONE
#SBATCH --time=24:00:00

module load flux

flux start
nextflow run nf-core/rnaseq \
    -profile test,lrz_cm4
```

In case the scheduling should not be done via flux, but local, please use:

```bash
#! /bin/bash
#SBATCH -D .
#SBATCH -J nextflow_run
#SBATCH --get-user-env
#SBATCH -M cm4                  # for serial: serial here; for terramem: inter
#SBATCH -p cm4_tiny             # for serial: serial here; for terramem: terramem_inter
#SBATCH --cpu-per-task=100      # Please see https://doku.lrz.de/job-processing-on-the-linux-cluster-10745970.html for partition limits
#SBATCH --ntasks=1
#SBATCH --export=NONE
#SBATCH --time=24:00:00

nextflow run nf-core/rnaseq \
    -profile test,lrz_cm4,local
```

#### cm4_std

> NB: If more than one node is used, make sure to use flux for execution.

On the `cm4_std` partition of the `cm4` cluster, full (exclusive) nodes are scheduled. Use

```bash
#! /bin/bash
#SBATCH -D .
#SBATCH -J nextflow_run
#SBATCH --get-user-env
#SBATCH -M cm4              # if cores <= 112 go to cm4_tiny
#SBATCH -p cm4_std          # if cores <= 112 go to cm4_tiny
#SBATCH --qos=cm4_std       # if tiny, QOS is not required
#SBATCH --nodes=2           # 2 nodes (maximum: 4)
#SBATCH --ntasks-per-node=1
#SBATCH --export=NONE
#SBATCH --time=24:00:00

module load flux

flux start
nextflow run nf-core/rnaseq \
    -profile test,lrz_cm4
```

this script is to be submitted via `sbatch`.
The correct resource limits are applied based on the number of requested nodes (which are fetched from the environment).
