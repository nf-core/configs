# nf-core/configs: Pawsey Setonix proteinfold specific configuration

Extra specific configuration for proteinfold pipeline

## Usage

To use, run the pipeline with `-profile pawsey_setonix`.

This will download and launch the proteinfold specific [`pawsey_setonix.config`](../../../conf/pipeline/proteinfold/pawsey_setonix.config) which has been pre-configured with a setup suitable for the Pawsey Setonix HPC cluster, including GPU acceleration.

Example: `nextflow run nf-core/proteinfold -profile pawsey_setonix`

## proteinfold specific configurations for Pawsey Setonix

Specific configurations for Pawsey Setonix has been made for proteinfold.

### Project accounting

The config uses the SLURM environmental variable `$PAWSEY_PROJECT` to assign a project code to all task job submissions for accounting purposes. If you are a member of multiple Pawsey projects, you should confirm which project will be charged for your pipeline execution. You can do this using:

```bash
echo $PAWSEY_PROJECT
```

You can manually override the `$PAWSEY_PROJECT` specification by editing your local copy of the `pawsey_setonix.config` and replacing `project_code = "${System.getenv('PAWSEY_PROJECT')}"` with your project code. For example:

```nextflow
process {
    project_code = '<abc>'
    ...
}
```

### GPU allocations

The config sets several GPU specific settings for GPU accelerated steps (Alphafold2, Boltz, Colabfold, ESMfold). These include:
* The correct AMD-GPU container to use
* Number of GCDs per process (i.e. the number of logical GPUs to use per process)
* GPU clusterOptions settings for each relevent task
* containerOptions settings for each relevent task

The only one of these you may need to change is boltz_gcds, as none of the other GPU tools can use more than one logical GPU.

### Cache directories
Both Alphafold2 and Colabfold use JAX and XLA under the hood. These perform JIT (just in time) compilation each time they run, unless you enable caching. With caching enabled, JIT will only be performed for novel conditions. To reduce the time spend running JIT, a JIT cache directory has been specified for both Alphafold2 and Colabfold with the following params settings, which will read and write to your $MYSOFTWARE directory by default, i.e. `/software/projects/$PAWSEY_PROJECT/$USER/`

```nextflow
params {
    alphafold2_jax_compilation_cache_dir = "${System.getenv('MYSOFTWARE')}/jax_cache/alphafold2"
    ...
    colabfold_jax_compilation_cache_dir = "${System.getenv('MYSOFTWARE')}/jax_cache/colabfold"
    ...
}
```

### ⚠️ Expected Warnings
When running the pipeline, you may encounter the following warnings:

```bash
WARN: The following invalid input values have been detected:

* --colabfold_jax_compilation_cache_dir: jax_cache/colabfold
* --colabfold_alphafold2_params_tags.alphafold2_multimer_v3: alphafold_params_colab_2022-12-06
* --colabfold_alphafold2_params_tags.alphafold2_multimer_v2: alphafold_params_colab_2022-03-02
* --colabfold_alphafold2_params_tags.alphafold2_multimer_v1: alphafold_params_colab_2021-10-27
* --colabfold_alphafold2_params_tags.alphafold2_ptm: alphafold_params_2021-07-14
* --alphafold2_jax_compilation_cache_dir: jax_cache/alphafold2
```

These warnings can be safely ignored. 
