# nf-core/configs: hki_genie Configuration

All nf-core pipelines have been successfully configured for use on the 'genie' cluster at the [Leibniz Institute for Natural Product Research and Infection Biology](http://eva.mpg.de).

To use, run the pipeline with `-profile hki_genie`. You can further with optimise submissions by specifying which cluster queue you are using e,g, `-profile hki_genie`. This will download and launch the [`hki_genie.config`](../conf/hki_genie.config) which has been pre-configured with a setup suitable.

> ![NOTE]
> This is an unofficial profile written and curated by the community, and the HKI IT team cannot provide support for it!

The configuration file is set to remove intermediate files on successful completion of the pipeline, to save space on the cluster.
To retain these files, you can use the `debug` profile, e.g. `-profile hki_genie,debug`.
If you have a failed run, make sure to clean up the `work/` directory once you have finally fixed the issue with `nextflow clean`.

In cases of a failed job (e.g. due to memory limits), Nextflow will automatically retry the job with increased resources to a maximum of two times.

Note that this profile does not automatically optimise resource requests for each process in the pipeline!
For this please speak to the contact to make a pipeline specific configuration file!

## Instructions

### Set up

Before running `nextflow run...` you must make sure you have Nextflow installed, e.g. via conda.

You should also specify a cache directory for singularity images, so each pipeline run does not need to re-download the images.
Ideally this should be to a location shared amongst everyone in your group and department.

You can do this by exporting the `NXF_SINGULARITY_CACHEDIR` environment variable, in your `~/.bashrc e.g.:

```bash
export NXF_SINGULARITY_CACHEDIR=/path/to/shared/cache
```

Department-specific shared locations:

- PBT: `/Net/Groups/cc/apps/singularity`

## Running a pipeline

You must submit the head job to the cluster as singularity/apptainer is not available on head nodes, for example in a file called `run.batch`

```bash
#!/bin/bash
#SBATCH --job-name=nf-core
#SBATCH -o slurm.%j.out        # STDOUT (the standard output stream)
#SBATCH -e slurm.%j.err        # STDERR (the output stream for errors)
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH -c 2
#SBATCH --mem=4GB
#SBATCH --export=ALL
#SBATCH --partition cpu

## Activate your Nextflow installation, here I installed it via my own conda environment
source ~/.bashrc
conda activate nf-core

## Specify a cache directory for singularity images to prevent redundant downloads!
export NXF_SINGULARITY_CACHEDIR=/Net/Groups/<path>/<to>/<shared>/<cache>/

## Execute your favourite pipeline here
nextflow run nf-core/<pipeline> \
-profile hki_genie,test \
-ansi-log false \
--outdir /Net/Groups/<path>/<to>/<your>/results/ \
-w /Net/Groups/<path>/<to>/<shared>/work/ \
<...>
```

And submit the head job the cluster with

```bash
sbatch run.bash
```

Some notes on the above:

1. `#SBATCH --time` should be set appropriately for the _entire_ pipeline to complete (this can be days!)
2. `-c` and `--mem` reflects ONLY the head job - do not increase to match the requirements of the worker jobs (this must be done via [an additional Nextflow](https://nf-co.re/docs/usage/getting_started/configuration#tuning-workflow-resources) configuration file)
3. `--partition cpu` must be used and NOT sent to the GPU queue, as the head job does not need the (GPU steps of the pipeline should automatically be sent to the GPU queue)
4. `source` you must tell SLURM to find your Nextflow installation depending on how you installed it
5. `export` you should specify a cache directory for singularity images to prevent re-downloading on EVERY run
6. `--ansi-log` is used to have human readable log files in `-o` (`true` will try to record 'real time' updates that are hard to read)
7. `--outdir` and `-w` it is best to specify full paths
