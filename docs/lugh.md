# nf-core/configs: LUGH configuration

Author: Barry Digby

Contact Info: barry.digby@nuigalway.ie

System Administrator: Chris Duke

## Quick Start

To use the lugh configuration profile with your pipeline, add `-profile lugh` to your `nextflow run` command:

```console
nextflow -bg run nf-core/rnaseq -profile test,nuig
```

Please take care to use the `-bg` flag, or run the job on a compute node.

:warning: DO NOT RUN ANALYSES ON THE HEAD NODE :warning:

The configuration file will load prerequisite modules for users (`Java` & `Singularity`), however it is up to the user to have a functional version of `nextflow` installed in their path. Follow `nextflow` installation instructions at the following [link](https://www.nextflow.io/docs/latest/getstarted.html#installation).

## Queue Resources

| Queue   | Hostnames      | Max Memory | Max CPUS | Max Time |
| ------- | -------------- | ---------- | -------- | -------- |
| MSC     | compute[01-03] | 32GB       | 16       | 336.h    |
| Normal  | compute[10-29] | 64GB       | 16       | 240.h    |
| Highmem | compute[04-09] | 128GB      | 32       | 2880.h   |

---

The configuration profile design is very simple. If your process exceeds 64GB memory or 16 cpus, it is sent to the `highmem` queue. If not, it is sent to the `normal` queue. Please do not use the `MSC` queue, this is reserved for Masters students.

Take others into consideration when deploying your workflow (do not hog the cluster :pig:). If you need to hammer the cluster with a pipeline, please reach out to me and we can tweak the configuration profile to dispatch jobs to only a handful of compute nodes via hostnames.

## Container Cache

Your workflow containers are stored under `/data/containers/` which is accessible to all users on lugh.
