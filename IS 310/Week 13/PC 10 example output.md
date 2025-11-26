```bash
Listing all running processes
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0  21784 12272 ?        Ss   16:04   0:00 /sbin/init
root           2  0.0  0.0   3072  1664 ?        Sl   16:04   0:00 /init
root           6  0.0  0.0   3072  1792 ?        Sl   16:04   0:00 plan9 --control-socket 7 --log-level 4 --server-fd 8 --pipe-fd 10 --log-truncate
root          39  0.0  0.0  50440 15104 ?        S<s  16:04   0:00 /usr/lib/systemd/systemd-journald
root          89  0.0  0.0  25008  6144 ?        Ss   16:04   0:00 /usr/lib/systemd/systemd-udevd
systemd+     104  0.0  0.0  21456 12672 ?        Ss   16:04   0:00 /usr/lib/systemd/systemd-resolved
systemd+     105  0.0  0.0  91024  7552 ?        Ssl  16:04   0:00 /usr/lib/systemd/systemd-timesyncd
root         173  0.0  0.0   4236  2560 ?        Ss   16:04   0:00 /usr/sbin/cron -f -P
message+     174  0.0  0.0   9552  4608 ?        Ss   16:04   0:00 @dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root         190  0.0  0.0  17964  8320 ?        Ss   16:04   0:00 /usr/lib/systemd/systemd-logind
syslog       207  0.0  0.0 222508  5504 ?        Ssl  16:04   0:00 /usr/sbin/rsyslogd -n -iNONE
root         213  0.0  0.0   3160  1920 hvc0     Ss+  16:04   0:00 /sbin/agetty -o -p -- \u --noclear --keep-baud - 115200,38400,9600 vt220
root         216  0.0  0.0   3116  1792 tty1     Ss+  16:04   0:00 /sbin/agetty -o -p -- \u --noclear - linux
root         222  0.0  0.1 107016 22016 ?        Ssl  16:04   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
root         315  0.0  0.0   3080   896 ?        Ss   16:04   0:00 /init
root         316  0.0  0.0   3096  1156 ?        S    16:04   0:00 /init
jackr        317  0.0  0.0   6204  5376 pts/0    Ss   16:04   0:00 -bash
root         318  0.0  0.0   6816  4480 pts/1    Ss   16:04   0:00 /bin/login -f
jackr        364  0.0  0.0  20312 11136 ?        Ss   16:04   0:00 /usr/lib/systemd/systemd --user
jackr        365  0.0  0.0  21152  3520 ?        S    16:04   0:00 (sd-pam)
jackr        389  0.0  0.0   6072  5120 pts/1    S+   16:04   0:00 -bash
root         708  0.0  0.0  25012  3300 ?        S    16:26   0:00 (udev-worker)
root         709  0.0  0.0  25012  3300 ?        S    16:26   0:00 (udev-worker)
root         710  0.0  0.0  25012  3300 ?        S    16:26   0:00 (udev-worker)
root         711  0.0  0.0  25012  3172 ?        S    16:26   0:00 (udev-worker)
jackr        712  0.0  0.0   4756  3200 pts/0    S+   16:26   0:00 /bin/bash ./Jack_Schumacher_PC10.sh
jackr        713  0.0  0.0   8284  4096 pts/0    R+   16:26   0:00 ps auxww
Finding all proccesses that are executing from unusual locations
[sudo] password for jackr: 
ls: cannot access '/proc/708/exe': No such file or directory
ls: cannot access '/proc/709/exe': No such file or directory
ls: cannot access '/proc/710/exe': No such file or directory
ls: cannot access '/proc/711/exe': No such file or directory
lrwxrwxrwx 1 root             root             0 Nov 26 16:04 /proc/1/exe -> /usr/lib/systemd/systemd
lrwxrwxrwx 1 systemd-resolve  systemd-resolve  0 Nov 26 16:04 /proc/104/exe -> /usr/lib/systemd/systemd-resolved
lrwxrwxrwx 1 systemd-timesync systemd-timesync 0 Nov 26 16:04 /proc/105/exe -> /usr/lib/systemd/systemd-timesyncd
lrwxrwxrwx 1 root             root             0 Nov 26 16:04 /proc/173/exe -> /usr/sbin/cron
lrwxrwxrwx 1 root             root             0 Nov 26 16:04 /proc/174/exe -> /usr/bin/dbus-daemon
lrwxrwxrwx 1 root             root             0 Nov 26 16:04 /proc/190/exe -> /usr/lib/systemd/systemd-logind
lrwxrwxrwx 1 root             root             0 Nov 26 16:04 /proc/2/exe -> /init
lrwxrwxrwx 1 root             root             0 Nov 26 16:04 /proc/207/exe -> /usr/sbin/rsyslogd
lrwxrwxrwx 1 root             root             0 Nov 26 16:04 /proc/213/exe -> /usr/sbin/agetty
lrwxrwxrwx 1 root             root             0 Nov 26 16:04 /proc/216/exe -> /usr/sbin/agetty
lrwxrwxrwx 1 root             root             0 Nov 26 16:04 /proc/222/exe -> /usr/bin/python3.12
lrwxrwxrwx 1 root             root             0 Nov 26 16:04 /proc/315/exe -> /init
lrwxrwxrwx 1 root             root             0 Nov 26 16:04 /proc/316/exe -> /init
lrwxrwxrwx 1 jackr            jackr            0 Nov 26 16:04 /proc/317/exe -> /usr/bin/bash
lrwxrwxrwx 1 root             root             0 Nov 26 16:04 /proc/318/exe -> /usr/bin/login
lrwxrwxrwx 1 jackr            jackr            0 Nov 26 16:04 /proc/364/exe -> /usr/lib/systemd/systemd
lrwxrwxrwx 1 root             root             0 Nov 26 16:04 /proc/365/exe -> /usr/lib/systemd/systemd-executor
lrwxrwxrwx 1 jackr            jackr            0 Nov 26 16:04 /proc/389/exe -> /usr/bin/bash
lrwxrwxrwx 1 root             root             0 Nov 26 16:04 /proc/39/exe -> /usr/lib/systemd/systemd-journald
lrwxrwxrwx 1 root             root             0 Nov 26 16:04 /proc/6/exe -> /init
lrwxrwxrwx 1 jackr            jackr            0 Nov 26 16:26 /proc/712/exe -> /usr/bin/bash
lrwxrwxrwx 1 root             root             0 Nov 26 16:26 /proc/714/exe -> /usr/bin/sudo
lrwxrwxrwx 1 jackr            jackr            0 Nov 26 16:26 /proc/715/exe -> /usr/bin/grep
lrwxrwxrwx 1 root             root             0 Nov 26 16:04 /proc/89/exe -> /usr/bin/udevadm
lrwxrwxrwx 1 root             root             0 Nov 26 16:26 /proc/self/exe -> /usr/bin/ls
lrwxrwxrwx 1 root             root             0 Nov 26 16:26 /proc/thread-self/exe -> /usr/bin/ls
Listing external connections and highlighting them
Netid Recv-Q Send-Q Local Address:Port Peer Address:PortProcess
```

