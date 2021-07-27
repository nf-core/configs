# nf-core/configs: LUGH configuration

To use the lugh configuration profile with your pipeline, add `-profile lugh` to your `nextflow run` command. Please take care to use the `-bg` flag or run the job on a compute node. DO NOT RUN ANALYSES ON THE HEAD NODE.

The configuration file will load prerequisite modules for users, however it is entirely up to the user to have a functional version of nextflow installed in their path.

Lugh has 3 queues:

    * `MSC`: compute0{1..3}, 16 cpus, 32GB memory (Please reserve for MSc students only)
    * `normal`: compute{10..29}, 16 cpus, 64GB memory.
    & `highmem`: compute0{4..9}, 32 cpus, 128GB memory.

The configuration profile design is very simple. If your process exceeds 64GB memory or 16 cpus, it is sent to the `highmem` queue. Else, `normal`.

Whilst I (@BarryDigby) am happy to help people set up their nextflow pipelines, please note that I am not the system administrator.

### Container Cache
Your workflow containers will be downloaded and stored at `/data/containers` which is accessible to all users. 
