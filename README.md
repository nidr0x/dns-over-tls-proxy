### DNS to DNS-over-TLS proxy

### Testing

Run the docker script:

`./docker.sh`

Test it by running:

`dig google.com -t A @127.0.0.1 -p 533 +tcp`

I'm using 533 port instead of 53 port to avoid conflicts with `mDnsResponder` under macOS.
