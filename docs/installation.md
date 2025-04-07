# Install

## Infrastructure
* It is recommended to use at least 2 Ubuntu 22/24 servers for a Patron installation
* The first server is for the teamserver / core functionalities
* The second server is for a redirector. The purpose is to:
    1. Enable IPv6 agents.
    2. Avoid callbacks directly to the teamserver.
    3. Allow caching of agents when the teamserver is being updated.

## Normal Install with internet access
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

## Install in airgapped environment

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

## Creating Discord bot
* Go to discord dev portal
* create new application (not actual bot)
* go to bot tab
* add bot (username , icon, uncheck public bot, check message content intent)
* Set Installation Contexts to User Install and Guild Install
* grab token (reset token, save for later)
* generate url to add to server, with permissions like `https://discord.com/oauth2/authorize?client_id=<your-client-id>&permissions=8&scope=bot+applications.commands&permissions=139586766912`
* go to oauth2 -> url generator (check bot)
* check (read messages/view Channels, send messages, embed links, send messages in thread)
* copy and open url in new tab
* add bot to each server
