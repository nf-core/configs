# nf-core/configs: University of Ghent High Performance Computing Infrastructure (VSC)

> **NB:** You will need an [account](https://www.ugent.be/hpc/en/access/faq/access) to use the HPC cluster to run the pipeline.

Regarding environment variables in `~/.bashrc`, make sure you have a setup similar to the one below. If you're already part of a VO, ask for one or use `VSC_DATA_USER` instead of `VSC_DATA_VO_USER`.

```bash
# Needed for Tier1 accounts, not for Tier2
export SLURM_ACCOUNT={FILL_IN_NAME_OF_YOUR_ACCOUNT}
export SALLOC_ACCOUNT=$SLURM_ACCOUNT
export SBATCH_ACCOUNT=$SLURM_ACCOUNT
# Needed for running Nextflow jobs
export NXF_HOME=$VSC_DATA_VO_USER/.nextflow
# Needed for running Apptainer containers
export APPTAINER_CACHEDIR=$VSC_DATA_VO_USER/.apptainer/cache
export APPTAINER_TMPDIR=$VSC_DATA_VO_USER/.apptainer/tmp
```

First you should go to the cluster you want to run the pipeline on. You can check what clusters have the most free space on this [link](https://shieldon.ugent.be:8083/pbsmon-web-users/). Use the following commands to easily switch between clusters:

```shell
module purge
module swap cluster/<CLUSTER>
```

Before running the pipeline you will need to create a PBS script to submit as a job.

```bash
#!/bin/bash

module load Nextflow

nextflow run <pipeline> -profile vsc_ugent,<CLUSTER> <Add your other parameters>
```

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.
The config contains a `cleanup` command that removes the `work/` directory automatically once the pipeline has completed successfully. If the run does not complete successfully then the `work/` dir should be removed manually to save storage space. The default work directory is set to `$VSC_SCRATCH_VO_USER/work` per this configuration

You can also add several TORQUE options to the PBS script. More about this on this [link](http://hpcugent.github.io/vsc_user_docs/pdf/intro-HPC-linux-gent.pdf#appendix.B).

To submit your job to the cluster by using the following command:

```shell
qsub <script name>.pbs
```

The VSC does [not support](https://docs.hpc.ugent.be/Linux/apptainer/) Apptainer containers provided via a URL (e.g., shub://... or docker://...).
One solution is to download all the containers beforehand, like in [this pipeline](https://github.com/saeyslab/spotless-benchmark).

First get the containers.json file from the pipeline you want to run:

```bash
nextflow inspect main.nf -profile vsc_ugent,<CLUSTER> > containers.json
```

Then run a build script (script appended below) to build all the containers. This can take a long time and a lot of space, but it is a one-time cost. For many large images, consider running this as a job.

```bash
bash build_all_containers.sh containers.json
```

Overwrite the container in your `nextflow.config`. If you need GPU support, also apply the label 'use_gpu':

```nextflow
process {
    withName: DEEPCELL_MESMER {
        label = 'use_gpu'
        // container "docker.io/vanvalenlab/deepcell-applications:0.4.1"
        container = "./DEEPCELL_MESMER_GPU.sif"
    }
}
```

> **NB:** The profile only works for the clusters `skitty`, `swalot`, `victini`, `kirlia` and `doduo`.

> **NB:** The default directory where the `work/` and `singularity/` (cache directory for images) is located in `$VSC_SCRATCH_VO_USER`.

`build_all_containers.sh`:

```bash
#!/bin/env bash

# avoid that Apptainer uses $HOME/.cache
export APPTAINER_CACHEDIR=/tmp/$USER/apptainer/cache
# instruct Apptainer to use temp dir on local filessytem
export APPTAINER_TMPDIR=/tmp/$USER/apptainer/tmpdir
# specified temp dir must exist, so create it
mkdir -p $APPTAINER_TMPDIR

# pull all containers from the given JSON file
# usage: build_all_containers.sh containers.json [FORCE]
JSON=$1
FORCE=${2:-false}

echo "Building containers from $JSON"
NAMES=$(sed -nE 's/.*"name": "([^"]*)".*/\1/p' $JSON)
CONTAINERS=$(sed -nE 's/.*"container": "([^"]*)".*/\1/p' $JSON)
# default FORCE to false
# paste name and containers together
paste <(echo "$NAMES") <(echo "$CONTAINERS") | while IFS=$'\t' read -r name container; do
    # is sif already present, continue unless FORCE is true
    if [ -f "$name.sif" ] && [ "$FORCE" != "true" ]; then
        continue
    fi

    # if container is null, skip
    if [ -z "$container" ]; then
        continue
    fi

    # if not docker://, add docker://
    if [[ $container != docker://* ]]; then
        container="docker://$container"
    fi
    echo "Building $container"
    # overwrite the existing container
    apptainer build --fakeroot /tmp/$USER/$name.sif $container
    mv /tmp/$USER/$name.sif $name.sif
done
```
