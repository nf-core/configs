# nf-core/configs: fub_curta methylseq specific configuration

Extra specific configuration for methylseq pipeline

## Usage

To use, run the pipeline with `-profile fub_curta`.

This will download and launch the methylseq specific [`fub_curta.config`](../../../conf/pipeline/methylseq/fub_curta.config) which has been pre-configured with a setup suitable for the `FUB Curta` cluster.

Example: `nextflow run nf-core/methylseq -profile fub_curta`

## methylseq specific configurations for fub_curta

Specific configurations for fub_curta has been made for methylseq.

- The general FUB Curta profile runs with default nf-core/methylseq parameters, but with `stageInMode = copy` in `'NFCORE_METHYLSEQ:METHYLSEQ:PREPARE_GENOME:BISMARK_GENOMEPREPARATION'`. This is due to an error whereby methylseq wouldn't detect the genome with the default `stageInMode = symlink` (see [Slack Thread](https://nfcore.slack.com/archives/CP3RJSMF0/p1701631528797349?thread_ts=1699299636.564489&cid=CP3RJSMF0) and [#305](https://github.com/nf-core/methylseq/issues/305))
