# nf-core/configs: Freie Universiät Berlin High-Performance Computer (Curta) Configuration

> **NB:** In order to run pipelines using this HPC cluster, you must first apply for access [here](https://ssl2.cms.fu-berlin.de/fu-berlin/en/sites/high-performance-computing/PM_Zugang-beantragen/index.html).

This profile is configured to run with Apptainer, which is pre-loaded and globally available to all users on the cluster.

Nextflow should be loaded into your environment before use. The following should be added to your Slurm script:

```bash
module load Nextflow
```

Using `-profile fub_curta` will download [`fub_curta.config`](../conf/fub_curta.config), which has been pre-configured with a setup suitable for the Curta cluster.

## Additional Profiles

A profile for deactivating the cleanup of intermediate files is also offered.

### debug

This simply turns off automatic clean up of intermediate files, which can be useful for debugging. It is specified with `-profile fub_curta,debug`.

## Publications

If computing time on Curta has contributed to a publication or the completion of a degree course, please send us the corresponding DOI or BibTeX entry and, if possible, an appropriate image to hpc@zedat.fu-berlin.de. This is the ONLY way we can document the usefulness of our service.

The current list of publications is available [here](https://www.fu-berlin.de/en/sites/high-performance-computing/Forschungsergebnisse).

Please also acknowledge the use of our service in any publications you produce, using the following [reporting guidelines](https://www.fu-berlin.de/en/sites/high-performance-computing/FAQ/Publikationen), including the DOI [10.17169/refubium-26754](http://dx.doi.org/10.17169/refubium-26754).

## Acknowledgments

This configuration was refined with Dr. Loris Bennett's help [@tardigradus](https://github.com/tardigradus) of the HPC Team from the FUB ZEDAT's Scientific Computing Unit.
