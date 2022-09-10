FROM debian:11-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y python3 python3-getdns python3-dnslib supervisor \
  && rm -rf /var/lib/apt/lists/*

COPY dns-proxy.py /usr/bin/dns-proxy
COPY dns-proxy-supervisor.conf /etc/supervisor/conf.d/dns-proxy-supervisor.conf

RUN chmod 755 /usr/bin/dns-proxy

EXPOSE 53

CMD ["/usr/bin/supervisord", "-n"]
