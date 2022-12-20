# Generate Open API Clients from Prism V2 OpenAPI v3 specification
## 1. Install openapi-generator-cli
```bash
npm install @openapitools/openapi-generator-cli -g
```

## 2. Install Python openapi-python-client
```bash
pip3 install openapi-python-client
```
## 3. CD to correct directory
```bash
cd openapi-generator/
```
## 4. Create dereferenced OpenAPI specification for Prism V2 
```bash
./generate_dereferenced_openapi_spec.sh
```
## 5. Generate or Update Open API Client
If client library don't exist then generate a new version  
```bash
./generate_client_library.sh 
```

If client library already exist then update the current version
```bash
./update_client_library.sh 
```