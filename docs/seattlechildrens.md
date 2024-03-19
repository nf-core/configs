# nf-core/configs: PROFILE Configuration

All nf-core pipelines have been successfully configured for use on the the Cybertron HPC at Seattle Children Research Institude (SCRI), Seattle, WA.

To use, run the pipeline with `-profile PROFILENAME`. This will download and launch the pipeline using [`seattlechildrens.config`](../conf/seattlechildrens.config) which has been pre-configured with a setup suitable for the Cybertron cluster at SCRI. Using this profile, a container with all of the required software will be downloaded.

# Project info
This config file is created for the use on the Cybertron HPC at Seattle Children Research Institude (SCRI), Seattle, WA. Using this config will pre-configure a set up suitable for the Cybertron HPC. The Singularity images will be downloaded to run on the cluster. The nextflow pipeline should be executed inside of the Cybertron system.

# Below are mandatory information SCRI
Before running the pipeline you will need to create a Nextflow environment on `mamba`. You can load _Singularity_ using the environment module system on **Cybertron**. 

## Create a Nextflow `mamba` environment 

1. Create _nextflow.yml_ file containing the following content. This YAML file can be utilized to set up a mamba environment, specifying both the version of Nextflow and the environment name.

```yaml
name: nextflow
channels:
  - bioconda
  - conda-forge
dependencies:
  - python>=3.9
  - nextflow==23.10.0
  - nf-core==2.10
  - graphviz
```

2. Setting channel priority
Make sure that channel priority is set to flexible using the following comments:

```bash
> mamba config --describe channel_priority # print your current conda settings
> mamba config --set channel_priority flexible # set to flexible if not already done
```


3. Create the _Nextflow_ `mamba` environment

```bash
> mamba env create -f nextflow.yaml
```




You can find more information about computational resources [here](https:#child.seattlechildrens.org/research/center_support_services/research_informatics/research_scientific_computing/high_performance_computing_core/). You have to be an employee of SCRI to access the link. 

