# nf-core/configs: McCleary Configuration

All nf-core pipelines have been successfully configured for use on the [Yale University McCleary cluster](https://docs.ycrc.yale.edu/clusters/mccleary/). To use, run the pipeline with -profile mccleary.

NB: You will need an account to use the HPC cluster on the McCleary cluster in order to run the pipeline. If in doubt contact IT. To use nf-core pipelines on McCleary:

1. Install [Nextflow](https://www.nextflow.io/docs/latest/install.html) for your user. Move the Nextflow executable to a folder in your `$PATH` variable (e.g. `~/bin`).

```
module load Java/17.0.4
curl -s https://get.nextflow.io | bash
```

2. Submit your pipeline script via `sbatch script.sh`. With the following script. Update `--job-name`,--time`, and `--partition` as needed for your head job. 2 CPUs and 5GB of memory is usually sufficient for the Nextflow head job but you can also update as needed.

```
#! /bin/bash

#SBATCH --job-name=nf-core
#SBATCH --out="slurm-%j.out"
#SBATCH --time=07-00:00:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=5G
#SBATCH --mail-type=ALL
#SBATCH --partition=week

module load Java/17.0.4
export NXF_WRAPPER_STAGE_FILE_THRESHOLD='40000'

nextflow pull nf-core/<pipeline> -r <release>
nextflow run nf-core/<pipeline> -r <release> \
-profile mccleary \
--outdir "results" \
...
```


## Pipeline Specific profiles

There are no specific profiles added for now
