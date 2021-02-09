# nf-core/configs: shh eager specific configuration

Extra specific configuration for eager pipeline

## Usage

To use, run the pipeline with `-profile shh`.

This will download and launch the eager specific [`shh.config`](../../../conf/pipeline/eager/shh.config) which has been pre-configured with a setup suitable for the shh cluster.

Example: `nextflow run nf-core/eager -profile shh`

## eager specific configurations for shh

Specific configurations for shh has been made for eager.

### General profiles

* If running with the MALT module turned on, the MALT process by default will be sent  to the long queue with a resource requirement minimum of 725GB and 64 cores. If this fails, the process will be tried once more only and sent to the supercruncher queue. The module will not retry after this, and pipeline will fail. Note, this will only work on SDAG.

### Contextual profiles

#### Microbiome Sciences

* `microbiome_screening` runs MALT straight to supercruncher (with no retries!) and full resources requested due to microbiome screening databases often easily reach this size

#### Human Pop-Gen

* `human`: optimised for mapping of human aDNA reads (i.e. bwa aln defaults as `-l 16500, -n 0.01`)

#### Pathogen

* `pathogen_loose`: optimised for mapping of human aDNA reads (i.e. bwa aln defaults as `-l 16 -n 0.01`)
* `pathogen_strict`: optimised for mapping of human aDNA reads (i.e. bwa aln defaults as `-l 32, -n 0.1`)
* `hops`: profile with default paths and parameters for automated/initial pathogen screening.
  * :warning: This is NOT a reproducible profile as it contains hardcoded paths. This should only be used for initial/automated screening where you wish to quickly check for any possible positives; after which you should re-do screening in a reproducible manner for publication!
