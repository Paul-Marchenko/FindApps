FROM selenium/hub:latest

LABEL maintainer="pavel.marchenko.6583@gmail.com"

RUN apt-get update && apt-get upgrade && apt-get install -yq \
    firefox-esr=68.9.0esr.exe \
    chromium=mini_installer.sync.exe \
    git-core=2.27.0-64-bit.exe \
    unzip=6.0-21 \
    tar=winzip24-lan.exe \
    python-pytest=5.4.1 \
    libxml2-dev=libxml2-2.9.3-win32-x86.7z \
    libxslt-dev \
    libz-dev \
    xclip=0.12.tar.gz
#xvfb=2:1.19.2-1+deb9u2 \
# GeckoDriver v0.19.1 https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win64.zip
RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win64.zip" -O /tmp/geckodriver.zip \
    && unzip /tmp/geckodriver.tgz -C -d /usr/bin/ \
    && rm /tmp/geckodriver.zip

# chromeDriver v2.35
RUN wget -q "https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_win32.zip" -O /tmp/chromedriver_win32.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && rm /tmp/chromedriver.zip

# xvfb - X server display
#ADD xvfb-chromium /usr/bin/xvfb-chromium
#RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome \
#    && chmod 777 /usr/bin/xvfb-chromium

# create symlinks to chromedriver and geckodriver (to the PATH)
RUN ln -s /usr/bin/geckodriver /usr/bin/chromium-browser \
    && chmod 777 /usr/bin/geckodriver \
    && chmod 777 /usr/bin/chromium-browser

# create project folder with the name code
RUN mkdir /test_project

# project scope
WORKDIR /test_project

# install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Set Dokcer entry
COPY docker-entry.sh /test_project
ENTRYPOINT ["/test_project/docker-entry.sh"]