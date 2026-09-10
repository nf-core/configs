# nf-core/configs: uppmax rnaseq specific configuration

## NGI Stockholm specific configurations for uppmax

When the `SITE` environment variable is set to `NGI-S` (as it is on production miarka in Stockholm), the following params are automatically set for the rnaseq pipeline when using `--genome GRCh38`:

- `gencode = true`
- `save_reference = true`

Usage with nf-core/rnaseq:

```bash
nextflow run nf-core/rnaseq -profile uppmax --genome GRCh38 ...
```

### Params files

Params files are available in `conf/pipeline/rnaseq/uppmax/`, both containing GRCh38 genome reference paths for bed12 and gtf files. They overwrite the genomes map from igenomes from GRCh38 and can then be used even when the `--genome` parameter is set to a different genome.

`rnaseq_sthlm_params.yaml` only contains the genome reference paths, so optional when not using GRCh38.
`rnaseq_sthlm_Pico-V3-trim_UMIs_params.yaml` is mandatory for Pico V3 library prep with UMIs, when using or not using the `--genome GRCh38` parameter.

Example:

```bash
nextflow run nf-core/rnaseq -profile uppmax --genome GRCh38 \
  -params-file conf/pipeline/rnaseq/uppmax/rnaseq_sthlm_Pico-V3-trim_UMIs_params.yaml
```
