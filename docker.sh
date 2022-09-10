#!/bin/bash

docker stop dns-proxy

docker build -t dns-proxy .

docker run -d --rm	-p 533:53 --name dns-proxy dns-proxy
