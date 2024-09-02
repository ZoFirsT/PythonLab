#!/bin/bash
mkdir -p outs
for filename in ./testcases/*.in; do
    echo "Running Case $(basename "$filename" .in) ..."
    python main.py < "$filename" > "outs/$(basename "$filename" .in).out"
    file1="./testcases/$(basename "$filename" .in).out"
    file2="./outs/$(basename "$filename" .in).out"

    # Check if the files exist
    if [ ! -e "$file1" ]; then
        echo "File '$file1' does not exist."
        exit 1
    fi

    if [ ! -e "$file2" ]; then
        echo "File '$file2' does not exist."
        exit 1
    fi

    # Use diff to compare the files
    diff --strip-trailing-cr "$file1" "$file2" > /dev/null

    if [ $? -eq 0 ]; then
        echo "Results: Matched, Good job!"
    else
        echo "Results: NOT Matched, Please check your code!"
        # Use diff to compare the files and colorize the output
        # colordiff -u --strip-trailing-cr "$file1" "$file2"
        diff -y --strip-trailing-cr "$file1" "$file2"
    fi
    echo ""
done
