# nf-core/configs: CZ Biohub Configuration

All nf-core pipelines have been successfully configured for use on the AWS Batch at the Chan Zuckerberg Biohub here.

To use, run the pipeline with `-profile czbiohub_aws`. This will download and launch the [`czbiohub_aws.config`](../conf/czbiohub_aws.config) which has been pre-configured with a setup suitable for the AWS Batch. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Ask Olga (olga.botvinnik@czbiohub.org) if you have any questions!

## Run the pipeline from a small AWS EC2 Instance

The pipeline will monitor and submit jobs to AWS Batch on your behalf. To ensure that the pipeline is successful, it will need to be run from a computer that has constant internet connection. Unfortunately for us, Biohub has spotty WiFi and even for short pipelines, it is highly recommended to run them from AWS.

### 1. Start tmux

[tmux](https://hackernoon.com/a-gentle-introduction-to-tmux-8d784c404340) is a "Terminal Multiplexer" that allows for commands to continue running even when you have closed your laptop. Start a new tmux session with `tmux new` and we'll name this session `nextflow`.

```bash
tmux new -n nextflow
```

Now you can run pipelines with abandon!

### 2. Make a GitHub repo for your workflows (optional :)

To make sharing your pipelines and commands easy between your teammates, it's best to share code in a GitHub repository. One way is to store the commands in a Makefile ([example](https://github.com/czbiohub/kh-workflows/blob/master/nf-kmer-similarity/Makefile)) which can contain multiple `nextflow run` commands so that you don't need to remember the S3 bucket or output directory for every single one. [Makefiles](https://kbroman.org/minimal_make/) are broadly used in the software community for running many complex commands. Makefiles can have a lot of dependencies and be confusing, so we're only going to write _simple_ Makefiles.

```bash
rnaseq:
nextflow run -profile czbiohub_aws nf-core/rnaseq \
      --reads 's3://czb-maca/Plate_seq/24_month/180626_A00111_0166_BH5LNVDSXX/fastqs/*{R1,R2}*.fastq.gz' \
      --genome GRCm38 \
      --outdir s3://olgabot-maca/nextflow-test/
```

Human_Mouse_Zebrafish:

```bash
nextflow run czbiohub/nf-kmer-similarity -latest -profile aws \
--samples s3://kmer-hashing/hematopoeisis/smartseq2/human_mouse_zebrafish/samples.csv
```

Merkin2012_AWS:

```bash
nextflow run czbiohub/nf-kmer-similarity -latest --sra "SRP016501" \
-r olgabot/support-csv-directory-or-sra \-profile aws
```

In this example, one would run the `rnaseq` rule and the nextflow command beneath it with:

```bash
make rnaseq
```

If one wanted to run a different command, e.g. `human_mouse_zebrafish`, they would specify that command instead. For example:

```bash
make human_mouse_zebrafish
```

Makefiles are a very useful way of storing longer commands with short mnemonic words.

Once you [create a new repository](https://github.com/organizations/czbiohub/repositories/new) (best to initialize with a `.gitignore`, license - MIT and `README`), clone that repository to your EC2 instance. For example, if the repository is called `kh-workflows`, this is what the command would look like:

```bash
git clone https://github.com/czbiohub/kh-workflows
```

Now both create and edit a `Makefile`:

```bash
cd
nano Makefile
```

Write your rule with a colon after it, and on the next line must be a **tab**, not spaces. Once you're done, exit the program (the `^` command shown in nano means "Control"), write the file, add it to git, commit it, and push it up to GitHub.

```bash
git add Makefile
git commit -m "Added makefile"
git push origin master
```

### 3. Run your workflow

Remember to specify `-profile czbiohub_aws` to grab the CZ Biohub-specific AWS configurations, and an `--outdir` with an AWS S3 bucket so you don't run out of space on your small AMI

```bash
nextflow run -profile czbiohub_aws nf-core/rnaseq \
    --reads 's3://czb-maca/Plate_seq/24_month/180626_A00111_0166_BH5LNVDSXX/fastqs/*{R1,R2}*.fastq.gz' \
    --genome GRCm38 \
    --outdir s3://olgabot-maca/nextflow-test/
```

### 4. If you lose connection, how do you restart the jobs

If you close your laptop, get onto the train, or lose WiFi connection, you may lose connection to AWS and may need to restart the jobs. To reattach, use the command `tmux attach` and you should see your Nextflow output! To get the named session, use:

```bash
tmux attach -n nextflow
```

To restart the jobs from where you left off, add the `-resume` flag to your `nextflow` command:

```bash
nextflow run -profile czbiohub_aws nf-core/rnaseq \
    --reads 's3://czb-maca/Plate_seq/24_month/180626_A00111_0166_BH5LNVDSXX/fastqs/*{R1,R2}*.fastq.gz' \
    --genome GRCm38 \
    --outdir s3://olgabot-maca/nextflow-test/ \
    -resume
```

It's important that this command be re-run from the same directory as there is a "hidden" `.nextflow` folder that contains all the metadata and information about previous runs.

## iGenomes specific configuration

A local copy of the iGenomes resource has been made available on `s3://czbiohub-reference/igenomes` (in `us-west-2` region) so you should be able to run the pipeline against any reference available in the `igenomes.config` specific to the nf-core pipeline.

You can do this by simply using the `--genome <GENOME_ID>` parameter.

For Human and Mouse, we use [GENCODE](https://www.gencodegenes.org/) gene annotations. This doesn't change how you would specify the genome name, only that the pipelines run with the `czbiohub_aws` profile would be with GENCODE rather than iGenomes.

> NB: You will need an account to use the HPC cluster on PROFILE CLUSTER in order to run the pipeline. If in doubt contact IT.
> NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.

## High Priority Queue

If you would like to run with the _High Priority_ queue, specify the `highpriority` config profile after `czbiohub_aws`. When applied after the main `czbiohub_aws` config, it overwrites the process `queue` identifier.

To use it, submit your run with with `-profile czbiohub_aws,highpriority`.

**Note that the order of config profiles here is important.** For example, `-profile highpriority,czbiohub_aws` will not work.
