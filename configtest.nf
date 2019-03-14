#!/usr/bin/env nextflow

def separator = "-"*40
print("$separator\n")
print("Parameter scope for config \'${workflow.profile}\'\n")
print("$separator\n")
params.each {
    assert it
    print("\t$it\n")
}