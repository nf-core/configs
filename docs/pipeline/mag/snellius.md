# nf-core/configs: Snellius HPC Configuration for the MAG pipeline


- You will need to specify an Apptainer cache directory in your ~./bashrc. This will store your container images in this cache directory without repeatedly downloading them every time you run a pipeline. Since space on home directory is limited, using lustre file system is recommended. e.g. somewhere in your project space.
- You can also use environment variables in you sbatch script

## sbatch example
```
#!/bin/bash
#-----------------------------Mail address-----------------------------
#SBATCH --mail-user=<your mail address>
#SBATCH --mail-type=ALL
#-----------------------------Output files-----------------------------
#SBATCH --output=/projects/0/<your project space>/jobs/output_%j.out
#SBATCH --error=/projects/0/<your project space>/jobs/error_%j.out
#-----------------------------Required resources-----------------------
# this defines where the nextflow process runs (as separate job)
# 16 cores is the minimum partition with 28 GB memory
#SBATCH --cpus-per-task 16
#SBATCH --partition=thin
#SBATCH --time=5-00:00:00
#SBATCH --job-name=nf-core-mag

source ~/.bashrc
# path to your nextflow
export PATH=/projects/0/<your project space>/nextflow/:$PATH

# base settings to your project space on Snellius
export PROJECTSPACE=/projects/0/<your project space>
export EMAIL="<your email address>"


#

export PROJECT="${PROJECTSPACE}$/projects/<project directory containing your raw data>"
export DATABASEDIR="${PROJECTSPAC}$/databases"

# config and temp locations
export CONFIGDIR="${PROJECTSPACE}/nextflow/config"
export WORKDIR="/scratch-shared/${USER}/${PROJECT}"
export TMPDIR="/scratch-local/${USER}/${PROJECT}"

# nextflow specific settings
export NXF_APPTAINER_CACHEDIR="${PROJECTSPACE}/$nextflow/containers"
export NXF_SINGULARITY_CACHEDIR=${NXF_APPTAINER_CACHEDIR}}
export NXF_OPTS="-Xms4g -Xmx28g"
export NXF_CACHE_DIR=${WORKDIR}
export NXF_TEMP=${TMPDIR}
export NXF_WORK=${WORKDIR}

# create the directories
mkdir $NXF_APPTAINER_CACHEDIR
mkdir $NXF_TEMP
mkdir $NXF_WORK

# load the default module
module load 2024

# load the enviroment (optional, only if you need nf-core tools), search for the appropriate mamba module using 'module spider mamba'
module load Mamba/24.9.0-0
mamba activate ${PROJECTSPACE}/nextflow/env_nf

# run nf-core mag
# adjust where the metadata files are
# instead of the config files, specify
export DATE=`date +%Y%m%d`

nextflow run nf-core/mag \
   --input ${PROJECT}/metadata/metadata_test.csv \
   --outdir ${PROJECT}/run_${DATE} \
   --gtdb_db ${DATABASEDIR}/gtdbtk_r220_data.tar.gz \
   --email ${EMAIL} \
   --skip_spades \
   -profile snellius \
   -resume \
   -work-dir ${WORKDIR}
