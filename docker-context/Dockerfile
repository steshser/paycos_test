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
    libpci-dev \
    xvfb


# Установка Google Chrome и Chrome WebDriver
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -y google-chrome-stable
RUN wget -N https://chromedriver.storage.googleapis.com/LATEST -P /root/
RUN unzip /root/chromedriver_linux64.zip -d /usr/local/bin/

# Установка Mozilla Firefox и GeckoDriver
RUN apt-get update && apt-get install -y firefox
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.29.0-linux64.tar.gz
RUN tar -xzf geckodriver-v0.33.0-linux64.tar.gz -C /usr/local/bin/
RUN chmod +x /usr/local/bin/geckodriver

# Добавляем драйверы в PATH
ENV PATH=$PATH:/usr/local/bin

# Устанавливаем и настраиваем Xvfb (виртуальный X-сервер)
RUN Xvfb :99 -ac &

# Устанавливаем переменную окружения для использования Xvfb
ENV DISPLAY=:99
