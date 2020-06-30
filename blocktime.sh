#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

for HEIGHT in {0..100}
do
    MEDIANTIME=$(bitcoin-cli getblockhash $HEIGHT | xargs bitcoin-cli getblockheader | jq .time)
    echo "$HEIGHT, $MEDIANTIME"
done
