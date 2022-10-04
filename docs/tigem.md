# nf-core/configs: TIGEM configuration

To use, run the pipeline with `-profile tigem`. This will download and launch the tigem.config which has been pre-configured with a setup suitable for the TIGEM personal biocluster.

---

This pipeline can be used on TIGEM clusters, in which is installed slurm as job scheduling system, so you can use this config if you have the same tool installed. An additional parameter is google.zone to allow downloading data from GCP for a specific time zone. It should not interfere with a local or an AWS configuration.
