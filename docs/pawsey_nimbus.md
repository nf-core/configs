# nf-core/configs: Pawsey Nimbus Cloud Configuration

nf-core pipelines have been successfully run on the Nimbus cloud at [Pawsey Supercomputing Centre](https://pawsey.org.au/).

Currently profiles for various [instance flavours](https://support.pawsey.org.au/documentation/display/US/How+to+Choose+a+Flavour), Singularity, and Docker are supported. This config has been developed for the ['Pawsey Bio - Ubuntu 22.04 - 2023-03' image](https://support.pawsey.org.au/documentation/display/US/Nimbus+for+Bioinformatics). Instructions for setting up your instance with an image are [here](https://support.pawsey.org.au/documentation/display/US/Create+a+Nimbus+Instance). Nextflow (v22.10.6), Singularity (v3.8.7), and Docker (v20.10.16) are pre-installed on the 'Pawsey Bio - Ubuntu 22.04 - 2023-03' image.

## Profiles

### Specifying instance flavour

Profiles for various standard instance flavours are available in this config. Please select a profile based on the flavour (i.e. CPUs, and RAM it has access to):

- c2r8: 2 CPU cores, 4Gb RAM
- c4r16: 4 CPU cores, 16 Gb RAM
- c8r32: 8 CPU cores, 32 Gb RAM
- c16r64: 16 CPU cores, 64 Gb RAM

For example, to run the nimbus profile on the c2r8 flavour with Singularity, specify:

```
-profile pawsey_nimbus,singularity,c2r8
```

### Specifying container management tool

Profiles for both Singularity and Docker are available. To run the nimbus profile with Singularity, specify:

```
-profile pawsey_nimbus,singularity
```

To run the nimbus profile with Docker, specify:

```
-profile pawsey_nimbus,docker
```

## Recommendations

Pawsey recommend storing cached nf-core container images on your attached external data volume. By default your Singularity cache directory will be `/home/ubuntu/singularity`. You can override this using the [`NXF_SINGULARITY_CACHEDIR=`](https://www.nextflow.io/docs/latest/singularity.html) environmental variable to change the default cache directory.
