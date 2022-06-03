# nf-core/configs: Bioinfo Genotoul Configuration

All nf-core pipelines have been successfully configured for use on the Bioinfo Genotoul cluster at the INRA toulouse.

To use, run the pipeline with `-profile genotoul`. This will download and
launch the [`genotoul.config`](../conf/genotoul.config) which has been
pre-configured with a setup suitable for the Bioinfo Genotoul cluster.

Using this profile, a docker image containing all of the required software
will be downloaded, and converted to a Singularity image before execution
of the pipeline. Images are stored for all users in following directory `/usr/local/bioinfo/src/NextflowWorkflows/singularity-img/`.

## Running the workflow ib the Genologin cluster

Before running the pipeline you will need to load Nextflow and
Singularity using the environment module system on Genotoul. You can do
this by issuing the commands below:

Once connected on our frontal node :

```bash
# Login to a compute node
srun --mem=4G --pty bash
```

Setup default nextflow and singularity home directory (to be done only one time):

```bash
sh /usr/local/bioinfo/src/NextflowWorkflows/create_nfx_dirs.sh
```

Load environment :

```bash
module purge
module load bioinfo/nfcore-Nextflow-v19.04.0
```

Try a test workflow (for example the methylseq workflow) :

```bash
nextflow run nf-core/methylseq -profile genotoul,test
```

Create launch script `nfcore-rnaseq.sh` :

```bash
#!/bin/bash
#SBATCH -p workq
#SBATCH -t 1:00:00  #time in hour
#SBATCH --mem=4G
#SBATCH --mail-type=BEGIN,END,FAIL

module load bioinfo/nfcore-Nextflow-v19.04.0
nextflow run nf-core/methylseq -profile genotoul,test
```

Launch on the cluster with sbatch:

```bash
sbatch nfcore-rnaseq.sh
```

## Mounted directory

By default, available mount points are:

- /bank
- /home
- /save
- /work
- /work2

To have access to specific other mount point (such as nosave or project)
you can add a config profile file with option `-profile` and which contain:

```bash
singularity.runOptions = '-B /directory/to/mount'
```

## Databanks

A local copy of several genomes are available in `/bank` directory. See
our [databank page](http://bioinfo.genotoul.fr/index.php/resources-2/databanks/)
to search for your favorite genome.

> NB: You will need an account to use the HPC cluster on Genotoul in order
> to run the pipeline. If in doubt see [http://bioinfo.genotoul.fr/](http://bioinfo.genotoul.fr/).
