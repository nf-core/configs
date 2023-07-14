# nf-core/configs: EBI Codon Cluster Configuration

All nf-core pipelines have been successfully configured for use on the codon cluster at the European Bioinformatics Institute.

To use, run the pipeline with `-profile ebi_codon`. This will download and launch the [`ebi_codon.config`](../conf/ebi_codon.config) which has been pre-configured with a setup suitable for the codon cluster.

You should not run Nextflow on the login nodes. You should submit a batch job that executes Nextflow.

## Loading the required modules

Before running the pipeline you will need to load Nextflow and Singularity using the environment module system on the codon cluster. You can do this by issuing the commands below:

```bash
## Load Nextflow and Singularity environment modules
module purge
module load nextflow/22.10.1
module load singularityce/3.10.3
```

You may want to add those module load commands to your shell configuration file if you use them often.

## Installing mamba

Run the following:

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
bash Mambaforge-$(uname)-$(uname -m).sh
```

Follow the instructions [here](https://github.com/conda-forge/miniforge#mambaforge) for more details.

## Setting up a suitable path for the Nextflow software cache

It is recommended to install conda environments and singularity containers in your `/hps/software` directory. To achieve this, add to your `~/.nextflow/config` file the following lines:

```nextflow
singularity.cacheDir = "/hps/software/users/<group>/<user_id>/nextflow_software_cache/singularity"
conda.cacheDir = "/hps/software/users/<group>/<user_id>/nextflow_software_cache/conda"
```
