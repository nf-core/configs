# nf-core/configs: MUNIN rnavar specific configuration

Extra specific configuration for rnavar pipeline

## Usage

To use, run the pipeline with `-profile munin`.

This will download and launch the rnavar specific [`munin.config`](../../../conf/pipeline/rnavar/munin.config) which has been pre-configured with a setup suitable for the `MUNIN` cluster.

Example: `nextflow run nf-core/rnavar -profile munin`

## rnavar specific configurations for MUNIN

Specific configurations for `MUNIN` has been made for rnavar.

Genome references

- Path to `fasta`: `/data1/references/CTAT_GenomeLib_v37_Mar012021/GRCh38_gencode_v37_CTAT_lib_Mar012021.plug-n-play/ctat_genome_lib_build_dir/ref_genome.fa`
- Path to `fasta_fai`: `/data1/references/CTAT_GenomeLib_v37_Mar012021/GRCh38_gencode_v37_CTAT_lib_Mar012021.plug-n-play/ctat_genome_lib_build_dir/ref_genome.fa.fai`
- Path to `gtf`: `/data1/references/CTAT_GenomeLib_v37_Mar012021/GRCh38_gencode_v37_CTAT_lib_Mar012021.plug-n-play/ctat_genome_lib_build_dir/ref_annot.gtf`
- Path to `gene_bed`: `/data1/references/CTAT_GenomeLib_v37_Mar012021/GRCh38_gencode_v37_CTAT_lib_Mar012021.plug-n-play/ctat_genome_lib_build_dir/ref_annot.bed`

Known genome resources

- Path to `dbsnp`: `/data1/references/annotations/GATK_bundle/dbsnp_146.hg38.vcf.gz`
- Path to `dbsnp_tbi`: `/data1/references/annotations/GATK_bundle/dbsnp_146.hg38.vcf.gz.tbi`
- Path to `known_indels`: `/data1/references/annotations/GATK_bundle/Mills_and_1000G_gold_standard.indels.hg38.vcf.gz`
- Path to `known_indels_tbi`: `/data1/references/annotations/GATK_bundle/Mills_and_1000G_gold_standard.indels.hg38.vcf.gz.tbi`

STAR index

- Path to `star_index`: `/data1/references/CTAT_GenomeLib_v37_Mar012021/GRCh38_gencode_v37_CTAT_lib_Mar012021.plug-n-play/ctat_genome_lib_build_dir/STAR.2.7.9a_2x151bp/`
- Params `read_length` set to `151`

Variant annotation configurations

- Params `annotation_cache` and `cadd_cache` set to `true`
- Params `snpeff_db` set to `GRCh38.99`
- Params `vep_cache_version` set to `99`
- Params `vep_genome` set to `GRCh38`
- Path to `snpeff_cache`: `/data1/cache/snpEff/`
- Path to `vep_cache`: `/data1/cache/VEP/`
- Path to `pon`: `/data1/PON/vcfs/BTB.PON.vcf.gz`
- Path to `pon_index`: `/data1/PON/vcfs/BTB.PON.vcf.gz.tbi`
- Path to `cadd_indels`: `/data1/cache/CADD/v1.4/InDels.tsv.gz`
- Path to `cadd_indels_tbi`: `/data1/cache/CADD/v1.4/InDels.tsv.gz.tbi`
- Path to `cadd_wg_snvs`: `/data1/cache/CADD/v1.4/whole_genome_SNVs.tsv.gz`
- Path to `cadd_wg_snvs_tbi`: `/data1/cache/CADD/v1.4/whole_genome_SNVs.tsv.gz.tbi`
