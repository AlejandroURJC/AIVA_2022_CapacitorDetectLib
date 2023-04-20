FROM python:3.10-slim

RUN apt-get update -y && apt-get install -y --no-install-recommends \
      bzip2 \
      g++ \
      git \
      graphviz \
      libgl1-mesa-glx \
      libhdf5-dev \
      openmpi-bin \
      wget && \
    rm -rf /var/lib/apt/lists/* \

# Setting up working directory
RUN mkdir /app
WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Minimize image size
RUN (apt-get autoremove -y; \
     apt-get autoclean -y)

ENTRYPOINT ["python"]

