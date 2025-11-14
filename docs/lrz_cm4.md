# nf-core/configs: LRZ CM4 Configuration

## About

All nf-core pipelines have been successfully configured for use on the CoolMuc4 cluster that is provided by the [Leibniz Rechenzentrum (LRZ)](https://lrz.de/) of the Bavarian Academy of Sciences, located in Garching, Germany..

> NB: You will need an account to use the LRZ Linux cluster.

## Usage

To use, run the pipeline with `-profile lrz_cm4,<tiny_flux,std_flux,serial_slurm,terramem_flux>`. This will download and launch the [`biohpc_gen.config`](../conf/biohpc_gen.config), together with the specific sub-profile.

We recommend using nextflow >= 25.04.2 with apptainer (1.3.4) for containerization.
These are available as modules (please confirm the module name using `module avail`):

```bash
## Load Nextflow and apptainer environment modules
module load nextflow/25.04.2 apptainer/1.3.4
```

## Details

### Serial

CM4 contains a `serial` cluster, which allows for up to 16 physical CPUs and up to 24 hours (`serial_std`) or 7 days (`serial_long`) of job walltime.
The `serial` profile (`-profile lrz_cm4,serial`) will handle submission into the correct partition based on requested time. In this profile, `SLURM` is used for scheduling of the individual tasks, and the `nextflow` head job needs to run persistently on the login node, to be able to submit jobs. Please limit resource usage by the `nextflow` head-job, limits can be set through the environment: i.e. `export NXF_OPTS='-Xms1g -Xmx4g'`.
`serial` has a maximum queue size of 96 running and 200 submitted jobs.

Example command:

```bash
nextflow run nf-core/rnaseq -profile test,lrz_cm4,serial`
```

There are situations where 16 CPUs per job are insufficient. For these, the `cm4` cluster can be used, although this requires a different setup.

### CM4

Running `nextflow` on the `cm4` cluster, which is designed to handle large, potentially node-spanning jobs, requires a different approach.

Instead of having `nextflow` submit jobs to the `SLURM` scheduler, the `nextflow` head job, coordinating the workflow, is run inside a (large) `SLURM`-job and job scheduling is done 'inside' the `SLURM` job using the `flux` executor. This is outlined [here](https://doku.lrz.de/job-farming-with-slurm-11481293.html).

This means that `nextflow` is not invoked on the login-node, but submitted via SLURM. Below are example scripts for the different clusters:

#### std

On `cm4_std` full (exclusive) nodes are scheduled. Use `-profile lrz_cm4,exclusive`

```bash
#! /bin/bash
#SBATCH -D .
#SBATCH -J nextflow_run
#SBATCH --get-user-env
#SBATCH -M cm4          #    if cores <= 112 go to cm4_tiny
#SBATCH -p cm4_std      #    if cores <= 112 go to cm4_tiny
#SBATCH --qos=cm4_std   #    if tiny, QOS is not required
#SBATCH --nodes=2       #    2 nodes (maximum: 4)
#SBATCH --ntasks-per-node=1
#SBATCH --export=NONE
#SBATCH --time=24:00:00

module load flux

flux start
nextflow run nf-core/rnaseq \
    -profile test,lrz_cm4,exclusive
```

this script is to be submitted via `sbatch`.
The correct resource limits are applied based on the number of requested nodes (which are fetched from the environment).

CPU in the table above refers to logical cores.

#### tiny

In case the `tiny` partition of `CM4` is to be used (i.e. if the job requires less 1 full node), this uses the same 'flux-in-slurm' setup, but requires the `shared` profile. Below is an example sbatch script:

```bash
#! /bin/bash
#SBATCH -D .
#SBATCH -J nextflow_run
#SBATCH --get-user-env
#SBATCH -M cm4_tiny
#SBATCH -p cm4_tiny
#SBATCH --cpu 100 # Can be 17-112
#SBATCH --mem 96G # Can be up to 488, or left empty for 2.1G / CPU
#SBATCH --export=NONE
#SBATCH --time=24:00:00

module load flux

flux start
nextflow run nf-core/rnaseq \
    -profile test,lrz_cm4,shared
```

### Terramem

`terramem` is part of the `inter` cluster, and accepts only a single job, with node shared, making submission via `SLURM` impractical.
The `lrz_cm4,shared` profile can be used to run workflows on the terramem node, similar to cm4_tiny:

```bash
#! /bin/bash
#SBATCH -D .
#SBATCH -J nextflow_run
#SBATCH --get-user-env
#SBATCH -M inter
#SBATCH -p terramem_inter
#SBATCH --cpu 12 # Can be 1-96 (physical; each with 2 threads)
#SBATCH --mem 20000G # Can be up to 5.9 TB (around 6 TB/cpu)
#SBATCH --export=NONE
#SBATCH --time=24:00:00 # Can be up to 240h

module load flux

flux start
nextflow run nf-core/rnaseq \
    -profile test,lrz_cm4,shared
```
