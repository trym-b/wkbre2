FROM ubuntu:24.04

RUN apt-get update
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get install \
    --assume-yes \
    g++ \
    git \
    wget \
    libbz2-dev \
    libenet-dev \
    libglew-dev \
    libmpg123-dev \
    libopenal-dev \
    libsdl2-dev \
    make \
    nlohmann-json3-dev

RUN mkdir /3rdParty/ && \
    cd /3rdParty/ && \
    git clone https://github.com/nothings/stb.git
RUN cd /3rdParty/stb && \
    git checkout f1c79c02822848a9bed4315b12c8c8f3761e1296

RUN mkdir /3rdParty/sol && \
    cd /3rdParty/sol && \
    wget https://github.com/ThePhD/sol2/releases/download/v3.3.0/sol.hpp && \
    wget https://github.com/ThePhD/sol2/releases/download/v3.3.0/config.hpp && \
    wget https://github.com/ThePhD/sol2/releases/download/v3.3.0/forward.hpp

RUN mkdir inc
RUN cp --recursive /3rdParty/stb inc
RUN cp --recursive /3rdParty/sol inc

COPY . .

RUN cd wkbre2 && \
    make -f ../Makefile
