# nf-core/configs: National University of Ireland, Galway (Lugh) Configuration

All nf-core pipelines have been successfully configured for use on Lugh at the [National University of Ireland, Galway](http://maths.nuigalway.ie/biocluster/).

To use, run the pipeline with `-profile nuig`. This will download and launch the [`nuig.config`](../conf/nuig.config) which has been pre-configured with a setup suitable for Lugh. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Running nextflow on Lugh

Before running a pipeline you will need a working version of nextflow. Please follow the install instructions below:

- Install Nextflow : [here](https://www.nextflow.io/docs/latest/getstarted.html#)

* Install Nextflow edge:  download the latest source code from Nextflow GitHub [releases](https://github.com/nextflow-io/nextflow/releases). Unpack source code, compile using `make`, add `nextflow` to your  `$PATH` when complete. 

One quirk of Lugh that will produce errors unless addressed: Lugh is not configured to take `memory` parameters in pipelines. This means you will have to make a fork of the pipeline, comment out (`//`) all instances of memory in config files (`nextflow.config`, `base.config`, `test.config` ) AND do away with any instances of `toGiga()` in the pipeline.
