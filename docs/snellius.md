# nf-core/configs: Snellius HPC common Configuration

To use, run the pipeline with `-profile snellius`. This will download and launch the snellius.config which has been pre-configured with a setup suitable for the Snellius cluster.

- The nfcore pipeline MAG has been tested on Snellius

## snellius documentation
- https://servicedesk.surf.nl/wiki/display/WIKI/System+details

##  accounting information used in this config
- https://servicedesk.surf.nl/wiki/display/WIKI/Snellius+partitions+and+accounting

## Before running a pipeline

- You will need an account to use the Snellius HPC cluster in order to run the pipeline.
- Make sure that Nextflow is installed (recommended to install in your project space).
- make sure the 2024 module is loaded
- check the java version

```
# openjdk version "21.0.5" 2024-10-15 LTS or higher
$ java -version
```

- optional: install nf-core tools in your own environment



```
$ module load 2024
```
## snellius specific scratch config
- Don't store intermediate files in your project space, use the scratch
- You will need to specify some environment variables to specify scratch and temporary locations
- You will need to specify an Apptainer cache directory in your ~./bashrc. This will store your container images in this cache directory without repeatedly downloading them every time you run a pipeline. Since space on home directory is limited, using your project file system is recommended. e.g. somewhere in your project space.
- You can also use environment variables in you sbatch script

## environment variables, replace where appropriate

```
# assume you install nexflow in ${PROJECTSPACE}/nextflow
export PROJECT=<your project name>
export PROJECTSPACE=/projects/0/<your project space>
export WORKDIR="/scratch-shared/${USER}/${PROJECT}"
export TMPDIR="/scratch-local/${USER}/${PROJECT}"

export NXF_APPTAINER_CACHEDIR="${PROJECTSPACE}/nextflow/containers"
export NXF_SINGULARITY_CACHEDIR=${NXF_APPTAINER_CACHEDIR}}
export NXF_OPTS="-Xms4g -Xmx28g"
export NXF_CACHE_DIR=${WORKDIR}
export NXF_TEMP=${TMPDIR}
export NXF_WORK=${WORKDIR}

mkdir $NXF_APPTAINER_CACHEDIR
mkdir $NXF_TEMP
mkdir $NXF_WORK

module load 2024

# optional, load the environment in which you installed nf-core tools python modules
# module load Mamba/24.9.0-0
# mamba activate ${PROJECTSPACE}/nextflow/env_nf
# submitting an nf-core pipeline will consume 16 SBU / h due to the smallest possible share on a node
