# nf-core/configs: uppmax rnaseq specific configuration

## NGI Stockholm specific configurations for uppmax

UPPMAX specific [parameter files](https://docs.seqera.io/nextflow/config#parameter-file) have been made for rnaseq, used by NGI Stockholm for their internal usage of the rnaseq pipeline.

Available params files in `conf/pipeline/rnaseq/uppmax/`:

- `rnaseq_sthlm_params.yaml` — GRCh38 genome reference paths (bed12, gtf) and gencode settings
- `rnaseq_sthlm_Pico-V3-trim_UMIs_params.yaml` — Same as above, with extra TrimGalore arguments (`--clip_r2 14`) for Pico V3 library prep with UMIs
