#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

for HEIGHT in {0..630000}
do
    MEDIANTIME=$(bitcoin-cli getblockhash $HEIGHT | xargs bitcoin-cli getblockheader | jq .mediantime)
    echo "$HEIGHT, $MEDIANTIME"
done
