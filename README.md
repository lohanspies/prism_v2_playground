# Prism V2 Playground

This repo contains a Jupyter Notebook that runs from a docker container.  
It's an easy way to interact with the PRISM Agent APIs via python jupyter-notebook.  
It also includes scripts to run local Prism Agents. The default script will start/stop three Prism Agents for the various actors (`issuer`,`holder`, `verifier`) used as part the Prism Playground.  

## Prerequisites 
Install and start [Docker Desktop](https://www.docker.com/products/docker-desktop/) and `docker-compose` in your local machine and ensure you have an active internet connection.  
To start the Prism Playground you can use the commands below to start and stop the Jupyter Notebook server and Prism Agents.

## Run
```bash
cd <path>/prism_v2_playground

# Starting the Jupyter Notebook Server
docker-compose up -d

# Starting the local Prism Agents.
./run_agents.sh
```

## Stop
```bash
cd <path>/prism_v2_playground

# Stopping the Jupyter Notebook Server
docker-compose down

# Stopping the local Prism Agents.
./stop_agents.sh
```

## Access the Jupyter Notebook

This is the default location of the notebook:

```bash
http://127.0.0.1:8888/
```

The default password is `Prismv2`

## ℹ️ Configure Jupyter Notebook Environment (Optional steps)

The config files are located in `./config` folder, edit the `jupyter-config.json` for customization.

Remember that the local `./config` dir is mounted as `/home/jovyan/.jupyter/config` within the container.

### Exposing the Jupyter Notebooks publicly
> ℹ️ 
In order to make the container publicly available, edit `docker-compose.yaml` and replace `- "127.0.0.1:8888:8888"` 
with `- "8888:8888"`. Remember, changing the port and host inside `jupyter-config.json` will only change the settings
inside the container, and likely to break the notebook.

### Passphrase

The default passphrase to access the notebook is `Prismv2`.

You will need to edit the `./config/jupyter-config.json` file and change the value of `NotebookApp.password` key. The
passphrase can be generated using the following command:

```bash
./passphrase
```

Use the output of the command to set the `NotebookApp.password` key.

### SSL

If you choose to set ssl certificates, place them in the `./config` folder and state the location of the files
as absolute paths in `./config/jupyter-config.json` starting with `/home/jovyan/work`:

```json
{
  "NotebookApp": {

    "certfile": "/home/jovyan/.jupyter/config/ssl-cert.pem",
    "keyfile": "/home/jovyan/.jupyter/config/ssl-cert.key",

  }
}
```
