# Use the miminal-notebook as base container
ARG BASE_CONTAINER=jupyter/minimal-notebook
FROM $BASE_CONTAINER

#USER root
# Install CURL
#RUN apt-get install curl jq -y

USER jovyan
# Copy the requirements.txt file
COPY requirements.txt requirements.txt

# Install all Python dependencies
RUN python3 -m pip install -r requirements.txt



# Install the widgets
RUN jupyter nbextension enable --py widgetsnbextension

# The base container takes care of the rest.
