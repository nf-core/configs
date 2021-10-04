# nf-core/configs: maestro eager specific configuration

Extra specific configuration for eager pipeline for human DNA data processing

## Usage

To use, run the pipeline with `-profile maestro,<qos>,<type>`, where <qos> can be normal or long and <type> can be nuclear or mitochondrial

This will download and launch the eager specific [`maestro.config`](../../../conf/pipeline/eager/maestro.config) which has been pre-configured with a setup suitable for the Maestro cluster.

Example: `nextflow run nf-core/eager -profile maestro,normal,nuclear`

## eager specific configurations for maestro

Specific configurations for maestro has been made for eager.

We decided not to provide any Tool parameter here and focus the profile only for ressource management: Maestro profiles runs with default nf-core/eager parameters, but with modifications concerning time (limit to 24h in normal qos so increasing the memnory and CPUs, specially for alignments).


## nuclear

Increases the number of CPUs and the amount of memory for key processes


##mitochondrial

more limited computational ressources


