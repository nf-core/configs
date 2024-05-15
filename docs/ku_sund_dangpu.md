# nf-core/configs: ku_sund_dangpu configuration

All nf-core pipelines have been successfully configured for use on the DANGPU server at the Novo Nordisk Foundation Center for Stem Cell Medicine (reNEW) at the University of Copenhagen.

To use the institution profile, run the pipeline with `-profile ku_sund_dangpu`. This will download and launch the [`ku_sund_dangpu.config`](../conf/ku_sund_dangpu.config) which has been pre-configured with a setup suitable for the DANGPU.

## Prepare the environment

Start a tmux session or a screen session. You can start a tmux session like this:

```
tmux new-session -s <session-name>
```

Before running the pipeline you will need to load Nextflow and Singularity using the environment module system on DANGPU.
Within the created session load Nextflow and Singularity and set up the environment by issuing the commands below:

first clear the environment and load Nextflow environment modules:

```bash
module purge
module load dangpu_libs openjdk/20.0.0 nextflow/23.04.1.5866
module load singularity/3.8.0 python/3.7.13 nf-core/2.7.2
```

for loading the older module nextflow/22.10.6 you can use `module load dangpu_libs java/11.0.15 nextflow/22.10.6` instead of `module load dangpu_libs openjdk/20.0.0 nextflow/23.04.1.5866`.

Next, set up bash environment variables for memory. (You can avoid repeatedly writing this every time by placing this code chunk into ${HOME}/.bash_profile and ${HOME}/.bashrc)

```bash
export NXF_OPTS='-Xms1g -Xmx4g'
export NXF_HOME=/projects/dan1/people/${USER}/cache/nxf-home
export NXF_TEMP=/scratch/temp/${USER}
export NXF_WORK=/scratch/temp/${USER}
export NXF_SINGULARITY_CACHEDIR=/projects/dan1/people/${USER}/cache/singularity-images
```

Create the user-specific nextflow directories if they don't exist yet. You have to do this only first time you run a nf-core pipeline.

```
mkdir -p $NXF_SINGULARITY_CACHEDIR
mkdir -p $NXF_HOME
mkdir $NXF_TEMP
```

## How to run a pipeline with institution profile

To download and test a pipeline for the first time, use the `-profile test` and specify `--outdir`. It is a good practice to use the pipeline version with specifying `-r` each time you run a pipeline. `-r` refers to a revision version and is useful to ensure reproducibility when rerunning the pipeline. You can read more on nf-core pipeline reproducibility [here](https://nf-co.re/rnaseq/3.10.1/usage#reproducibility)

For example to run rnaseq:

```
nextflow run nf-core/rnaseq -r 3.14.0 -profile test,ku_sund_dangpu --outdir <name-of-output-directory>
```

To run a pipeline:

```
nextflow run nf-core/rnaseq  -r 3.14.0 -profile ku_sund_dangpu --outdir <name-of-output-directory> --input <name-of-input-csv-file>
```

## Notes

Note that normally on dangpu server you are required to run resource-intensive commands with slurm, but at ku_sund_dangpu profile we have pre-configured slurm to be the resource manager within the `ku_sund_dangpu profile`. Just make sure that the pipeline is run within a tmux session or within a screen session.

Start a new session and enter the vitual screen named `mysessionname`:

```bash
tmux new-session -s mysessionname

# load modules
# define variables
# run nfcore pipeline here
```

Detach a session use control+B and then press d.

To attach a previously detached session again:

```bash
tmux atttach-session -t mysessionname
```

To exit a tmux session when the job is done:

```bash
exit
```
