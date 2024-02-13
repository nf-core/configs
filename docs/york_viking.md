# nf-core/configs: York University Viking Configuration

This config is for running nf-core pipelines, either directly on Viking or via tower.nf

To use, run the pipeline with `-profile york_viking`. This will download and launch the [`york_viking.config`](../conf/york_viking.config) which has been pre-configured with a setup suitable for the Viking cluster.

I recommend running Nextflow via tower.nf, in which case make sure to include the **york_viking** profile within the pipeline.

However, should you need to run it directly on the HPC follow the guidance below.

## Loading the required modules

Before running the pipeline you will need to load Nextflow and Singularity using the environment module system on the Viking cluster. You can do this by issuing the commands below:

```bash
## Load Nextflow and Singularity environment modules
module purge
module load Apptainer
module load Nextflow/23.10.0
```

You may want to add those module load commands to your shell configuration file if you use them often.

## Environmental variables

You need to make sure that the following environmental variables are set (pointing to appropriate dirs):

```bash
export NXF_HOME="/mnt/scratch/<PATH_TO_FOLDER>"
export NXF_CONDA_CACHEDIR="/mnt/scratch/<PATH_TO_FOLDER>"
export NXF_TEMP="/mnt/scratch/<PATH_TO_FOLDER>"
export NXF_APPTAINER_CACHEDIR="/mnt/scratch/<PATH_TO_FOLDER>"
export APPTAINER_TMPDIR="/mnt/scratch/<PATH_TO_FOLDER>"
export APPTAINER_CACHEDIR="/mnt/scratch/<PATH_TO_FOLDER>"
```

## Running the nextflow pipeline

Create a params.json file with the desired parameters for the pipeline. Place this file in the folder from which you wish to run the Nextflow pipeline. Then using a screen session:

```bash
screen -S run-nextflow
nextflow run nf-core/<pipeline_name> -profile york_viking -name <run_name> -params-file params.json -r <nf-core revision>
```
