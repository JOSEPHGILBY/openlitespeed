#!/bin/sh
PHP_VERSION="lsphp81"
DIR=$(dirname "$0")

cp ./clone_repo.sh /usr/local/bin
chmod +x /usr/local/bin/clone_repo.sh

if [ ! -f "$DIR/../BUILD_DONE" ]; then
    # If the BUILD_DONE file doesn't exist, call build.sh and create the BUILD_DONE file
    "$DIR/../build.sh" Debug
    if [ $? -ne 0 ] ; then
        exit 1
    fi
    touch "$DIR/../BUILD_DONE"
fi
"$DIR/../install.sh"
if [ $? -ne 0 ] ; then
    exit 1
fi
echo 'cloud-docker' > /usr/local/lsws/PLAT

dnf install -y mysql $PHP_VERSION $PHP_VERSION-mysqlnd $PHP_VERSION-common $PHP_VERSION-opcache \
   $PHP_VERSION-curl $PHP_VERSION-imagick $PHP_VERSION-redis $PHP_VERSION-memcached $PHP_VERSION-intl

/bin/bash -c "if [[ $PHP_VERSION == lsphp7* ]]; then dnf install $PHP_VERSION-json -y; fi"

curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
chmod +x wp-cli.phar 
mv wp-cli.phar /usr/bin/wp
ln -s /usr/local/lsws/$PHP_VERSION/bin/php /usr/bin/php

dnf install -y crontabs cronie cronie-anacron socat
wget -O -  https://get.acme.sh | sh

cp "$DIR/docker.conf" /usr/local/lsws/conf/templates/docker.conf
cp "$DIR/setup_docker.sh" /usr/local/lsws/bin/setup_docker.sh
cp "$DIR/httpd_config.xml" /usr/local/lsws/conf/httpd_config.xml
cp "$DIR/htpasswd" /usr/local/lsws/admin/conf/htpasswd

chmod +x /usr/local/lsws/bin/setup_docker.sh
/usr/local/lsws/bin/setup_docker.sh

rm /usr/local/lsws/bin/setup_docker.sh
chown lsadm:lsadm /usr/local/lsws/conf -R
cp -RP /usr/local/lsws/conf/ /usr/local/lsws/.conf/
cp -RP /usr/local/lsws/admin/conf /usr/local/lsws/admin/.conf/


/bin/bash -c "if [[ $PHP_VERSION == lsphp8* ]]; then ln -sf /usr/local/lsws/$PHP_VERSION/bin/lsphp /usr/local/lsws/fcgi-bin/lsphp8; fi"
/bin/bash -c "if [[ $PHP_VERSION == lsphp8* ]]; then ln -sf /usr/local/lsws/fcgi-bin/lsphp8 /usr/local/lsws/fcgi-bin/lsphp; fi"
/bin/bash -c "if [[ $PHP_VERSION == lsphp7* ]]; then ln -sf /usr/local/lsws/$PHP_VERSION/bin/lsphp /usr/local/lsws/fcgi-bin/lsphp7; fi"
/bin/bash -c "if [[ $PHP_VERSION == lsphp7* ]]; then ln -sf /usr/local/lsws/fcgi-bin/lsphp7 /usr/local/lsws/fcgi-bin/lsphp; fi"
cp "$DIR/entrypoint.sh" /entrypoint.sh
chmod +x /entrypoint.sh

PASS_DIR="/usr/local/lsws/admin/misc"
ENCRYPT_PASS=`$PASS_DIR/../fcgi-bin/admin_php -q $PASS_DIR/htpasswd.php asdfgh`
echo "admin:$ENCRYPT_PASS" > $PASS_DIR/../conf/htpasswd


dnf -y module reset nodejs \
    && dnf -y module enable nodejs:18 \
    && dnf -y install nodejs

dnf install -y epel-release

dnf install -y libargon2 lsphp81-imap

dnf install -y lsphp81-bcmath \
    lsphp81-dba \
    lsphp81-enchant \
    lsphp81-gmp \
    lsphp81-odbc \
    lsphp81-posix \
    lsphp81-pspell \
    lsphp81-snmp \
    lsphp81-sqlite3 \
    lsphp81-sysvmsg \
    lsphp81-sysvsem \
    lsphp81-sysvshm \
    lsphp81-apcu \
    lsphp81-pecl-igbinary \
    lsphp81-msgpack \
    lsphp81-json \
    lsphp81-ldap \
    lsphp81-pgsql \
    lsphp81-soap \
    lsphp81-sodium \
    lsphp81-pdo_pgsql \
    lsphp81-xml \
    lsphp81-gd \
    lsphp81-pdo 

dnf install -y \
    lsphp81-devel \
    automake \
    autoconf \
    gcc \
    make \
    wget

wget https://xdebug.org/files/xdebug-3.2.2.tgz -O /xdebug-3.2.2.tgz \
    && mkdir /xdebug-3.2.2 \
    && tar -xvzf /xdebug-3.2.2.tgz -C /xdebug-3.2.2 \
    && cd /xdebug-3.2.2 \
    && /usr/local/lsws/lsphp81/bin/phpize \
    && ./configure --with-php-config=/usr/local/lsws/lsphp81/bin/php-config \
    && make \
    && cp modules/xdebug.so /usr/local/lsws/lsphp81/lib64/php/modules \
    && echo "zend_extension = xdebug" > /usr/local/lsws/lsphp81/etc/php.d/99-xdebug.ini \
    && echo "xdebug.mode = debug" >> /usr/local/lsws/lsphp81/etc/php.d/99-xdebug.ini \
    && echo "xdebug.start_with_request = yes" >> /usr/local/lsws/lsphp81/etc/php.d/99-xdebug.ini

curl -sS https://getcomposer.org/installer -o /composer-setup.php \
    && php /composer-setup.php --install-dir=/usr/local/bin --filename=composer \
    && rm /composer-setup.php \
    && composer self-update --2

touch "/INSTALL_DONE"
/entrypoint.sh

echo "openlitespeed admin password is now asdfgh"

