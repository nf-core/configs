# [![nf-core/configs](docs/images/nfcore-configs_logo.png "nf-core/configs")](https://github.com/nf-core/configs) <!-- omit in toc -->

[![Lint Status](https://github.com/nf-core/configs/workflows/Configs%20tests/badge.svg)](https://github.com/nf-core/configs/workflows/Configs%20tests/badge.svg)

A repository for hosting Nextflow configuration files containing custom parameters required to run nf-core pipelines at different Institutions.

## Table of contents <!-- omit in toc -->

* [Using an existing config](#using-an-existing-config)
  * [Configuration and parameters](#configuration-and-parameters)
  * [Offline usage](#offline-usage)
* [Adding a new config](#adding-a-new-config)
  * [Checking user hostnames](#checking-user-hostnames)
  * [Testing](#testing)
  * [Documentation](#documentation)
  * [Uploading to `nf-core/configs`](#uploading-to-nf-coreconfigs)
* [Adding a new pipeline-specific config](#adding-a-new-pipeline-specific-config)
  * [Pipeline-specific institutional documentation](#pipeline-specific-institutional-documentation)
  * [Pipeline-specific documentation](#pipeline-specific-documentation)
  * [Enabling pipeline-specific configs within a pipeline](#enabling-pipeline-specific-configs-within-a-pipeline)
  * [Create the pipeline-specific `nf-core/configs` files](#create-the-pipeline-specific-nf-coreconfigs-files)
* [Help](#help)

## Using an existing config

The Nextflow [`-c`](https://www.nextflow.io/docs/latest/config.html) parameter can be used with nf-core pipelines in order to load custom config files that you have available locally.
However, if you or other people within your organisation are likely to be running nf-core pipelines regularly it may be a good idea to use/create a custom config file that defines some generic settings unique to the computing environment within your organisation.

### Configuration and parameters

The config files hosted in this repository define a set of parameters which are specific to compute environments at different Institutions but generic enough to be used with all nf-core pipelines.

All nf-core pipelines inherit the functionality provided by Nextflow, and as such custom config files can contain parameters/definitions that are available to both.
For example, if you have the ability to use [Singularity](https://sylabs.io/singularity/) on your HPC you can add and customize the Nextflow [`singularity`](https://www.nextflow.io/docs/latest/config.html#scope-singularity) scope in your config file.
Similarly, you can define a Nextflow [`executor`](https://www.nextflow.io/docs/latest/executor.html) depending on the job submission process available on your cluster.
In contrast, the `params` section in your custom config file will typically define parameters that are specific to nf-core pipelines.

You should be able to get a good idea as to how other people are customising the execution of their nf-core pipelines by looking at some of the config files in [`nf-core/configs`](https://github.com/nf-core/configs/tree/master/conf).

### Offline usage

If you want to use an existing config available in `nf-core/configs`, and you're running on a system that has no internet connection, you'll need to download the config file and place it in a location that is visible to the file system on which you are running the pipeline.
Then run the pipeline with `--custom_config_base` or `params.custom_config_base` set to the location of the directory containing the repository files:

```bash
## Download and unzip the config files
cd /path/to/my/configs
wget https://github.com/nf-core/configs/archive/master.zip
unzip master.zip

## Run the pipeline
cd /path/to/my/data
nextflow run /path/to/pipeline/ --custom_config_base /path/to/my/configs/configs-master/
```

Alternatively, instead of using the configuration profiles from this repository, you can run your pipeline directly calling the single institutional config file that you need with the `-c` parameter.

```bash
nextflow run /path/to/pipeline/ -c /path/to/my/configs/configs-master/conf/my_config.config
```

> Note that the nf-core/tools helper package has a `download` command to download all required pipeline files + singularity containers + institutional configs in one go for you, to make this process easier.

## Adding a new config

If you decide to upload your custom config file to `nf-core/configs` then this will ensure that your custom config file will be automatically downloaded, and available at run-time to all nf-core pipelines, and to everyone within your organisation.
You will simply have to specify `-profile <config_name>` in the command used to run the pipeline.
See [`nf-core/configs`](https://github.com/nf-core/configs/tree/master/conf) for examples.

Please also make sure to add an extra `params` section with `params.config_profile_description`, `params.config_profile_contact` and `params.config_profile_url` set to reasonable values.
Users will get information on who wrote the configuration profile then when executing a nf-core pipeline and can report back if there are things missing for example.

### Checking user hostnames

If your cluster has a set of consistent hostnames, nf-core pipelines can check that users are using your profile.
Add one or more hostname substrings to `params.hostnames` under a key that matches the profile name.
If the user's hostname contains this string at the start of a run or when a run fails and their profile does not contain the profile name, a warning message will be printed.

### Testing

If you want to add a new custom config file to `nf-core/configs` please test that your pipeline of choice runs as expected by using the [`-c`](https://www.nextflow.io/docs/latest/config.html) parameter.

```bash
## Example command for nf-core/rnaseq
nextflow run nf-core/rnaseq --reads '*_R{1,2}.fastq.gz' --genome GRCh37 -c '/path/to/custom.config'
```

### Documentation

You will have to create a [Markdown document](https://www.markdownguide.org/getting-started/) outlining the details required to use the custom config file within your organisation.
You might orientate yourself using the [Template](docs/template.md) that we provide and filling out the information for your cluster there.

See [`nf-core/configs/docs`](https://github.com/nf-core/configs/tree/master/docs) for examples.

Currently documentation is available for the following systems:

* [ABIMS](docs/abims.md)
* [AWSBATCH](docs/awsbatch.md)
* [BIGPURPLE](docs/bigpurple.md)
* [BI](docs/bi.md)
* [BINAC](docs/binac.md)
* [BIOHPC_GEN](docs/biohpc_gen.md)
* [CAMBRIDGE](docs/cambridge.md)
* [CBE](docs/cbe.md)
* [CCGA_DX](docs/ccga_dx.md)
* [CCGA_MED](docs/ccga_med.md)
* [CFC](docs/cfc.md)
* [CRICK](docs/crick.md)
* [CZBIOHUB_AWS](docs/czbiohub.md)
* [DENBI_QBIC](docs/denbi_qbic.md)
* [EBC](docs/ebc.md)
* [EVA](docs/eva.md)
* [GENOTOUL](docs/genotoul.md)
* [GENOUEST](docs/genouest.md)
* [GIS](docs/gis.md)
* [GOOGLE](docs/google.md)
* [HEBBE](docs/hebbe.md)
* [ICR_DAVROS](docs/icr_davros.md)
* [JAX](docs/jax.md)
* [KRAKEN](docs/kraken.md)
* [MPCDF](docs/mpcdf.md)
* [MUNIN](docs/munin.md)
* [OIST](docs/oist.md)
* [PASTEUR](docs/pasteur.md)
* [PHOENIX](docs/phoenix.md)
* [PRINCE](docs/prince.md)
* [SANGER](docs/sanger.md)
* [SEG_GLOBE](docs/seg_globe.md)
* [SHH](docs/shh.md)
* [UCT_HPC](docs/uct_hpc.md)
* [UPPMAX](docs/uppmax.md)
* [UTD_GANYMEDE](docs/utd_ganymede.md)
* [UTD_SYSBIO](docs/utd_sysbio.md)
* [UZH](docs/uzh.md)

### Uploading to `nf-core/configs`

[Fork](https://help.github.com/articles/fork-a-repo/) the [`nf-core/configs`](https://github.com/nf-core/configs/) repository to your own GitHub account.
Within the local clone of your fork add the custom config file to the [`conf/`](https://github.com/nf-core/configs/tree/master/conf) directory, and the documentation file to the [`docs/`](https://github.com/nf-core/configs/tree/master/docs) directory.
You will also need to edit and add your custom profile to the [`nfcore_custom.config`](https://github.com/nf-core/configs/blob/master/nfcore_custom.config) file in the top-level directory of the clone.
You will also need to edit and add your custom profile to the [`README.md`](https://github.com/nf-core/configs/blob/master/README.md) file in the top-level directory of the clone.

In order to ensure that the config file is tested automatically with GitHub Actions please add your profile name to the `profile:` scope in [`.github/workflows/main.yml`](.github/workflows/main.yml). If you forget to do this the tests will fail with the error:

```bash
Run python ${GITHUB_WORKSPACE}/bin/cchecker.py ${GITHUB_WORKSPACE}/nfcore_custom.config ${GITHUB_WORKSPACE}/.github/workflows/main.yml
Tests don't seem to test these profiles properly. Please check whether you added the profile to the Github Actions testing YAML.
set(['<profile_name>'])
##[error]Process completed with exit code 1.
```

Commit and push these changes to your local clone on GitHub, and then [create a pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) on the `nf-core/configs` GitHub repo with the appropriate information.

We will be notified automatically when you have created your pull request, and providing that everything adheres to nf-core guidelines we will endeavour to approve your pull request as soon as possible.

## Adding a new pipeline-specific config

Sometimes it may be desirable to have configuration options for an institute that are specific to a single nf-core pipeline.
Such options should not be added to the main institutional config, as this will be applied to all pipelines.
Instead, we can create a pipeline-specific institutional config file.

:warning: Remember to replace the `<PIPELINE>` and `<PROFILE>` placeholders with the pipeline name and profile name in the following examples

Institutional configs work because the pipeline `nextflow.config` file loads the [`nf-core/configs/nfcore_custom.config` config file](https://github.com/nf-core/configs/blob/master/nfcore_custom.config), which in turn loads the institutional configuration file based on the profile `<PROFILE>` supplied on the command line.

To add in pipeline-specific institutional configs, we add a second `includeConfig` call in the pipeline `nextflow.config` file, which loads the `pipeline/<PIPELINE>.config` file from the [`nf-core/configs`](https://github.com/nf-core/configs) repo.
This file has `<PIPELINE>` specific institution configuration again with different profiles `<PROFILE>`.

The pipeline `nextflow.config` file should first load the generic institutional configuration file and then the pipeline-specific institutional configuration file.
Each configuration file will add new params and overwrite the params already existing.

Note that pipeline-specific configs are not required and should only be added if needed.

### Pipeline-specific institutional documentation

Currently documentation is available for the following pipelines within specific profiles:

* ampliseq
  * [BINAC](docs/pipeline/ampliseq/binac.md)
  * [UPPMAX](docs/pipeline/ampliseq/uppmax.md)
* eager
  * [SHH](docs/pipeline/eager/shh.md)
  * [EVA](docs/pipeline/eager/eva.md)
* rnafusion
  * [MUNIN](docs/pipeline/rnafusion/munin.md)
* sarek
  * [MUNIN](docs/pipeline/sarek/munin.md)
  * [UPPMAX](docs/pipeline/sarek/uppmax.md)

### Pipeline-specific documentation

Currently documentation is available for the following pipeline:

* viralrecon
  * [genomes](docs/pipeline/viralrecon/genomes.md)

### Enabling pipeline-specific configs within a pipeline

:warning: **This has to be done on a fork of the `nf-core/<PIPELINE>` repository.**

[Fork](https://help.github.com/articles/fork-a-repo/) the `nf-core/<PIPELINE>` repository to your own GitHub account.
Within the local clone of your fork, if not already present, add the following to `nextflow.config` **after** the code that loads the generic nf-core/configs config file:

```nextflow
// Load nf-core/<PIPELINE> custom profiles from different Institutions
try {
  includeConfig "${params.custom_config_base}/pipeline/<PIPELINE>.config"
} catch (Exception e) {
  System.err.println("WARNING: Could not load nf-core/config/<PIPELINE> profiles: ${params.custom_config_base}/pipeline/<PIPELINE>.config")
}
```

Commit and push these changes to your local clone on GitHub, and then [create a pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) on the `nf-core/<PIPELINE>` GitHub repo with the appropriate information.

We will be notified automatically when you have created your pull request, and providing that everything adheres to nf-core guidelines we will endeavour to approve your pull request as soon as possible.

### Create the pipeline-specific `nf-core/configs` files

:warning: This has to be done on a fork of the [`nf-core/configs`](https://github.com/nf-core/configs/) repository.

[Fork](https://help.github.com/articles/fork-a-repo/) the [`nf-core/configs`](https://github.com/nf-core/configs/) repository to your own GitHub account.
And add or edit the following files in the local clone of your fork.

* `pipeline/<PIPELINE>.config`

If not already created, create the `pipeline/<PIPELINE>.config` file, and add your custom profile to the profile scope

```Groovy
profiles {
  <PROFILE> { includeConfig "${params.custom_config_base}/conf/pipeline/<PIPELINE>/<PROFILE>.config" }
}
```

* `conf/pipeline/<PIPELINE>/<PROFILE>.config`

Add the custom configuration file to the `conf/pipeline/<PIPELINE>/` directory.
Make sure to add an extra `params` section with `params.config_profile_description`, `params.config_profile_contact` to the top of `pipeline/<PIPELINE>.config` and set to reasonable values.
Users will get information on who wrote the pipeline-specific configuration profile then when executing the nf-core pipeline and can report back if there are things missing for example.

* `docs/pipeline/<PIPELINE>/<PROFILE>.md`

Add the documentation file to the `docs/pipeline/<PIPELINE>/` directory.
You will also need to edit and add your custom profile to the [`README.md`](https://github.com/nf-core/configs/blob/master/README.md) file in the top-level directory of the clone.

* `README.md`

Edit this file, and add the new pipeline-specific institutional profile to the list in the section Pipeline specific documentation

Commit and push these changes to your local clone on GitHub, and then [create a pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) on the `nf-core/configs` GitHub repo with the appropriate information.
In the pull-request description, add a link to the repository specific pull-request(s) that use this new code.
Both PRs will need to be merged at the approximately the same time.

## Help

If you have any questions or issues please send us a message on [Slack](https://nfcore.slack.com/channels/configs).
