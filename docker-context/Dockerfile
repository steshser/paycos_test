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


# Установка Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -y google-chrome-stable

# Установка Mozilla Firefox
RUN apt-get install -y firefox

# Установка Chrome WebDriver
RUN wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/118.0.5993.70/linux64/chromedriver-linux64.zip -O /tmp/chromedriver-linux64.zip
RUN unzip /tmp/chromedriver-linux64.zip -d /tmp
RUN mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver
RUN chmod +x /usr/local/bin/chromedriver
RUN chromedriver --version

# Установка GeckoDriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz -O /tmp/geckodriver.tar.gz
RUN tar -xzf /tmp/geckodriver.tar.gz -C /tmp
RUN mv /tmp/geckodriver /usr/local/bin/geckodriver
RUN chmod +x /usr/local/bin/geckodriver
RUN geckodriver --version

# Устанавливаем и настраиваем Xvfb (виртуальный X-сервер)
RUN Xvfb :99 -ac &

# Устанавливаем переменную окружения для использования Xvfb
ENV DISPLAY=:99
