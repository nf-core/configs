# nf-core/configs: BIH HPC Configuration

This configuration enables the use of nf-core pipelines on the [BIH HPC cluster at the Berlin Institute of Health operated by CUBI]([https://www.hpc.bihealth.org/]).
To use, run a pipeline with `-profile bih`.
This will download and launch the [`bih.config`](../conf/bih.config) which has been pre-configured with a setup suitable for the BIH HPC cluster.
It will use slurm as a scheduler for the compute cluster, defines max resources, and specifies cache locations for apptainer.
Pipeline specific parameters still need to be configured manually.

### Install Nextflow and nf-core

The latest version of Nextflow is not installed by default on the BIH HPC cluster.
You can install it via conda following the [official documentation](https://nf-co.re/docs/usage/getting_started/installation#bioconda-installation):

```
# Install Bioconda according to the documentation, notably setting up channels and disabling auto-activation of the base environment.
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
conda config --set auto_activate_base false

# Create the environment env_nf, and install the tool nextflow as well as nf-core.
conda create --name env_nf nextflow nf-core
```

### Run Nextflow

Here is an example of an sbatch script with the nf-core pipeline rnaseq ([read documentation here](https://nf-co.re/rnaseq/3.14.0)).
The user has to include a scratch path and the parameters of the pipeline.

```
# Initiating SLURM options
#!/bin/bash
#SBATCH --job-name=rnaseq_nf
#SBATCH --mem-per-cpu=10G
#SBATCH --ntasks=1
#SBATCH -n 1
#SBATCH --output=%x_%A_%a.log

# Launch conda and nextflow/nf-core
source <path to your conda installation>/etc/profile.d/conda.sh
conda activate env_nf

# Nextflow run
nextflow run nf-core/rnaseq -r 3.14.0 -profile bih,test,apptainer \
--scratch "<path to your scratch folder>" \
--outdir "test_run_rnaseq"
```

All of the intermediate files required to run the pipeline will be stored in the `<path to your scratch folder>/work_$USER/` directory and the docker/apptainer images in the `<path to your scratch folder>/apptainer_imgs_$USER/`.
Therefore, we recommend the `--scratch` option to point to a user/group/project's scratch directory.
If the pipeline runs successfully, files in the work directory are deleted automatically.
If the pipeline exits with an error, the work directory is not deleted and pipeline execution can be continued with the `-resume` option.
Main output files created by the pipeline will be saved in the `--outdir` directory.

