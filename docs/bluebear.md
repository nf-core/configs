# nf-core/configs: BlueBEAR HPC Configuration

Configuration for the BlueBEAR high performance computing (HPC) cluster at the University of Birmingham.

## Setup

To run a Nextflow pipeline, load the following modules,

```bash
module load bear-apps/2022b
module load Nextflow/24.04.2
```

## Apptainer/Singularity

BlueBEAR comes with Apptainer installed for running processes inside containers. Our configuration makes use of this
when executing processes.

We advise you create a directory in which to cache images using the following environment variable. For example,

```bash
export NXF_SINGULARITY_CACHEDIR="/rds/projects/_initial_/_project_/.apptainer"
```

where `_project_` is your project code and `_initial_` is its initial letter.

You may notice that our nf-core configuration file enables Singularity, not Apptainer, for use with Nextflow. Due to
their similarities (see [this announcement](https://apptainer.org/news/community-announcement-20211130/)), Apptainer
creates the alias `singularity` for `apptainer` allowing both commands to be used. Nextflow's Singularity engine makes
use of pre-built Singularity images, whereas its Apptainer engine does not.

## Run

**Do not** run Nextflow pipelines on a login node. Instead, create a submission script or start an interactive job.

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

Nextflow creates a working directory to store files while the pipeline is running. We have configured Nextflow to clean
the contents of this directory after a successful run. The `-resume` option will only work after an unsuccessful run.
If you want to keep the working directory contents, add the `debug` profile to your run command (e.g.
`-profile bluebear,debug`).

## Example

Here is an example job submission script. This job runs the `nf-core/rnaseq` pipeline tests with the BlueBEAR config
file. We request 1 hour to run the pipeline on 1 node with 2 tasks.

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

# Directory in which to cache apptainer/singularity images
export NXF_SINGULARITY_CACHEDIR="/rds/projects/_initial_/_project_/.apptainer"

nextflow run nf-core/rnaseq -profile bluebear,test --outdir test_results
```

## Troubleshooting

### Failed while making image from oci registry

You may get an error which looks like the following,

```text
FATAL: While making image from oci registry: error fetching image to cache: while building SIF from
layers: conveyor failed to get: while getting config: no descriptor found for reference
"139610e0c1955f333b61f10e6681e6c70c94357105e2ec6f486659dc61152a21"
```

This may be caused by an issue with parallel image downloads (see e.g.
[this issue](https://github.com/apptainer/singularity/issues/5020)). You can fix this by downloading all images required
by the pipeline using `nf-core` tools to
[download the pipeline](https://nf-co.re/docs/nf-core-tools/pipelines/download) either interactively with

```bash
nf-core download _pipeline_ -o /path/to/outdir --container-system singularity --container-cache-utilisation amend
```

or in a Slurm job.

**Note:** `nf-core` tools is a Python package which needs to be installed first.

Here is an example Slurm job script which downloads version 3.14.0 of the `nf-core/rnaseq` pipeline.

```bash
#!/bin/bash
#SBATCH --account _project_
#SBATCH --qos bbdefault
#SBATCH --time 30
#SBATCH --nodes 1
#SBATCH --ntasks 2

set -e  # exit on first error

module purge; module load bluebear
module load bear-apps/2022b
module load Nextflow/24.04.2
module load Python/3.10.8-GCCcore-12.2.0

# Directory in which to cache apptainer images
export NXF_SINGULARITY_CACHEDIR="/rds/projects/_initial_/_project_/.apptainer"

# Path to Python virtual environment with nf-core tools
VENV_DIR="/path/to/virtual/environments"
VENV_PATH="${VENV_DIR}/nf-core-${BB_CPU}"

# Check if base virtual environment directory exists and create it if not
if [[ ! -d ${VENV_DIR} ]]; then
    mkdir -p ${VENV_DIR}
fi

# Check if virtual environment exists and create it if not
if [[ ! -d ${VENV_PATH} ]]; then
    python3 -m venv ${VENV_PATH}
    ${VENV_PATH}/bin/python3 -m pip install --upgrade pip
    ${VENV_PATH}/bin/python3 -m pip install nf-core
fi

# Activate virtual environment
source ${VENV_PATH}/bin/activate

# Run nf-core download tool to fetch pipeline and pull apptainer/singularity images
# You must specify the pipeline revision/branch
nf-core download rnaseq -r 3.14.0 -o /path/to/outdir -d -x none \
--container-system singularity --container-cache-utilisation amend
```

Then, you can update the final line in the [example script](#example) with the path to the locally
downloaded pipeline.

```bash
nextflow run /path/to/outdir/3_14_0 -profile bluebear,test --outdir test_results
```

**Note:** Make sure that the `NXF_SINGULARITY_CACHEDIR` environment variable is the same in both scripts for Nextflow
to see the pre-downloaded images.
