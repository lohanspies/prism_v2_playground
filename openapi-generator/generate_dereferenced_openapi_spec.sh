#!/usr/bin/env bash
openapi-generator-cli generate -i https://k8s-dev.atalaprism.io/docs/prism-agent/api/openapi-spec.yaml -g openapi-yaml -o ./derereferenced_openapi.yml