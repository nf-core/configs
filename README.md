<img src="docs/images/nf-core-logo.png" width="400">

# [nf-core/configs](https://github.com/nf-core/configs)

A repository for hosting nextflow config files containing custom parameters required to run nf-core pipelines at different Institutions.

## Table of contents
* [Using an existing config](#using-an-existing-config)
    * [Configuration and parameters](#configuration-and-parameters)
    * [Offline usage](#offline-usage)
* [Adding a new config](#adding-a-new-config)
    * [Testing](#testing)
    * [Documentation](#documentation)
    * [Uploading to `nf-core/configs`](#uploading-to-nf-coreconfigs)
* [Help](#help)

## Using an existing config

The Nextflow [`-c`](https://www.nextflow.io/docs/latest/config.html) parameter can be used with nf-core pipelines in order to load custom config files that you have available locally. However, if you or other people within your organisation are likely to be running nf-core pipelines regularly it may be a good idea to use/create a custom config file that defines some generic settings unique to the computing environment within your organisation.

### Configuration and parameters

The config files hosted in this repository define a set of parameters which are specific to compute environments at different Institutions but generic enough to be used with all nf-core pipelines.

All nf-core pipelines inherit the functionality provided by Nextflow, and as such custom config files can contain parameters/definitions that are available to both. For example, if you have the ability to use [Singularity](https://singularity.lbl.gov/) on your HPC you can add and customise the Nextflow [`singularity`](https://www.nextflow.io/docs/latest/config.html#scope-singularity) scope in your config file. Similarly, you can define a Nextflow [`executor`](https://www.nextflow.io/docs/latest/executor.html) depending on the job submission process available on your cluster. In contrast, the `params` section in your custom config file will typically define parameters that are specific to nf-core pipelines.

You should be able to get a good idea as to how other people are customising the execution of their nf-core pipelines by looking at some of the config files in [`nf-core/configs`](https://github.com/nf-core/configs/tree/master/conf).

### Offline usage

If you want to use an existing config available in `nf-core/configs`, and you're running on a system that has no internet connection, you'll need to download the config file and place it in a location that is visible to the file system on which you are running the pipeline. Then run the pipeline with `--custom_config_base`
or `params.custom_config_base` set to the location of the directory containing the repository files:

```bash
## Download and unzip the config files
cd /path/to/my/configs
wget https://github.com/nf-core/configs/archive/master.zip
unzip master.zip

## Run the pipeline
cd /path/to/my/data
nextflow run /path/to/pipeline/ --custom_config_base /path/to/my/configs/configs-master/
```

Alternatively, instead of using the configuration profiles from this repository, you can run your
pipeline directly calling the single institutional config file that you need with the `-c` parameter.

```bash
nextflow run /path/to/pipeline/ -c /path/to/my/configs/configs-master/conf/my_config.config
```

> Note that the nf-core/tools helper package has a `download` command to download all required pipeline
> files + singularity containers + institutional configs in one go for you, to make this process easier.

## Adding a new config

If you decide to upload your custom config file to `nf-core/configs` then this will ensure that your custom config file will be automatically downloaded, and available at run-time to all nf-core pipelines, and to everyone within your organisation. You will simply have to specify `-profile <config_name>` in the command used to run the pipeline. See [`nf-core/configs`](https://github.com/nf-core/configs/tree/master/conf) for examples.

Please also make sure to add an extra `params` section with `params.  config_profile_name`, `params.config_profile_description`, `params.config_profile_contact` and `params.config_profile_url` set to reasonable values. Users will get information on who wrote the configuration profile then when executing a nf-core pipeline and can report back if there are things missing for example.

### Testing

If you want to add a new custom config file to `nf-core/configs` please test that your pipeline of choice runs as expected by using the [`-c`](https://www.nextflow.io/docs/latest/config.html) parameter.

```bash
## Example command for nf-core/rnaseq
nextflow run nf-core/rnaseq --reads '*_R{1,2}.fastq.gz' --genome GRCh37 -c '[path to custom config]'
```

### Documentation

You will have to create a [Markdown document](https://www.markdownguide.org/getting-started/) outlining the details required to use the custom config file within your organisation. You might orientate yourself using the [Template](docs/template.md) that we provide and filling out the information for your cluster there.

See [`nf-core/configs/docs`](https://github.com/nf-core/configs/tree/master/docs) for examples.

Currently documentation is available for the following clusters:

* [BINAC](docs/binac.md)
* [CCGA](docs/ccga.md)
* [CFC](docs/binac.md)
* [CRICK](docs/crick.md)
* [GIS](docs/gis.md)
* [HEBBE](docs/hebbe.md)
* [MENDEL](docs/mendel.md)
* [MUNIN](docs/munin.md)
* [PHOENIX](docs/phoenix.md)
* [SHH](docs/shh.md)
* [UCT_HEX](docs/uct_hex.md)
* [UPPMAX-DEVEL](docs/uppmax-devel.md)
* [UPPMAX](docs/uppmax.md)
* [UZH](docs/uzh.md)

### Uploading to `nf-core/configs`

[Fork](https://help.github.com/articles/fork-a-repo/) the `nf-core/configs` repository to your own GitHub account. Within the local clone of your fork add the custom config file to the [`conf/`](https://github.com/nf-core/configs/tree/master/conf) directory, and the documentation file to the [`docs/`](https://github.com/nf-core/configs/tree/master/docs) directory. You will also need to edit and add your custom profile to the [`nfcore_custom.config`](https://github.com/nf-core/configs/blob/master/nfcore_custom.config) file in the top-level directory of the clone.

Commit and push these changes to your local clone on GitHub, and then [create a pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) on the `nf-core/configs` GitHub repo with the appropriate information.

We will be notified automatically when you have created your pull request, and providing that everything adheres to nf-core guidelines we will endeavour to approve your pull request as soon as possible.

## Help

If you have any questions or issues please send us a message on [Slack](https://nf-core-invite.herokuapp.com/).
