# nf-core/configs: MUNIN sarek specific configuration

Extra specific configuration for sarek pipeline

## Usage

To use, run the pipeline with `-profile munin`.

This will download and launch the sarek specific [`munin.config`](../../../conf/pipeline/sarek/munin.config) which has been pre-configured with a setup suitable for the `MUNIN` cluster.

Example: `nextflow run nf-core/sarek -profile munin`

## Sarek specific configurations for MUNIN

Specific configurations for `MUNIN` has been made for sarek.

- Params `annotation_cache` and `cadd_cache` set to `true`
- Params `vep_cache_version` set to `95`
- Path to `snpeff_cache`: `/data1/cache/snpEff/`
- Path to `vep_cache`: `/data1/cache/VEP/`
- Path to `pon`: `/data1/PON/vcfs/BTB.PON.vcf.gz`
- Path to `pon_index`: `/data1/PON/vcfs/BTB.PON.vcf.gz.tbi`
- Path to `cadd_indels`: `/data1/cache/CADD/v1.4/InDels.tsv.gz`
- Path to `cadd_indels_tbi`: `/data1/cache/CADD/v1.4/InDels.tsv.gz.tbi`
- Path to `cadd_wg_snvs`: `/data1/cache/CADD/v1.4/whole_genome_SNVs.tsv.gz`
- Path to `cadd_wg_snvs_tbi`: `/data1/cache/CADD/v1.4/whole_genome_SNVs.tsv.gz.tbi`
- Load module `Sentieon` for Processes with `sentieon` labels
