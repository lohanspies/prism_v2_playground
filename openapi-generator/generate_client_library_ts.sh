#!/usr/bin/env bash
openapi-generator-cli generate \
  -i https://bg65j.atalaprism.io/docs/prism-agent/api/openapi-spec.yaml \
  -o prism-agent-ts-open-api \
  -g typescript-fetch \
  --additional-properties=supportsES6=true,typescriptThreePlus=true