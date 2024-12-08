# nf-core/configs: KAUST Configuration

manage the pipeline jobs via the nf-core/configs: KAUST Configuration

The purpose of this custom configurations is to streamline executing nf-core pipelines on the KAUST Ibex cluster.

## Getting help

We have a wiki page dedicated to the Bioinformatics team at KAUST to help users: [Bioinformatics Workflows](https://bclwiki.kaust.edu.sa/en/bix/analysis/public/bioinformatics-workflows).

## Using the KAUST config profile

The recommended way to activate `Nextflow`, that is needed to run the `nf-core` workflows on Ibex,
is to use the [module system](https://docs.hpc.kaust.edu.sa/soft_env/prog_env/modulesystem/basic_commands.html):

```bash
# Log in to the desired cluster
ssh <USER>@ilogin.ibex.kaust.edu.sa

# Activate the modules, you can also choose to use a specific version with e.g. `Nextflow/24.04.4`.
module load nextflow
```

Launch the pipeline with `-profile kaust` (one hyphen) to run the workflows using the KAUST profile.
This will download and launch the [`kaust.config`](../conf/kaust.config) which has been pre-configured with a setup suitable for the KAUST servers.
It will enable `Nextflow` to manage the pipeline jobs via the `Slurm` job scheduler and `Singularity` to run the tasks.
Using the KAUST profile, `Docker` image(s) containing required software(s) will be downloaded, and converted to `Singularity` image(s) if needed before execution of the pipeline. To avoid downloading same images by multiple users, we provide a singularity `libraryDir` that is configured to use images already downloaded in our central container library. Images missing from our library will be downloaded to the user's directory as defined by `cacheDir`.

### Accessing reference genomes on Ibex

We provide a collection of reference genomes, enabling users to run workflows seamlessly without needing to download the files. To enable access to this resource, simply add the `includeConfig` line in the script below to a `nextflow.config` file under the launch directory.

### Run workflows on Ibex

The KAUST profile makes running the nf-core workflows as simple as:

```bash

# Load Nextflow and Singularity modules
module purge
module load nextflow
module load singularity

# Utilize the existing genome resources
echo "includeConfig '/biocorelab/BIX/resources/configs/genomes.yaml'" >> nextflow.config

# Launch nf-core pipeline with the kaust profile, e.g. for analyzing human data:
$ nextflow run nf-core/<PIPELINE> -profile kaust -r <PIPELINE_VERSION> --genome GRCh38.p14 --samplesheet input.csv [...]
```

Where `input_csv` contains information about the samples and datafile paths.

Remember to use `-bg` to launch `Nextflow` in the background, so that the pipeline doesn't exit if you leave your terminal session.
Alternatively, you can also launch a `tmux` or a `screen` session to run the commands above. Another good way, is to run it as an independent sbatch job as [explained here](https://bclwiki.kaust.edu.sa/en/bix/analysis/public/bioinformatics-workflows#run-workflow-using-sbatch).

### Workflow specific profiles

In addition to this general config profile that should work for most pipelines, we also add pipeline-specific config files that will automatically be loaded specifying resources when running particular tasks, e.g. [MEGAHIT in metagenomics](conf/pipeline/mag/kaust.config). Please let us know if there are particular processes that continously fail so that we modify the defaults in the corresponding profile. 
