#!/usr/bin/env nextflow

workflow {
    def separator = "-" * 40
    print("${separator}\n")
    print("Parameter scope for config \'${workflow.profile}\'\n")
    print("${separator}\n")
    params.each { param ->
        assert param
        print("\t${param}\n")
    }
}
