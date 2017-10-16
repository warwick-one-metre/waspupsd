## GOTO UPS monitoring daemon [![Travis CI build status](https://travis-ci.org/warwick-one-metre/gotoupsd.svg?branch=master)](https://travis-ci.org/warwick-one-metre/gotoupsd)

Part of the observatory software for the Warwick La Palma telescopes.

`gotoupsd` is a Pyro frontend for monitoring the GOTO UPSes via SNMP.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the W1m software architecture and instructions for developing and deploying the code.

### Software Setup

After installing `goto-ups-monitor-server`, the `gotoupsd` must be enabled using:
```
sudo systemctl enable gotoupsd.service
```

The service will automatically start on system boot, or you can start it immediately using:
```
sudo systemctl start gotoupsd.service
```
