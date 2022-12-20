# Generate Open API Clients from Prism V2 OpenAPI v3 specification
## 1. Install openapi-generator-cli
```bash
npm install @openapitools/openapi-generator-cli -g
```
## 2. CD to correct directory
```bash
cd openapi-generator/
```
## 3. Create dereferenced OpenAPI specification for Prism V2 
```bash
./generate_dereferenced_openapi_spec.sh
```
## 4. Generate Open API Client
```bash
./generate_library.sh 
```