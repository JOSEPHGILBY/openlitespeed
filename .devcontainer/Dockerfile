FROM almalinux:8.4

ARG PHP_VERSION

RUN dnf update -y 
RUN dnf install -y wget tar git go
# RUN apt-get update && apt-get install wget curl cron tzdata -y

#RUN wget https://openlitespeed.org/preuse/openlitespeed-$OLS_VERSION.tgz && \
#    tar xzf openlitespeed-$OLS_VERSION.tgz && cd openlitespeed 
    #&& ./install.sh && \ echo 'cloud-docker' > /usr/local/lsws/PLAT && rm -rf /openlitespeed && rm /openlitespeed-$OLS_VERSION.tgz

RUN /workspaces/openlitespeed/build.sh
RUN /workspaces/openlitespeed/install.sh && \ 
    echo 'cloud-docker' > /usr/local/lsws/PLAT


