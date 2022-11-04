# nf-core/configs: TIGEM configuration

To use, run the pipeline with `-profile tigem`. This will download and launch the tigem.config which has been pre-configured with a setup suitable for the TIGEM personal biocluster.

## Personal bash configuration

Before running the pipeline, make sure to set these environment variables in your bash profile. You can either copy and past these line in your command line or set them as global environment variables adding them in your .bashrc personal file.

```bash
# set your personal path
# >>> nf-core variables >>>
export NXF_SINGULARITY_CACHEDIR="/personal/path/.singularity/"
export SINGULARITY_CACHEDIR="/personal/path/.singularity"
export SINGULARITY_TMPDIR="/personal/path/.singularity"
# <<< nf-core variables <<<
```

---

This configuration profile can be used on TIGEM clusters, with the pre-installed SLURM job scheduling system. An additional parameter is `google.zone` to allow downloading data from GCP for a specific time zone. It should not interfere with any local or other AWS configuration.
