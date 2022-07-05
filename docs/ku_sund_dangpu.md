# nf-core/configs: PROFILE Configuration

All nf-core pipelines have been successfully configured for use on the dangpu PROFILE CLUSTER at the 
Novo Nordisk Foundation Center for Stem Cell Medicine (reNEW) and the Novo Nordisk Foundation Center for Protein Research (CPR) at the University of Copenhagen.

To use, run the pipeline with `-profile ku_sund_dangpu`. This will download and launch the [`ku_sund_dangpu.config`](../conf/ku_sund_dangpu.config) which has been pre-configured with a setup suitable for the PROFILE CLUSTER.

## Modules

Before running the pipeline you will need to load Nextflow and Singularity using the environment module system on PROFILE CLUSTER. You can do this by issuing the commands below:

```bash
## Load Nextflow and Singularity environment modules
module purge
module load openjdk/11.0.0 nextflow/22.04.3 singularity/3.8.0 
```

## How to use the nf-core pipelines on PROFILE CLUSTER

###1. set up .bash_profile
Add memory restrictions to `.bash_profile`. Use `vim` text editor to edit `.bash_profile` file (or create one if it does not exist in your home directory:

```
vi ~/.bash_profile
```

paste the following text within the file:
```
# personalising the profile: change the value of the variable $abc123 to your own user id
abc123=def456 

# In some cases, the Nextflow Java virtual machines can start to request a large amount of memory. We recommend adding the following line to your environment to limit this
export NXF_OPTS='-Xms1g -Xmx4g'

# Don't fill up your home directory with cache files
export NXF_HOME=/projects/dan1/people/${abc123}/cache/nxf-home 
export NXF_TEMP=${SNIC_TMP:-$HOME/glob/nxftmp}

# Nextflow singularity image cachedir export 
NXF_SINGULARITY_CACHEDIR=/projects/dan1/people/${abc123}/cache/singularity-images  
```

then save the changes and exit the editor. Now you need to activate the `.bash_profile` by logging out and in again to PROFILE CLUSTER or by typing:
```
source .bash_profile
```

The `$HOME` directory at dangpu has restricted space and should not be used to store cache files. Create those designated cache spaces for nextflow and singularity outside your `$HOME`:
```
mkdir $NXF_SINGULARITY_CACHEDIR
mkdir $NXF_HOME
```

### 3. choose a nf-core pipeline and test it with your preferred settings
```
nextflow run nf-core/rnaseq -profile test,ku_sund_dangpu
```

