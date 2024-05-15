# nf-core/configs: Configuration for the MRC LMS Jex cluster

All `nf-core` pipelines have been configured for use on the
[MRC LMS](https://lms.mrc.ac.uk/) Jex cluster and can be used by running with
`-profile jex`.

The [`jex.config`](../conf/jex.config) file has been customised to suit the
cluster's SLURM system and streamlines the use of containerised `nf-core` workflows.
Using this profile, `docker` images containing the required software will be downloaded
and converted to `singularity` images prior to execution and jobs will be submitted
to the correct SLURM partitions and QoS groups. Converted `singularity` images are
cached in a central area to reduce duplication.

To run a pipeline, `nextflow` and `singularity` will need to be loaded into your
environment:

```bash
#
# NOTE:
# We use `module reset` rather than `module purge`, as Jex makes use of various
# default modules that provide a consistent user environment.
#

module reset

module load nextflow
module load singularityce
```

Full documentation on now to run `nextflow` on Jex can be found on the internal
[wiki](http://hpcwiki.lms.mrc.ac.uk). Remember:

> Jex provides a special SLURM partition for running workflow managers, including
> `nextflow`. Manager processes submitted with `--partition ctrl --qos qos_ctrl`
> have elevated priorities and wallclock limits of up to 30 days.

> Jex makes available various shared genome resources to avoid duplication.
> These are located within `/opt/resources` and can be searched and referenced using
> the `asset` command.
