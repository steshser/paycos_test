FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    software-properties-common \
    bzip2 \
    libxtst6 \
    libxtst6 \
    libx11-xcb-dev \
    libdbus-glib-1-2 \
    libxt6 \
    libpci-dev


# Установка Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -y google-chrome-stable

# Установка Mozilla Firefox
RUN apt-get install -y firefox

