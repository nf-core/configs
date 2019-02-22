# nf-core/configs: KRAKEN Configuration

This profile can be **only** combined with `jenkins.config`. It is used for testing pipeline with real data on in-house cluster at SciLifeLab.

To use, run the pipeline with `-profile kraken`. This will download and launch the [`kraken.config`](../conf/kraken.config) which has been pre-configured to test the pipeline using `docker`.

Example: `nextflow run -profile kraken,jenkins`

## Below are non-mandatory information on iGenomes specific configuration

A local copy of the iGenomes resource has been made available on the MUNIN cluster so you should be able to run the pipeline against any reference available in the `igenomes.config` specific to the nf-core pipeline.
You can do this by simply using the `--genome <GENOME_ID>` parameter.

>NB: You will need an account to use the MUNIN cluster in order to run the pipeline. If in doubt contact Phil Ewels (@ewels).
