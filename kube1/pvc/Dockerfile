FROM nginx:1.12
RUN set -ex && \
    apt-get update && \
    apt-get update install -y procps && \
    apt-get clean

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]