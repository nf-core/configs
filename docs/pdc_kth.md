# nf-core/configs: PDC Configuration

nf-core pipelines have been successfully configured for use on the PDC
cluster dardel. No other clusters have yet been tested, but support can be
added if needed.

## Getting started

The base java installation on dardel is Java 11. By loading the `PDC`
and `Java` module, different versions (e.g. 17) are available.

To pull new singularity images, singularity must be available
(e.g. through the module system) to the nextflow monitoring process,
suggested preparatory work before launching nextflow is:

```shell

module load PDC Java singularity
```

(for reproducibility, it may be a good idea to check what versions you
have loaded with `module list` and using those afterwards, e.g.
`module load PDC/22.06 singularity/3.10.4-cpeGNU-22.06 Java/17.0.4`.)

No singularity images or nextflow versions are currently preloaded on
dardel, to get started you can e.g. download nextflow through

```shell
wget https://raw.githubusercontent.com/nextflow-io/nextflow/master/nextflow && \
  chmod a+x nextflow
```

The profile `pdc_kth` has been provided for convenience, it expects you to
pass the project used for slurm accounting through `--project`, e.g.
`--project=nais2023-22-1027`.

Due to [how partitions are set
up](https://www.pdc.kth.se/support/documents/run_jobs/job_scheduling.html#dardel-partitions)
on dardel, in particular the lack of long-runtime nodes with more
memory. Some runs may be difficult to get through.

Note that node local scratch is not available and `SNIC_TMP` as well
as `PDC_TMP` point to a cluster-scratch area that will have similar
perfomance characteristics as your project storage. `/tmp` points to a
local `tmpfs` which uses RAM to store contents. Given that nodes don't
have swap space anything stored in `/tmp` will mean less memory is
available for your job.
