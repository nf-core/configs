# nf-core/configs: MUNIN sarek specific configuration

Extra specific configuration for sarek pipeline

## Usage

To use, run the pipeline with `-profile munin`.

This will download and launch the sarek specific [`munin.config`](../conf/pipeline/sarek/munin.config) which has been pre-configured with a setup suitable for the MUNIN cluster.

Example: `nextflow run nf-core/sarek -profile munin`

## Sarek specific configurations for MUNIN

Specific configurations for MUNIN has been made for sarek.

* Params `annotation_cache` set to `true`
* Path to `snpEff_cache`: `/data1/cache/snpEff/`
* Path to `vep_cache`: `/data1/cache/VEP/`
* Path to `pon`: `/data1/PON/vcfs/BTB.PON.vcf.gz`
* Path to `pon_index`: `/data1/PON/vcfs/BTB.PON.vcf.gz.tbi`
* Load module `Sentieon` for Processes with `sentieon` labels
