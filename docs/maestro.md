# nf-core/configs Maestro (at Pateur Institute, Paris) Configuration

To use, run the pipeline with `-profile maestro,<qos>` (with qos being long or normal). This will download and launch the maestro.config which has been pre-configured with a setup suitable for the Maestro cluster on either the long or normal qos.
Using one of these profiles, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline

## needed Modules

Please first load java, nextflow and singularity modules
`module load java`
`module load nextflow`
`module load singularity`

Also, do not forget to run nextflow using tmux or alike.

## Other profiles at Pasteur

If you are using TARS cluster, please refer to the [pasteur profile](<(docs/pasteur.md)>).

Please refer to [docs/pasteur.md](docs/pasteur.md) for installing and running nf-core instructions.
