<img src="docs/images/nf-core-logo.png" width="400">

# [nf-core/configs](https://github.com/nf-core/configs)
[![Build Status](https://travis-ci.org/nf-core/configs.svg?branch=master)](https://travis-ci.org/nf-core/configs)
[![codecov](https://codecov.io/gh/nf-core/configs/branch/master/graph/badge.svg)](https://codecov.io/gh/nf-core/configs)

A repository for hosting nextflow config files containing custom parameters required to run nf-core pipelines at different Institutions.

## Table of contents

* [Overview](#overview)
* [Testing](#testing)
* [Documentation](#documentation)
* [Uploading to `nf-core/configs`](#uploading-to-nf-core-configs)
* [Help](#help)

## Overview

The Nextflow [`-c`](https://www.nextflow.io/docs/latest/config.html) parameter can be used with nf-core pipelines in order to load custom config files that you have available locally. However, if you or other people within your organisation are likely to be running nf-core pipelines regularly it may be a good idea to create a custom config file that defines some generic settings unique to the computing environment within your organisation. This will ensure that your custom config file will be automatically downloaded, and available at run-time to all `nf-core` pipelines, and to everyone within your organisation. You will simply have to specify `-profile <config_name>` in the command used to run the pipeline.

See [`nf-core/configs`](https://github.com/nf-core/configs/tree/master/conf) for examples.

## Testing

Once you have created your custom config file please can you test that your pipeline of choice runs as expected by using the [`-c`](https://www.nextflow.io/docs/latest/config.html) parameter.

```bash
## Example command for nf-core/rnaseq
nextflow run nf-core/rnaseq --reads '*_R{1,2}.fastq.gz' --genome GRCh37 -c '[path to custom config]'
```

## Documentation

You will have to create a [Markdown document](https://www.markdownguide.org/getting-started/) outlining the details required to use the custom config file within your organisation.

See [`nf-core/configs/docs`](https://github.com/nf-core/configs/tree/master/docs)) for examples.

## Uploading to `nf-core/configs`

[Fork](https://help.github.com/articles/fork-a-repo/) the `nf-core/configs` repository to your own github account. Within the local clone of your fork add the custom config file to the [`conf/`](https://github.com/nf-core/configs/tree/master/conf) directory, and the documentation file to the [`docs/`](https://github.com/nf-core/configs/tree/master/docs) directory. You will also need to edit and add your custom profile to the [`nfcore_custom.config`](https://github.com/nf-core/configs/blob/master/nfcore_custom.config) file in the top-level directory of the clone.

Commit and push these changes to your local clone on GitHub, and then [create a pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) on the `nf-core/configs` GitHub repo.

## Help

We will be notified automatically when you have created your pull request, and providing that everything adheres to `nf-core` guidelines we will endeavour to approve your pull request as soon as possible.

If you have any questions or issues please send us a message on [`Slack`](https://nf-core-invite.herokuapp.com/).
