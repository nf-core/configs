# nf-core/configs: ku_sund_dangpu configuration

All nf-core pipelines have been successfully configured for use on the DANGPU at the
Novo Nordisk Foundation Center for Stem Cell Medicine (reNEW) and the Novo Nordisk Foundation Center for Protein Research (CPR) at the University of Copenhagen.

To use, run the pipeline with `-profile ku_sund_dangpu`. This will download and launch the [`ku_sund_dangpu.config`](../conf/ku_sund_dangpu.config) which has been pre-configured with a setup suitable for the DANGPU.

## Prepare the environment

Start a tmux session or a screen session. You can start a tmux session like this:

```
tmux new-session -s <session-name>
```

Before running the pipeline you will need to load Nextflow and Singularity using the environment module system on DANGPU.
Within the created session load Nextflow and Singularity and set up the environment by issuing the commands below:

```bash
## Load Nextflow and Singularity environment modules
module purge
module load java/11.0.15 nextflow/22.04.4 singularity/3.8.0

# set up bash environment variables for memory
export NXF_OPTS='-Xms1g -Xmx4g'
export NXF_HOME=/projects/dan1/people/${USER}/cache/nxf-home
export NXF_TEMP=/scratch/tmp/${USER}
export NXF_SINGULARITY_CACHEDIR=/projects/dan1/people/${USER}/cache/singularity-images
```

Create the user-specific nextflow directories if they don't exist yet:

```
mkdir -p $NXF_SINGULARITY_CACHEDIR
mkdir -p $NXF_HOME
mkdir $NXF_TEMP
```

## How to run a pipeline with institution profile

To download and test a pipeline for the first time, use the `-profile test` and specify `--outdir`. It is a good practice to use the pipeline version with specifying `-r` each time you run a pipeline.

For example to run rnaseq:

```
nextflow run nf-core/rnaseq -r 3.8.1 -profile test,ku_sund_dangpu --outdir <name-of-output-directory>
```

To run a pipeline:

```
nextflow run nf-core/rnaseq  -r 3.8.1 -profile ku_sund_dangpu --outdir <name-of-output-directory>
```

## Notes

Note that normally on dangpu server you are required to run resource-intensive commands with slurm, but at ku_sund_dangpu profile we have pre-configured slurm to be the resource manager within the `ku_sund_dangpu profile`. Just make sure that the pipeline is run within a tmux session or within a screen session.
