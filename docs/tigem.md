# nf-core/configs: TIGEM configuration

To use, run the pipeline with `-profile tigem`. This will download and launch the tigem.config which has been pre-configured with a setup suitable for the TIGEM personal biocluster.

---

This configuration profile can be used on TIGEM clusters, with the pre-installed SLURM job scheduling system. An additional parameter is `google.zone` to allow downloading data from GCP for a specific time zone. It should not interfere with any local or other AWS configuration.
