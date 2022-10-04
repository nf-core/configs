# nf-core/configs: ku_sund_dangpu configuration

All nf-core pipelines have been successfully configured for use on the DANGPU at the
Novo Nordisk Foundation Center for Stem Cell Medicine (reNEW) and the Novo Nordisk Foundation Center for Protein Research (CPR) at the University of Copenhagen.

To use, run the pipeline with `-profile ku_sund_dangpu`. This will download and launch the [`ku_sund_dangpu.config`](../conf/ku_sund_dangpu.config) which has been pre-configured with a setup suitable for the DANGPU.

## Modules

Before running the pipeline you will need to load Nextflow and Singularity using the environment module system on DANGPU. You can do this by issuing the commands below:

```bash
## Load Nextflow and Singularity environment modules
module purge
module load java/11.0.15 nextflow/22.04.4 singularity/3.8.0
# alternative modules for older nextflow version (v.21) that works with java 8:
# module load jdk/1.8.0_291 nextflow/21.04.1.5556 singularity/3.8.0
export NXF_OPTS='-Xms1g -Xmx4g'
export NXF_HOME=/projects/dan1/people/${USER}/cache/nxf-home
export NXF_TEMP=/scratch/tmp
export NXF_SINGULARITY_CACHEDIR=/projects/dan1/people/${USER}/cache/singularity-images
```

Create the user-specific nextflow directories if they don't exist yet:

```
mkdir $NXF_SINGULARITY_CACHEDIR
mkdir $NXF_HOME
```

Finally, download and test the pipeline of choice using the `-profile ku_sund_dangpu`. Note that normally you would run resource-intensive commands with slurm, but in case of nf-core pipelines you do not have to do this: we have pre-configured slurm to be the resource manager within the `ku_sund_dangpu profile`. Just make sure that the pipeline is run within a tmux session.

```
nextflow run nf-core/rnaseq -profile test,ku_sund_dangpu
```
