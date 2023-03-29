# nf-core/configs: Sage Bionetworks Global Configuration

To use this custom configuration, run the pipeline with `-profile sage`. This will download and load the [`sage.config`](../conf/sage.config), which contains a number of optimizations relevant to Sage employees running workflows on AWS (_e.g._ using Nextflow Tower). This profile will also load any applicable pipeline-specific configuration.

This global configuration includes the following tweaks:

- Update the default value for `igenomes_base` to `s3://sage-igenomes`
- Enable retries for all failures
- Allow pending jobs to finish if the number of retries are exhausted
- Increase resource allocations for specific resource-related exit codes
- Optimize resource allocations to better "fit" EC2 instance types
- Slow the increase in the number of allocated CPU cores on retries
- Increase the default time limits because we run pipelines on AWS
- Increase the amount of time allowed for file transfers
- Improve reliability of file transfers with retries and reduced concurrency
- Define the `check_max()` function, which is missing in Sarek v2

## Additional information about iGenomes

The following iGenomes prefixes have been copied from `s3://ngi-igenomes/` (`eu-west-1`) to `s3://sage-igenomes` (`us-east-1`). See [this script](https://github.com/Sage-Bionetworks-Workflows/nextflow-infra/blob/main/bin/mirror-igenomes.sh) for more information. The `sage-igenomes` S3 bucket has been configured to openly available, but files cannot be downloaded out of `us-east-1` to avoid egress charges. You can check the `conf/igenomes.config` file in each nf-core pipeline to figure out the mapping between genome IDs (_i.e._ for `--genome`) and iGenomes prefixes ([example](https://github.com/nf-core/rnaseq/blob/89bf536ce4faa98b4d50a8ec0a0343780bc62e0a/conf/igenomes.config#L14-L26)).

- **Human Genome Builds**
  - `Homo_sapiens/Ensembl/GRCh37`
  - `Homo_sapiens/GATK/GRCh37`
  - `Homo_sapiens/UCSC/hg19`
  - `Homo_sapiens/GATK/GRCh38`
  - `Homo_sapiens/NCBI/GRCh38`
  - `Homo_sapiens/UCSC/hg38`
- **Mouse Genome Builds**
  - `Mus_musculus/Ensembl/GRCm38`
  - `Mus_musculus/UCSC/mm10`
