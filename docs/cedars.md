# Cedars-Sinai Medical Center HPC

- You will need HPC access from EIS, which can be requested in the Service Center.
- You will need to load the nextflow module on the HPC before running any pipelines (`module load nextflow`). This should automatically load Java as well.
- Run this with `-profile cedars`
- By default this config file does not specify a queue for submission, and things will thus go to `all.q`. Because of that, the memory and cpu limits have been set accordingly.
- We highly recommend specifying a location of a cache directory to store singularity images (so you re-use them across runs, and not pull each time), by specifying the location with the `$NXF_SINGULARITY_CACHE_DIR` bash environment variable in your `.bash_profile` or `.bashrc`
