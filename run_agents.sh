#!/usr/bin/env bash
./agent/run.sh -n issuer -p 8080 -b;./agent/run.sh -n holder -p 8090 -b;./agent/run.sh -n verifier -p 9000 -b