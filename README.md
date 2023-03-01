# Prism V2 Playground

This repo contains a jupyter notebook that runs from a docker container. It's an easy way to interact with the PRISM Agent APIs via python jupyter-notebook.


## Run
Install and start [Docker Desktop](https://www.docker.com/products/docker-desktop/) in your local machine and use the docker-compose command to start the container:
```
cd <path>/prism_v2_playground
docker-compose up -d
```

## Stop

```
docker-compose down

```

## Access

This is the default location of the notebook:

```
http://127.0.0.1:8888/
```

The default password is `Prismv2`

In order to make the container publicly available, edit `docker-compose.yaml` and replace `- "127.0.0.1:8888:8888"` 
with `- "8888:8888"`. Remember, changing the port and host inside `jupyter-config.json` will only change the settings
inside the container, and likely to break the notebook.

## ℹ️ Configure (Optional steps)

The config files are located in `./config` folder, edit the `jupyter-config.json` for customization.

Remember that the local `./config` dir is mounted as `/home/jovyan/.jupyter/config` within the container.

### Passphrase

The default passphrase to access the notebook is `Prismv2`.

You will need to edit the `./config/jupyter-config.json` file and change the value of `NotebookApp.password` key. The
passphrase can be generated using the following command:

```yaml
./passphrase
```

Use the output of the command to set the `NotebookApp.password` key.

### ssl

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
