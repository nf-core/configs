# nf-core/configs: AWS Batch with Tower Configuration

To be used when submitting jobs to AWS Batch by using Tower Forge. If you are not using Tower Forge, consider using the profile `awsbatch` where you can directly specify the Batch queue, AWS region and AWS cli path.

This profile defines `awsbatch` as executor, and allows `overwrite` of `trace`, `timeline`, `report` and `dag` to allow resuming pipelines.
