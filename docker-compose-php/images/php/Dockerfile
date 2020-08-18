# Для начала указываем исходный образ, он будет использован как основа
FROM php:7.4-fpm
# Необязательная строка с указанием автора образа
MAINTAINER PHPtoday.ru <info@phptoday.ru>

# RUN выполняет идущую за ней команду в контексте нашего образа.
# В данном случае мы установим некоторые зависимости и модули PHP.
# Для установки модулей используем команду docker-php-ext-install.
# На каждый RUN создается новый слой в образе, поэтому рекомендуется объединять команды.
RUN apt-get update && apt-get install -y \
        curl \
        wget \
        git \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
        libonig-dev \
    && apt-get clean

RUN docker-php-ext-install -j$(nproc) iconv mbstring mysqli pdo_mysql \
    && docker-php-ext-install -j$(nproc) gd
    
# Куда же без composer'а.
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Добавим свой php.ini, можем в нем определять свои значения конфига
ADD php.ini /usr/local/etc/php/conf.d/40-custom.ini
ADD php-fpm.conf /usr/local/etc/php-fpm.d/zz-docker.conf

# Указываем рабочую директорию для PHP
WORKDIR /var/www

# Запускаем контейнер
# Из документации: The main purpose of a CMD is to provide defaults for an executing container. These defaults can include an executable, 
# or they can omit the executable, in which case you must specify an ENTRYPOINT instruction as well.
#EXPOSE 80
CMD ["php-fpm"]
