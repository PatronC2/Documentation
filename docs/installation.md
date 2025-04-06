# Install

* Run `git clone https://github.com/PatronC2/Patron.git`
* Run `./install.sh -dps <your-ip>` for fresh install

```
Options:
  -d    Use default options
  -w    Wipe Database
  -s    <your_ip_address>   Server Ip address
  -b    Set up the discord bot
  -p    Prompts you to enter passwords
  -h    Show this help message
```

# Install in airgapped environment

* Set the git proxy
  * `git config --global http.proxy http://my-user:my-pass@proxy-ip:proxy-port`
  * `git config --global https.proxy http://my-user:my-pass@proxy-ip:proxy-port`
* Set git proxy certificate (if needed)
  * Get the proxy certificate, i.e. `wget --no-check-certificate -O /tmp/proxy-cert.pem https://proxy-ip/my-cert.pem`
  * `git config --global http.sslCAInfo /tmp/proxy-cert.pem`
* Clone the repository
  * `git clone https://github.com/PatronC2/Patron.git`
* Run the installer
  * No discord bot
    *  `./install.sh -dps <the-server-ipv4-address>`
  * With discord bot (see below)
    * `./install.sh -dpbs <the-server-ipv4-address>`
