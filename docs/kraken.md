# nf-core/configs: KRAKEN Configuration

This profile can be **only** combined with `jenkins.config`. It is used for
testing pipeline with real data on **in-house** cluster located at SciLifeLab.

To use, run the pipeline with `-profile kraken`. This will download and launch
the [`kraken.config`](../conf/kraken.config) which has been pre-configured to
test the pipeline using `docker` by default.

Example: `nextflow run -profile kraken,jenkins`
