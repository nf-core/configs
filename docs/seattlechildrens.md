# nf-core/configs: Seattle Children's Research Institute Configuration

All nf-core pipelines have been successfully configured for use on the the Sasquatch HPC at Seattle Children Research Institude (SCRI), Seattle, WA.

To use, run the pipeline with `-profile seattlechildrens`. This will download and launch the pipeline using [`seattlechildrens.config`](../conf/seattlechildrens.config) which has been pre-configured with a setup suitable for the Sasquatch cluster at SCRI.

This profile assumes that you will use the `cpu-core-sponsored` partition.  If you need to use `gpu-core-sponsored` for some steps, you can get in touch with Research Scientific Computing on Teams or email about how to modify the pipeline.

We also maintain a [webpage about Nextflow](http://gonzo/hpcGuide/Nextflow.html) within the Seattle Children's intranet.

# Project info

This config file is created for the use on the Sasquatch HPC at Seattle Children Research Institude (SCRI), Seattle, WA. Using this config will pre-configure a set up suitable for the Sasquatch HPC. The Singularity images will be downloaded to run on the cluster. The nextflow pipeline should be executed inside of the Sasquatch system.

# Below are mandatory information SCRI

Before running the pipeline you will need to create a Nextflow environment on `mamba`. _Singularity_ is on the path by default and does not need to be loaded.

## Create a Nextflow `mamba` environment

1. Create _nextflow.yml_ file containing the following content. This YAML file can be utilized to set up a mamba environment, specifying both the version of Nextflow and the environment name.

```yaml
name: nextflow
channels:
  - bioconda
  - conda-forge
dependencies:
  - python>=3.9
  - nextflow==24.10.4
  - nf-core==3.2.0
  - graphviz
```

2. Setting channel priority

Make sure that channel priority is set to flexible using the following comments:

```bash
# print your current conda settings
mamba config --describe channel_priority
# set to flexible if not already done
mamba config --set channel_priority flexible
```

3. Create the _Nextflow_ `mamba` environment

```bash
mamba env create -f nextflow.yaml
```

4. Running in HPC (Sasquatch)

Please look into [RSC-RP/nextflow_scri_config](https://github.com/RSC-RP/nextflow_scri_config) for details.

```bash
# activate enviornment
mamba activate nextflow

# To list all the accounts you are authorized on HPC. For example if you have an account cpu-mylab-sponsored, your association is "mylab".
sshare -o "Account,Partition%20"

# example to run nextflow pipeline (please replace with your own association, module, and temp directory)
nextflow run \
    [nf-core/module_name] \
    -profile seattlechildrens \
    --assoc ["your_association_name"] \
    -workDir /data/hps/assoc/private/mylab/user/mmouse/temp_rnaseq \
```

You can find more information about computational resources [here](https:#child.seattlechildrens.org/research/center_support_services/research_informatics/research_scientific_computing/high_performance_computing_core/). You have to be an employee of SCRI to access the link.
