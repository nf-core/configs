# [![nf-core/configs](docs/images/nfcore-configs_logo.png "nf-core/configs")](https://github.com/nf-core/configs) <!-- omit in toc -->

[![Lint Status](https://github.com/nf-core/configs/workflows/Configs%20tests/badge.svg)](https://github.com/nf-core/configs/workflows/Configs%20tests/badge.svg)

A repository for hosting Nextflow configuration files containing custom parameters required to run nf-core pipelines at [different institutions](https://nf-co.re/configs).

## Table of contents <!-- omit in toc -->

- [Using an existing config](#using-an-existing-config)
  - [Configuration and parameters](#configuration-and-parameters)
  - [Offline usage](#offline-usage)
- [Adding a new config](#adding-a-new-config)
  - [Testing](#testing)
  - [Documentation](#documentation)
  - [Uploading to `nf-core/configs`](#uploading-to-nf-coreconfigs)
- [Adding a new pipeline-specific config](#adding-a-new-pipeline-specific-config)
  - [Pipeline-specific institutional documentation](#pipeline-specific-institutional-documentation)
  - [Pipeline-specific documentation](#pipeline-specific-documentation)
  - [Enabling pipeline-specific configs within a pipeline](#enabling-pipeline-specific-configs-within-a-pipeline)
  - [Create the pipeline-specific `nf-core/configs` files](#create-the-pipeline-specific-nf-coreconfigs-files)
- [Help](#help)

## Using an existing config

The Nextflow [`-c`](https://www.nextflow.io/docs/latest/config.html) parameter can be used with nf-core pipelines in order to load custom config files that you have available locally.

However, if you or other people within your organisation are likely to be running nf-core pipelines regularly it may be a good idea to use/create a custom config file that defines some generic settings unique to the computing environment within your organisation.

This is where nf-core/configs comes in.
No need to write a custom config, simply run `nextflow run <nf-core pipeline> -profile <hpc_name>` and everything is configured for you!

All currently supported HPCs and infrastructure can be seen on the [nf-core website](https://nf-co.re/configs).

### Configuration and parameters

The config files hosted in this repository define a set of parameters which are specific to compute environments at different institutions but generic enough to be used with all nf-core pipelines.

All nf-core pipelines inherit the functionality provided by Nextflow, and as such custom config files can contain parameters/definitions that are available to both.

For example, if you have the ability to use [Singularity](https://sylabs.io/singularity/) on your HPC you can add and customize the Nextflow [`singularity`](https://www.nextflow.io/docs/latest/config.html#scope-singularity) scope in your config file.
Similarly, you can define a Nextflow [`executor`](https://www.nextflow.io/docs/latest/executor.html) depending on the job submission process available on your cluster.
In contrast, the `params` section in your custom config file will typically define parameters that are specific to nf-core pipelines.

You should be able to get a good idea as to how other people are customising the execution of their nf-core pipelines by looking at some of the config files in [`nf-core/configs`](https://github.com/nf-core/configs/tree/master/conf).

### Offline usage

To use nf-core pipelines offline, we recommend using the `nf-core download` helper tool. This will download both the pipeline files and also the config profiles from `nf-core/configs`. The pipeline files are then edited to load the configs from their relative file path correctly.

```bash
# Download the workflow + transfer to offline cluster
nf-core download rnaseq
scp nf-core-rnaseq-3.0.tar.gz me@myserver.com:/path/to/workflows   # or however you prefer to transfer files to your offline cluster
# Connect to offline cluster
ssh me@myserver.com
# Extract workflow files
cd /path/to/workflows
tar -xzf nf-core-rnaseq-3.0.tar.gz
# Run workflow
cd /path/to/data
nextflow run /path/to/workflows/nf-core-rnaseq-3.0/workflow -profile mycluster
```

If required, you can instead download the nf-core/configs files yourself and customise the `--custom_config_base` / `params.custom_config_base` parameter in each pipeline to to set to the location of the configs directory.

## Adding a new config

If you decide to upload your custom config file to `nf-core/configs` then this will ensure that your custom config file will be automatically downloaded, and available at run-time to all nf-core pipelines, and to everyone within your organisation.

You will simply have to specify `-profile <config_name>` in the command used to run the pipeline.
See [`nf-core/configs`](https://github.com/nf-core/configs/tree/master/conf) for examples.

Before adding your config file to nf-core/configs, we highly recommend writing and testing your own custom config file (as described [above](https://github.com/nf-core/configs#using-an-existing-config)), and then continuing with the next steps.

> [!WARNING]
> In the near future, nf-core/configs will require adherence to Nextflow's 'strict' syntax.
> Ensure you read the documentation [here](https://www.nextflow.io/docs/latest/config.html#config-syntax) and [here](https://www.nextflow.io/docs/latest/strict-syntax.html#configuration-syntax) on how to correctly write and format your config.
> Use of the [language server](https://github.com/nextflow-io/language-server) through the [VSCode Extension](https://nextflow.io/docs/latest/vscode.html) can be helpful for identifying syntax errors.

> [!NOTE]
> In your config file, please also make sure to add an extra `params` section with `params.config_profile_description`, `params.config_profile_contact` and `params.config_profile_url` set to reasonable values.
> Users will get information on who wrote the configuration profile then when executing a nf-core pipeline and can report back if there are things missing for example.

> [!NOTE]
> If you try to specify a shell environment variable within your profile, in some cases you may get an error during testing of something like `Unknown config attribute env.USER_SCRATCH -- check config file: /home/runner/work/configs/configs/nextflow.config` (where the bash environment variable is `$USER_SCRATCH`).
> This is because the GitHub runner used for CI testing will not have your institutional environment variables set. To fix this you can define this as an internal variable, and set a fallback value for that variable. A good example is in the [VSC_UGENT profile](`https://github.com/nf-core/configs/blob/69468e7ca769643b151a6cfd1ab24185fc341c06/conf/vsc_ugent.config#L2`).

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

### Uploading to `nf-core/configs`

> [!WARNING]
> Before you start, make sure you are a part of the nf-core GitHub organisation!
> More information on joining can be found [here](https://nf-co.re/join).

[Fork](https://help.github.com/articles/fork-a-repo/) the [`nf-core/configs`](https://github.com/nf-core/configs/) repository to your own GitHub account.
Within the local clone of your fork:

1.  **add** the custom config file to the [`conf/`](https://github.com/nf-core/configs/tree/master/conf) directory
2.  **add** the documentation file to the [`docs/`](https://github.com/nf-core/configs/tree/master/docs) directory
3.  **edit** and add your custom profile to the [`nfcore_custom.config`](https://github.com/nf-core/configs/blob/master/nfcore_custom.config) file in the top-level directory of the clone
4.  **add** your profile name to GitHub Actions YAML `profile:` scope (under strategy matrix) in [`.github/workflows/main.yml`](.github/workflows/main.yml).

    - If you forget to do this the tests will fail with the error in GitHub Actions:

          ```bash
          Tests don't seem to test these profiles properly. Please check whether you added the profile to the Github Actions testing YAML.
          set(['<profile_name>'])
          ##[error]Process completed with exit code 1.
          ```

> [!WARNING]
> In the near future, nf-core/configs will require adherence to Nextflow's 'strict' syntax.
> Ensure you read the documentation [here](https://www.nextflow.io/docs/latest/config.html#config-syntax) and [here](https://www.nextflow.io/docs/latest/strict-syntax.html#configuration-syntax) on how to correctly write and format your config.
> Use of the [language server](https://github.com/nextflow-io/language-server) through the [VSCode Extension](https://nextflow.io/docs/latest/vscode.html) can be helpful for identifying syntax errors.

Once all the files have been added and updated, commit and push these changes to your local clone on GitHub, and then [create a pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) on the `nf-core/configs` GitHub repo with the appropriate information.

Please request review from @nf-core/maintainers and/or on #request-review on the nf-core slack, and providing that everything adheres to nf-core guidelines we will endeavour to approve your pull request as soon as possible.

> [!NOTE]
> Once you get approval, you as the pull request author MUST merge the pull request.
> Community members cannot be held responsible for the use config on your infrastructure as they do not have permission to test on your infrastructure, therefore the PR author should be the person to merge in the config.
> If you do not see the 'merge' button at the bottom of the PR, ensure you're in nf-core GitHub organisation!
> More information on joining can be found [here](https://nf-co.re/join).

## Adding a new pipeline-specific config

> [!WARNING]
> Before you start, make sure you are a part of the nf-core GitHub organisation!
> More information on joining can be found [here](https://nf-co.re/join).

Sometimes it may be desirable to have configuration options for an institute that are specific to a single nf-core pipeline.
Such options should not be added to the main institutional config, as this will be applied to all pipelines.
Instead, we can create a pipeline-specific institutional config file.

Existing pipeline-specific HPC and infrastructure configs can be seen on the [nf-core website](https://nf-co.re/configs) under the 'pipeline configs column.

> The following steps are similar to the instructions for standard institutional config, however using `pipeline` variants of folders e.g., `conf/pipeline/` or under `pipeline/`

> [!WARNING]
> Remember to replace the `<PIPELINE>` and `<PROFILE>` placeholders with the pipeline name and profile name in the following examples

Institutional configs work because the pipeline `nextflow.config` file loads the [`nf-core/configs/nfcore_custom.config` config file](https://github.com/nf-core/configs/blob/master/nfcore_custom.config), which in turn loads the institutional configuration file based on the profile `<PROFILE>` supplied on the command line.

To add in pipeline-specific institutional configs, we add a second `includeConfig` call in the pipeline `nextflow.config` file, which loads the `pipeline/<PIPELINE>.config` file from the [`nf-core/configs`](https://github.com/nf-core/configs) repo.
This file has `<PIPELINE>` specific institution configuration again with different profiles `<PROFILE>`.

The pipeline `nextflow.config` file should first load the generic institutional configuration file and then the pipeline-specific institutional configuration file.
Each configuration file will add new params and overwrite the params already existing.

Note that pipeline-specific configs are not required and should only be added if needed.

### Enabling pipeline-specific configs within a pipeline

> [!WARNING] > **This has to be done on a fork of the `nf-core/<PIPELINE>` repository.**

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

> [!WARNING]
> This has to be done on a fork of the [`nf-core/configs`](https://github.com/nf-core/configs/) repository.

[Fork](https://help.github.com/articles/fork-a-repo/) the [`nf-core/configs`](https://github.com/nf-core/configs/) repository to your own GitHub account.

And add or edit the following files in the local clone of your fork:

- `pipeline/<PIPELINE>.config`

  If not already created, create the `pipeline/<PIPELINE>.config` file, and add your custom profile to the profile scope

  ```Groovy
  profiles {
    <PROFILE> { includeConfig "${params.custom_config_base}/conf/pipeline/<PIPELINE>/<PROFILE>.config" }
  }
  ```

- `conf/pipeline/<PIPELINE>/<PROFILE>.config`

  Add the custom configuration file to the `conf/pipeline/<PIPELINE>/` directory.
  Make sure to add an extra `params` section with `params.config_profile_description`, `params.config_profile_contact` to the top of `pipeline/<PIPELINE>.config` and set to reasonable values.
  Users will get information on who wrote the pipeline-specific configuration profile then when executing the nf-core pipeline and can report back if there are things missing for example.

- `docs/pipeline/<PIPELINE>/<PROFILE>.md`

  Add the documentation file to the `docs/pipeline/<PIPELINE>/` directory.
  You will also need to edit and add your custom profile to the [`README.md`](https://github.com/nf-core/configs/blob/master/README.md) file in the top-level directory of the clone.

> [!WARNING]
> In the near future, nf-core/configs will require adherence to Nextflow's 'strict' syntax.
> Ensure you read the documentation [here](https://www.nextflow.io/docs/latest/config.html#config-syntax) and [here](https://www.nextflow.io/docs/latest/strict-syntax.html#configuration-syntax) on how to correctly write and format your config.
> Use of the [language server](https://github.com/nextflow-io/language-server) through the [VSCode Extension](https://nextflow.io/docs/latest/vscode.html) can be helpful for identifying syntax errors.

Commit and push these changes to your local clone on GitHub, and then [create a pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) on the `nf-core/configs` GitHub repo with the appropriate information.
In the pull-request description, add a link to the repository specific pull-request(s) that use this new code.

Please request review from @nf-core/maintainers and/or on #request-review on the nf-core slack, and providing that everything adheres to nf-core guidelines we will endeavour to approve your pull request as soon as possible.
Both PRs will need to be merged at the approximately the same time.

> [!NOTE]
> Once you get approval, you as the pull request author MUST merge the pull request.
> Community members cannot be held responsible for the use config on your infrastructure as they do not have permission to test on your infrastructure, therefore the PR author should be the person to merge in the config.
> If you do not see the 'merge' button at the bottom of the PR, ensure you're in nf-core GitHub organisation!
> More information on joining can be found [here](https://nf-co.re/join).

## Help

If you have any questions or issues please send us a message on [Slack](https://nfcore.slack.com/channels/configs).
