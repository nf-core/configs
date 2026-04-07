# nf-core/configs: LRZ CM4 Configuration

## About

All nf-core pipelines have been successfully configured for use on the CoolMuc4 cluster that is provided by the [Leibniz Rechenzentrum (LRZ)](https://lrz.de/) of the Bavarian Academy of Sciences, located in Garching, Germany.

> NB: You will need an [account to use the LRZ Linux cluster](https://doku.lrz.de/access-and-login-to-the-linux-cluster-10745974.html).

## General usage

> NB: Please note that running nextflow on a login node is not permitted.

> NB: Please note that it is not possible to run nextflow with the SLURM executor in a job, compute nodes cannot submit jobs.

Instead of having `nextflow` run on a login node and submit jobs to the `SLURM` scheduler, the `nextflow` head job, coordinating the workflow, has to run inside a `SLURM`-job and job scheduling is done 'inside' the `SLURM` job using the `flux` or `local` executors. This is outlined [here](https://doku.lrz.de/job-farming-with-slurm-11481293.html) and implemented in `-profile lrz_cm4`. This profile detects if the `flux` executor has been started, and will switch executor accordingly. Example `sbatch` scripts are provided [below](#examples).

## Setup

To use, run the pipeline with `-profile lrz_cm4`. This will download and launch the [`lrz_cm4.config`](../conf/lrz_cm4.config).

We recommend using nextflow >= 25.04.2 with apptainer (>=1.3.4) for containerization.

These are available as modules (please confirm the module name using `module avail`):

```bash
## Load Nextflow, apptainer, and flux environment modules
module load nextflow/25.04.2 apptainer/1.3.4 flux
```

In case additional flexibility / other versions are needed, a conda environment containing the required packages is also an option.
This could be done as follows for a temporary environment on `SCRATCH_DSS`:

```bash
module load micromamba
export ENV_PATH=$SCRATCH_DSS/env_nfcore # Adjust path as desired
micromamba create \
    -p $ENV_PATH \
    -c conda-forge \
    -c bioconda \
    nextflow nf-core apptainer flux-core flux-sched
micromamba activate $ENV_PATH
```

For a more persistent environment in `$HOME` consider:

```bash
module load micromamba
micromamba create \
    -n nf-env \
    -c conda-forge \
    -c bioconda \
    nextflow nf-core apptainer flux-core flux-sched
micromamba activate nf-env
```

## Considerations

While testing can be done with partial nodes, or interactive jobs, we recommend requesting at least one full node for production runs. Both `local` and `flux` executor can be used for single-node runs, multi-node runs **must** use `flux` to make use of the additional resources. Please note that during testing, we observed that the same test-run of `nf-core/rnaseq` took around 11h with the `local` executor, and 8h with the `flux` executor, which we largely attribute to more efficient scheduling.

<details markdown="1">
<summary>Test setup</summary>

The test was performed using the `test_full` profile of `nf-core/rnaseq`, with a customized samplesheet, containing a total of 24 samples.
We compared the performance of `local` and `flux` on a single node, and scaling of flux across 1, 2, or 4 nodes.

| Executor | # Nodes | Time     |
| -------- | ------- | -------- |
| local    | 1       | 11:06:57 |
| flux     | 1       | 08:15:11 |
| flux     | 2       | 04:45:39 |
| flux     | 4       | 03:36:09 |

This is a short summary of a more extensive test, kindly conducted by Martin Ohlerich at LRZ. If you would like to learn more, please take a look [here](https://doku.lrz.de/nf-core-experience-report-2238563906.html)

</details>

## Examples

### Full node(s)

When running a nextflow pipeline on one or more full node(s), we advise to use `flux`.
There are some specific settings required to make `flux` use all available logical processing units when running inside a `SLURM` job, which are set correctly in the example script. The script below requests 4 nodes.

```bash
#SBATCH -D .
#SBATCH -o log.%x.%j
#SBATCH -J nf_flux_hwt_4N
#SBATCH --get-user-env
#SBATCH -M cm4
#SBATCH -p cm4_std
#SBATCH --qos=cm4_std
#SBATCH --nodes=4-4 # 1-1, 2-2, 3-3, or 4-4
#SBATCH --ntasks-per-node=2
#SBATCH -c 112
#SBATCH --hint=multithread
#SBATCH --export=none
#SBATCH --time=1-00:00:00 # Max of 2 days

module load nextflow/25.04.2 apptainer/1.3.4 flux
# OR
# Please use either modules or a conda environment
conda activate nf-env

# Write commands to heredoc to pass to flux start
# For runs that are not using the test profile, modify accordingly.
# The complete nextflow command needs to be here.

cat > workflow.sh << EOT
nextflow run nf-core/rnaseq \
    -profile test,lrz_cm4
EOT

# Make file executable
chmod u+x workflow.sh

# Start flux via srun
srun --export=all --mpi=none flux start ./workflow.sh
```

<details markdown="1">
<summary>Usage of logical CPU with flux</summary>

By default, `flux` discovers physical CPU. To make use of the logical CPU available, the following settings are required:

- `SLURM` has to use multithreading
- two `flux`-brokers are required per node, each serving half of the logical CPU (there are two logical per physical CPU). For this reason, we start with `--ntasks-per-node=2`
- `flux` must not be cpu-bound by `SLURM`/`srun`.

</details>

### Partial node

Run nextflow inside a SLURM job using either `local` or `flux` for job scheduling within the SLURM allocation. We recommend runs on less than 1 full node only for testing purposes.
In case the `cm4_tiny` partition of the `cm4` cluster, the `serial` partition of `serial` cluster, or `terramem` partition of the `inter` cluster is to be used (i.e. if the job requires less 1 full node) please prepare a script similar to the one below:

> NB: This config assumes that memory is not requested explicitly, and computes the memory resourceLimit as 4.5GB \* number of CPUs

```bash
#SBATCH -D .
#SBATCH -o log.%x.%j
#SBATCH -J nf_partial_node
#SBATCH --get-user-env
#SBATCH -M cm4
#SBATCH -p cm4_tiny
#SBATCH --qos=cm4_tiny
#SBATCH -c 24
#SBATCH --hint=multithread
#SBATCH --export=none
#SBATCH --time=1-00:00:00 # Max of 2 days

nextflow run nf-core/rnaseq \
    -profile test,lrz_cm4
```
