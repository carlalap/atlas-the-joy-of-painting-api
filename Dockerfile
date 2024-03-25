FROM ubuntu:18.04

RUN apt-get update 
RUN apt-get -y upgrade
RUN apt-get install -y \
    curl \
    wget \
    git \
    vim \
    emacs \
    locales \
    python3.7 \
    python3.7-dev \
    python3-pip \
    tidy

# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# MySQL
RUN echo "mysql-community-server mysql-community-server/data-dir select ''" | debconf-set-selections
RUN echo "mysql-community-server mysql-community-server/root-pass password root" | debconf-set-selections
RUN echo "mysql-community-server mysql-community-server/re-root-pass password root" | debconf-set-selections
RUN echo "mysql-server-5.7 mysql-server/root_password password root" | debconf-set-selections
RUN echo "mysql-server-5.7 mysql-server/root_password_again password root" | debconf-set-selections
RUN apt-get install -y --force-yes mysql-server-5.7
RUN apt-get install -y --force-yes libmysqlclient-dev

# Python
# Instalar paquetes de Python
RUN apt-get install -y \
    build-essential \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libreadline-dev \
    libffi-dev \
    libsqlite3-dev


# Installing Python Packets
RUN pip3 install \
    pycodestyle==2.5 \
    mypy \
    SQLAlchemy \
    flask \
    flask_babel \
    flask-cors \
    pytz \
    requests \
    beautifulsoup4 \
    mysql-connector-python \
    parameterized \
    bs4

# W3C validator
RUN curl -o "/usr/bin/w3c_validator.py" "https://raw.githubusercontent.com/holbertonschool/W3C-Validator/master/w3c_validator.py"
RUN chmod u+x "/usr/bin/w3c_validator.py"
RUN apt-get install -y tidy

# Node JS
RUN curl -sl https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh

RUN apt-get update && apt-get install -y nodejs

# Create test user
RUN useradd -M correction_tester

# Keep the container running indef 
CMD ["tail", "-f", "/dev/null"]