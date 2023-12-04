# nf-core/configs: self-hosted-runner Configuration

To use, run the pipeline with `-profile self-hosted-runner`. This will download and launch the [`self-hosted-runner.config`](../conf/self-hosted-runner.config) which has been pre-configured with a setup suitable for the self-hosted-runners (for now on AWS via terraform). The main aim of this profile is to fix the permission errors on self-hosted GitHub actions runners.
