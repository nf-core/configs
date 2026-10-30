# nf-core/configs: OIST Configuration

To use, run the pipeline with `-profile oist`.
This will download and launch the [`oist.config`](../conf/oist.config), which has been pre-configured for the clusters of the Okinawa Institute of Science and Technology Graduate University ([OIST](https://www.oist.jp)).
Using this profile, container images are pulled and converted to Singularity images before execution of the pipeline.

The `oist` profile is always required.
On its own, it submits tasks to the `compute` partition of _Deigo_, on the AMD nodes (`-C epyc`), with at most 128 CPUs, 500 GB and 96 hours per task.
To run elsewhere, add one of the [sub-profiles](#sub-profiles) after it.

## Loading Nextflow

```bash
ml purge
ml bioinfo-ugrp-modules Nextflow3
```

Pipelines released before they were made compatible with the Nextflow [strict syntax](https://docs.seqera.io/nextflow/strict-syntax) fail with `Nextflow3`, typically with a syntax error in `nextflow.config` or with a boolean parameter reported as a string.
Load `Nextflow2` instead of `Nextflow3` to run them.

## Work directory

By default, Nextflow creates its work directory in the directory where it is launched.
When launching from anywhere other than `/flash` on _Deigo_ or `/work` on _Saion_, for example from `/bucket` or `/home`, always give the work directory with `-w`:

```bash
nextflow run <pipeline> -profile oist -w /flash/<unit>/<user>/work_<run> ...
```

`/bucket` is read-only on compute nodes, and a work directory there makes the run hang and then fail with an uninformative error.

## Interaction with Slurm

| Setting                      | Value     | Effect                                                                       |
| ---------------------------- | --------- | ---------------------------------------------------------------------------- |
| `process.array`              | `96`      | tasks of a process are submitted as job arrays of up to 96 tasks             |
| `executor.submitRateLimit`   | `12/1min` | at most 12 submissions (jobs or job arrays) per minute                       |
| `executor.queueSize`         | `208`     | at most 208 tasks queued or running at once, array tasks included            |
| `executor.queueStatInterval` | `5 min`   | one `squeue` call every 5 minutes                                            |
| `executor.pollInterval`      | `30 sec`  | checks for task completion files in the work directory; does not query Slurm |

Job arrays are incompatible with some pipelines:

- Arrays are not supported by the local executor.
  A pipeline that runs some processes locally, or a run where all tasks use the local executor, stops with `Executor 'local' does not support job arrays`.
- All tasks of an array share the same resources.
  Pipelines that give different resources to each task of a process can hang.

To disable arrays, add `-process.array 0` to the command line.
As of September 2026, the pipelines of [sanger-tol](https://github.com/sanger-tol) and `nf-core/genomeassembler` need it.

## Sub-profiles

A sub-profile is added after `oist`, for example `-profile oist,oist_short`, and replaces only the settings below.

| Sub-profile  | Cluster | Partition | Node constraint | Limits per task      | `queueSize` | `array` |
| ------------ | ------- | --------- | --------------- | -------------------- | ----------- | ------- |
| `oist_short` | Deigo   | `short`   | `-C xeon`       | 40 CPU, 500 GB, 2 h  | 208         | 96      |
| `oist_saion` | Saion   | `intel`   | none            | 40 CPU, 120 GB, 96 h | 40          | 16      |
| `oist_ci`    | Deigo   | `short`   | `-C xeon`       | 4 CPU, 15 GB, 1 h    | 32          | 0       |

`oist_saion` lets Slurm requeue preempted jobs instead of cancelling them, and waits up to one day for a requeued job to restart before Nextflow considers the task failed.

`oist_ci` is for test suites of tens of short tasks, for example `-profile oist,test,oist_ci`.
Its limits replace those of the pipeline's `test` profile.
It also sets `submitRateLimit` to `1/1s`, `pollInterval` to `5 sec` and `queueStatInterval` to `1 min`.
