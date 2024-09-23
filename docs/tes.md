# nf-core/configs: GA4GH TES Configuration

To be used with the `tes` profile by specifying the `-profile tes` when running nf-core pipelines.
Custom endpoints and authentication need to be supplied with `params.endpoint`, `params.basicUsername`, `params.basicPassword`.
Additionally you will need to add the `-plugin nf-ga4gh` at command line to import the correct plugin. 

## Required Parameters

### `--endpoint`

URL of TES endpoint.

### `--basicUsername`

Username for authentication for TES endpoint.

### `--basicPassword`

Password for authentication for TES endpoint.
