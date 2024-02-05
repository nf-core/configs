# nf-core/configs: Freie Universität Berlin _Curta_ Configuration

> **NB:** In order to run pipelines using this HPC cluster, you must first apply for access [here](https://ssl2.cms.fu-berlin.de/fu-berlin/en/sites/high-performance-computing/PM_Zugang-beantragen/index.html).

Job limits are capped at 32 CPUs, 772 GB and a maximum run time of 14 days.

This profile is configured to run with Apptainer, which is pre-loaded and globally available to all users on the cluster.

First, Nextflow should be loaded into your interactive session or added to your Slurm script using:

```bash
module load Nextflow
```

> Note: There exists different version modules for Nextflow on the cluster. This command ensures loading the latest version.

Using `-profile fub_curta` will download the config file, which has been pre-configured with a setup suitable for the Curta cluster.

The default partition for job submissions is `main`. The user has access to 166 nodes on `main`. The profile automatically detects whether the user belongs to the BeGenDiv working group, and gives the user access to 4 more nodes by making use of the `begendiv` partition together with `main`, giving precedence to the former.

In addition, job submissions are assigned the appropriate quality of service (QOS) as such:

- `hiprio` for `task.time <= 3.h`
- `prio` for `task.time <= 3.d`
- `standard` for `task.time <= 14.d`

Institute-specific pipeline profiles exists for:

- [methylseq](pipeline/methylseq/fub_curta.md)

## debug profile

Deactivating the cleanup of intermediate files is also possible. It is done by specifying `-profile fub_curta,debug`. This simply turns off automatic clean up of intermediate files, which can be useful for debugging.

## Publications

If computing time on Curta has contributed to a publication or the completion of a degree course, please send us the corresponding DOI or BibTeX entry and, if possible, an appropriate image to hpc@zedat.fu-berlin.de. This is the ONLY way we can document the usefulness of our service.

The current list of publications is available [here](https://www.fu-berlin.de/en/sites/high-performance-computing/Forschungsergebnisse).

Please also acknowledge the use of our service in any publications you produce, using the following [reporting guidelines](https://www.fu-berlin.de/en/sites/high-performance-computing/FAQ/Publikationen), including the DOI [10.17169/refubium-26754](http://dx.doi.org/10.17169/refubium-26754).
