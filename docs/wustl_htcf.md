# nf-core/configs: Washington University, St Louis Center for Genome Sciences HPC Configuration

This is a basic configuration for running nf-core pipelines on the Washington University, St Louis Center for Genome Sciences HPC. To use this configuration, use the following parameter: `-profile wustl_htcf`. This will launch your pipeline of choice with the following configuration: [`wustl_htcf.config`](../conf/wustl_htcf.config). Any given nf-core pipeline will likely require additional parameters to run properly.

Note: you will need to install and maintain nextflow on your own HTCF profile. A common, and current, distribution is not maintained by the WUSTL HTCF sys admins. Personally, I use conda to create a vitual environment, and then download nextflow into it. To do this, make sure to correctly [set your conda channels](https://bioconda.github.io/user/install.html#set-up-channels). Alternatively, you do not need to use conda or a virtual enviornment. You can follow the instructions directly from nextflow:

- Install Nextflow : [here](https://www.nextflow.io/docs/latest/getstarted.html#)

If you need help installing nextflow, find a computational person in your lab, or your neighbor lab, and get their help. If you still need help with this, e-mail me.

To use an nf-core pipeline: 

1. Find the pipeline you're interested in [here](https://nf-co.re/pipelines) and read the documentation thoroughly
2. sign into htcf and cd into your lab's scratch space : `cd /scratch/<your-lab>/$USER`. If you don't know what your lab is called on HTCF, it should be the second word in this output: `id -G -n $USER`
3. run a pipeline according to the given pipeline's instructions. For example, to run the rna-seq test, do the following (this will work directly -- no need to do anything else after you install nextflow): `nextflow run nf-core/rnaseq -profile test,wustl_htcf`

If you're doing things correctly, then all intermediate files required to run the pipeline will be stored in a directory called `/scratch/<your-lab>/$USER/work/`. It is recommended to delete this directory after the pipeline has __successfully__ finished as it can get quite large. Do not delete this directory if you would like to be able to use the `-resume` flag on this particular input set in the future. All of the main output files will be saved in the `results/` directory.

You may run nextflow from where ever you like, but my suggestion is to always run from your `$USER` scratch directory and then move `results/` elsewhere when it has completed. If you happen to run this from `$HOME`, note that you have a 20GB limit which is easily exceeded.

Finally, note that it is highly recommended -- and quite likely required for any given pipeline to successfully complete -- that you use `screen` to submit your nextflow jobs.
