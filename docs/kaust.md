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
ssh <USER>@ilogin.kaust.edu.sa

# Activate the modules, you can also choose to use a specific version with e.g. `Nextflow/24.04.4`.
module load nextflow
```

Launch the pipeline with `-profile kaust` (one hyphen) to run the workflows using the KAUST profile.
This will download and launch the [`kaust.config`](../conf/kaust.config) which has been pre-configured with a setup suitable for the KAUST servers.
It will enable `Nextflow` to manage the pipeline jobs via the `Slurm` job scheduler and `Singularity` to run the tasks.
Using the KAUST profile, `Docker` image(s) containing required software(s) will be downloaded, and converted to `Singularity` image(s) if needed before execution of the pipeline. To avoid downloading same images by multiple users, we provide a singularity `libraryDir` that is configured to use images already downloaded in our central container library. Images missing from our library will be downloaded to your home directory path as defined by `cacheDir`.

The KAUST profile makes running the nf-core workflows as simple as:

```bash
module load nextflow
# Launch nf-core pipeline with the kaust profile, e.g. for analyzing human data:
$ nextflow run nf-core/<PIPELINE> -profile kaust -r <PIPELINE_VERSION> --genome GRCh38.p14 --samplesheet input.csv [...]
```

Where `input_csv` contains information about the samples and datafile paths.

Remember to use `-bg` to launch `Nextflow` in the background, so that the pipeline doesn't exit if you leave your terminal session.
Alternatively, you can also launch `Nextflow` in a `tmux` or a `screen` session.
