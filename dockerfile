FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
      bzip2 \
      g++ \
      git \
      graphviz \
      libgl1-mesa-glx \
      libhdf5-dev \
      openmpi-bin \
      wget \
      python3-tk && \
    rm -rf /var/lib/apt/lists/*
# Setting up working directory
RUN mkdir /app
WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Minimize image size
RUN (apt-get autoremove -y; \
     apt-get autoclean -y)

ENV QT_X11_NO_MITSHM=1
ENTRYPOINT ["python"]
