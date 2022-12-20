#!/usr/bin/env bash
#openapi-generator-cli generate -i https://k8s-dev.atalaprism.io/docs/prism-agent/api/openapi-spec.yaml -g openapi-yaml -o ./derereferenced_openapi.yml

openapi-generator-cli generate -i http://127.0.0.1:8080/prism-agent/api/openapi-spec.yaml -g openapi-yaml -o ./derereferenced_openapi.yml