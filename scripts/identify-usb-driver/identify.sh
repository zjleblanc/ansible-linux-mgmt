#!/bin/bash

while getopts m:p: flag
do
    case "${flag}" in
        m) manufacturer=${OPTARG};;
        p) product=${OPTARG};;
    esac
done

if [ -z "$manufacturer" ]; then
    echo "manufacturer (-m) is required"
    echo "example: -m 058f"
    exit 1
fi

info=`lsusb -tvv | grep "$manufacturer:$product" -A 1 | tail -n 1`
sys=`echo $info | cut -d " " -f 1`
dev=`echo $info | cut -d " " -f 2`

echo "sys: $sys"
echo "dev: $dev"