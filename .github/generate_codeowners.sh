#!/usr/bin/env bash

CONFIGS=$(fd . -e .config 'conf/')

output_file=".github/CODEOWNERS"
rm $output_file

for file in $CONFIGS; do
    # Get the line of the file that starts with config_profile_contact
    line=$(rg "config_profile_contact" "$file")
    # and then get the username after the @ and remove anything after it
    username=$(echo "$line" | sed 's/^.*@/@/g')
    # Remove the )'
    username=$(echo "$username" | sed 's/).*$//g')

    # Get the insitute name
    # conf/<institute>.config
    institute=$(echo "$file" | sed 's/^.*\///g' | sed 's/\.config$//g')

    # # Remove quotes from authors
    echo "**$institute**" $username >> $output_file
done
