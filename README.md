## SuperWASP UPS monitoring daemon [![Travis CI build status](https://travis-ci.org/warwick-one-metre/waspupsd.svg?branch=master)](https://travis-ci.org/warwick-one-metre/waspupsd)

Part of the observatory software for the Warwick La Palma telescopes.

`waspupsd` is a Pyro frontend for monitoring the SuperWASP UPSes via SNMP.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the W1m software architecture and instructions for developing and deploying the code.

### Software Setup

After installing `wasp-ups-server`, the `waspupsd` must be enabled using:
```
sudo systemctl enable waspupsd.service
```

The service will automatically start on system boot, or you can start it immediately using:
```
sudo systemctl start waspupsd.service
```

If needed, open a port in the firewall so that other machines on the network can access the daemon:
```
sudo firewall-cmd --zone=public --add-port=9027/tcp --permanent
sudo firewall-cmd --reload
```
