#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

LAST=$(tail -n 1 block-data.csv | cut -d, -f1)
HEIGHT=$(bitcoin-cli getblockchaininfo | jq .blocks)

START=$((LAST + 1))

for (( CURRENT=$START; CURRENT<=$HEIGHT; CURRENT++ ))
do
    TIME=$(bitcoin-cli getblockhash $CURRENT | xargs bitcoin-cli getblockheader | jq .time)
    echo "$CURRENT,$TIME"
done
