# nf-core/configs: Institute of Cancer Research (Alma HPC) Configuration

Deployment and testing of nf-core pipelines on the Alma cluster is on-going in collaboration between the RSE team and research groups.

To run an nf-core pipeline on Alma, run the pipeline with `-profile icr_alma`. This will download and launch the [`icr_alma.config`](../conf/icr_alma.config) which has been pre-configured with a setup suitable for the Alma HPC cluster.

Before running the pipeline you will need Nextflow available in your environment. The preferred way is to create a conda or mamba environment (you only need to do this once) which you activate.

```bash
## Create and activate mamba environment
mamba create --name mamba_nf -c bioconda nextflow nf-core
mamba activate mamba_nf
```

Singularity is installed on the compute nodes of Alma, but not the login nodes. There is no module for Singularity.

The `icr_alma` profile uses a shared, read-only Singularity image library at `/data/rds/shared/SINGULARITY/nextflow`. Nextflow uses images from this library when they are available. Any image not in the library is pulled into your own cache: by default `<workDir>/singularity`, or set `NXF_SINGULARITY_CACHEDIR` (e.g. in your `~/.bashrc`) to a directory you own to reuse images across runs.

## Resource requests on Alma

Alma `compute` nodes have 48 CPUs, a maximum of 8042 MB of memory per CPU and a maximum walltime of 5 days. The scheduler's submit rules only accept jobs that request **1, 2, 4, 6, 8, 12, 16, 24 or 48 CPUs per task**, and reject requests above 8042 MB per CPU.

The `icr_alma` profile adapts every task to these rules automatically: it requests enough CPUs to fit the task's memory at no more than 8042 MB per CPU, rounds the CPU count up to the next allowed value, and requests at least 1 GB per CPU. A task may therefore be allocated more CPUs or memory than the pipeline asked for. Individual tasks are capped at 48 CPUs and 376 GB.

If you set `process.clusterOptions` in your own config, it replaces this logic, so make sure your requests follow the same rules. In your own `sbatch` scripts (for example for the Nextflow head job), use an allowed `--cpus-per-task` value with `--mem-per-cpu` rather than `--mem`.

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. The `icr_alma` profile does not delete the `work/` directory automatically, so that runs can be resumed with `-resume`. Once you are happy with the results, delete the `work/` directory manually to free up space.

> NB: Nextflow will need to submit the jobs via SLURM to the HPC cluster. This can be done from an interactive or a normal job. If in doubt contact Scientific Computing.

Alma has a master-worker partition for the long running nextflow manager which spawns jobs to the compute node. A typical nextflow job will run a batch script through sbatch which will run on the master-worker thread spawning the jobs.

Command to run the nextflow job:

```bash
sbatch my-nextflow.sh
```

Contents of my-nextflow.sh

```
#!/bin/bash
#SBATCH --job-name=nf-username
#SBATCH --output=slurm_out.txt
#SBATCH --partition=master-worker
#SBATCH --ntasks=1
#SBATCH --time=1:00:00
#SBATCH --mem-per-cpu=4000

nextflow run nf-core/sarek  -profile icr_alma,test --outdir ./results
```
