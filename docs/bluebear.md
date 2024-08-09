# nf-core/configs: BlueBEAR HPC Configuration

Configuration for the BlueBEAR high performance computing (HPC) cluster at the University of Birmingham.

## Setup

To run a Nextflow pipeline, load the following modules,

```bash
module load bear-apps/2022b
module load Nextflow/24.04.2
```

## Apptainer

The BlueBEAR config uses Apptainer to run pipeline processes in containers. We advise you create a directory
in which to cache Apptainer images using the following environment variable. For example,

```bash
export APPTAINER_CACHEDIR="/rds/projects/_initial_/_project_/.apptainer"
export NXF_APPTAINER_CACHEDIR="${APPTAINER_CACHEDIR}"
```

where `_project_` is your project code and `_initial_` is its initial letter.

## Run

Do not run Nextflow pipelines on a login node. Instead, create a submission script or start an interactive job.

To run a Nextflow pipeline, specify the BlueBEAR profile option. For example,

```bash
nextflow run nf-core/_pipeline_ -profile bluebear --outdir results
```

where `_pipeline_` is the name of the pipeline.

Make sure the job time requested is sufficient for running the full pipeline. If the job ends before the pipeline is
complete, rerun it from a checkpoint using the `-resume` option. For example, run

```bash
nextflow run nf-core/_pipeline_ -profile bluebear --outdir results -resume
```

in a new job with more time requested.

## Example

Here is an example job submission script. This job runs the `nf-core/mag` Nextflow pipeline tests with the BlueBEAR
config file. We request 1 hour to run the pipeline on 1 node with 2 tasks.

```bash
#!/bin/bash
#SBATCH --account _project_
#SBATCH --qos bbdefault
#SBATCH --time 1:0:0
#SBATCH --nodes 1
#SBATCH --ntasks 2

set -e

module purge; module load bluebear
module load bear-apps/2022b
module load Nextflow/24.04.2

# Directory in which to cache apptainer images

export APPTAINER_CACHEDIR="/rds/projects/_initial_/_project_/.apptainer"
export NXF_APPTAINER_CACHEDIR="${APPTAINER_CACHEDIR}"

nextflow run nf-core/mag -profile bluebear,test --outdir test_results
```

## Clean Work Directory

Nextflow caches pipeline files in a work directory (default is `work`). This is useful if you need to resume a job
after a failure (using the `-resume` option). However, the `work` directory can fill up quickly. Regularly cleaning the
work directory avoids filling up your project quota. For example, the following command will show cached files for all
runs before the last run,

```bash
nextflow clean -n -before last
```

Then, to forcibly remove these files, execute the following command,

```bash
nextflow clean -f -before last
```

If you also want to remove cached files for the last run, execute,

```bash
nextflow clean -f last
```
