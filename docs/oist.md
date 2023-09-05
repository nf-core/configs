# nf-core/configs: OIST Configuration

The nf-core pipelines [rnaseq](https://nf-co.re/rnaseq) and
[eager](https://nf-co.re/eager) have been successfully tested on the _Deigo_
cluster at the Okinawa Institute of Science and Technology Graduate University
([OIST](https://www.oist.jp)). We have no reason to expect that other
pipelines would not work.

To use, run the pipeline with `-profile oist`. This will download and launch
the [`oist.config`](../conf/oist.config) which has been pre-configured with a
setup suitable for _Deigo_. Using this profile, a docker image containing all
of the required software will be downloaded, and converted to a Singularity
image before execution of the pipeline.

## Below are non-mandatory information e.g. on modules to load etc

Before running the pipeline you will need to load Nextflow and Singularity
using the environment module system on _Deigo_. You can do this by issuing the
commands below:

```bash
## Load the latest Nextflow and Singularity environment modules
ml purge
ml bioinfo-ugrp-modules Nextflow2

If you run a _nf-core_ pipeline via the `nf-core` tool, the following command
will load all the modules you need.

```bash
ml bioinfo-ugrp-modules nf-core
```

> NB: You will need an account to use the _Deigo_ cluster in order to run the
> pipeline. If in doubt contact [SCDA](https://groups.oist.jp/scs/documentation).
>
> NB: Nextflow submits the jobs via the SLURM scheduler to the compute nodes.
> You can run the `nextflow` or `nf-core` commands on the login nodes, but
> pay attention that the Nextflow `work` directory must be on the `/flash` file
> system.
