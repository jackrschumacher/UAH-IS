# Programming Challenge 10 Notes

For this project, I am using Gemini instead of ChatGPT. I used the "thinking mode" in order to provide more complete and complex answers

## Research notes

### Questions

> "How can I list all running processes with command paths?"
>
> "How can i find command processes that might be in non-standard locations"
>
> "How can I list network connections and highlight any connections to external IP addresses"

### Responses

**"How can I list all running processes with command paths?"**

> To list all running processes with their **full command paths** (and arguments), the standard tool is `ps`.
>
> Here are the most effective ways to do this, ranging from listing everything to finding specific processes.
>
> 
>
> ### 1. The Best All-Around Command: `ps`
>
> 
>
> By default, `ps` truncates output to fit your screen width. To see the full, unlimited command path, you must add the `ww` (wide, wide) flags.
>
> **Command:**
>
> Bash
>
> ```bash
> ps auxww
> ```
>
> **Explanation of flags:**
>
> - `a`: All users' processes (not just yours).1
>
>   
>
>   
>
> - `u`: Display user-oriented format (shows owner, CPU, RAM).
>
> - `x`: Include processes not attached to a terminal (background daemons).2
>
>   
>
>   
>
> - `ww`: **Crucial flag.** It sets "unlimited width" so the command path isn't cut off.
>
> Clean Output (Command Only):
>
> If you only want the full command path without the PID, CPU usage, etc., use this formatting option:
>
> Bash
>
> ```bash
> ps -A -o cmd
> ```
>
> ------
>
> 
>
> ### 2. Searching for a Specific Process: `pgrep`
>
> 
>
> If you are looking for a specific process and want to see its full path, `pgrep` is often faster than piping `ps` into `grep`.
>
> **Command:**
>
> Bash
>
> ```bash
> pgrep -a "process_name"
> ```
>
> - `-a`: Lists the full command line as well as the process ID.
> - `-f`: Matches the pattern against the full command line (useful if you are searching for a specific path argument).
>
> ------
>
> 
>
> ### 3. Interactive Viewers: `top` and `htop`
>
> 
>
> If you are monitoring the system and want to see full paths in real-time:
>
> - In top:
>
>   Press the c key while top is running.3 This toggles between the process name (e.g., python) and the full command line (e.g., /usr/bin/python3 /home/user/script.py).
>
> - **In `htop`:**
>
>   - `htop` usually shows the full path by default, but you can scroll horizontally using the **Arrow Keys** to read long paths.
>   - If it is hidden, press **`p`** to toggle the full path display.
>
> ------
>
> 
>
> ### 4. The "Raw" Data (For Scripts): `/proc`
>
> 
>
> Linux stores process information in the `/proc` directory.4 If you need the exact, unmodified command that started a specific PID (Process ID), you can read it directly.
>
> 
>
> Bash
>
> ```bash
> # Replace 1234 with the actual PID
> cat /proc/1234/cmdline
> ```
>
> *Note: This output is null-separated (not space-separated), so it may look like one long string or have no spaces depending on your terminal. You can clean it up like this:*
>
> Bash
>
> ```bash
> cat /proc/1234/cmdline | tr '\0' ' '
> ```
>
> 
>
> ### Summary Table
>
> 
>
> | **Goal**                        | **Command**       |
> | ------------------------------- | ----------------- |
> | **List everything**             | `ps auxww`        |
> | **List everything (Tree view)** | `pstree -a`       |
> | **Find specific process**       | `pgrep -a "name"` |
> | **Interactive monitor**         | `top` (press `c`) |

**"How can i find command processes that might be in non-standard locations"**

> Executing processes from "non-standard" locations (directories that are world-writable like `/tmp` or `/dev/shm`) is a classic indicator of malware, unauthorized scripts, or compromised user accounts.
>
> Legitimate Linux binaries typically live in root-owned directories like `/bin`, `/usr/bin`, or `/sbin`.
>
> Here are the most effective ways to hunt for these processes.
>
> 
>
> ### 1. The Most Reliable Method: Querying `/proc`
>
> 
>
> This is the "forensic" approach. The `ps` command can sometimes be spoofed by malware, but the kernel's record in `/proc` is much harder to fake. We will look for symbolic links pointing to executables in suspicious directories.
>
> Run this command to scan for processes running from `/tmp`, `/dev/shm`, or hidden folders in home directories:
>
> Bash
>
> ```bash
> sudo ls -l /proc/*/exe 2>/dev/null | grep -E '/tmp|/dev/shm|/var/tmp|/home/.*/\.'
> ```
>
> **Breakdown:**
>
> - `ls -l /proc/*/exe`: Lists the actual executable path for every running process ID.
>
> - `2>/dev/null`: Hides "Permission denied" errors (for processes you can't see).
>
> - `grep -E`: Filters for the suspicious paths.
>
>   - `/tmp`: Common drop point for scripts.1
>
>     
>
>     
>
>   - `/dev/shm`: (Shared Memory) A favorite spot for malware because it runs purely in RAM and leaves no trace on the hard drive after a reboot.
>
>   - `/home/.*/\.`: Looks for executables running from hidden directories inside a user's home folder (e.g., `/home/user/.cache/miner`).
>
> ------
>
> 
>
> ### 2. Using `lsof` (List Open Files)2
>
> 
>
> If you have `lsof` installed, it is excellent for this because it can recursively check a directory for *any* open file (executable, library, or log) being held by a process.
>
> **To check specific risky directories:**
>
> Bash
>
> ```bash
> sudo lsof +D /tmp
> sudo lsof +D /dev/shm
> sudo lsof +D /var/tmp
> ```
>
> - `+D`: Tells `lsof` to search the directory recursively.
>
> ------
>
> 
>
> ### 3. The "Quick Check" with `ps`
>
> 
>
> If you want a quick visual scan using standard tools, you can list processes and filter for these paths. Note that sophisticated malware can sometimes change the name shown here, making method #1 more reliable.
>
> Bash
>
> ```bash
> ps auxww | grep -E '/tmp|/dev/shm|/var/tmp'
> ```
>
> 
>
> ### Suspicious vs. Benign Examples
>
> 
>
> | **Location**   | **Suspicious Example**       | **Likely Benign Example**                   |
> | -------------- | ---------------------------- | ------------------------------------------- |
> | **`/tmp`**     | `/tmp/x86_64_miner`          | `/tmp/go-build...` (if you are a developer) |
> | **`/dev/shm`** | `/dev/shm/.hidden_script`    | `/dev/shm/pulse...` (PulseAudio)            |
> | **`/var/tmp`** | `/var/tmp/reverse_shell`     | System logs or cache files                  |
> | **`/home`**    | `/home/user/.config/sus_bin` | `/home/user/bin/my_script.sh`               |
>
> Next Step:
>
> If you find a PID (Process ID) that looks malicious (e.g., PID 1234), do not kill it immediately if you need to investigate. Instead, pause it to stop the damage while you inspect it:
>
> Bash
>
> ```bash
> kill -STOP 1234
> ```
>
> Then you can check where it came from using `ls -l /proc/1234/cwd`.

**"How can I list network connections and highlight any connections to external IP addresses"**

> To list network connections and identify those communicating with external (non-local) IP addresses, you can use the `ss` command (the modern replacement for `netstat`) combined with `grep` to filter out your local private networks.
>
> 
>
> ### 1. The "Highlight" Command (Show Only External Connections)
>
> 
>
> This command lists all established connections but **hides** purely local traffic (localhost, 192.168.x.x, 10.x.x.x, etc.). What remains are connections to the outside world.
>
> Bash
>
> ```bash
> ss -tun state established | grep -vE "127\.|192\.168\.|10\.|172\.(1[6-9]|2[0-9]|3[0-1])\."
> ```
>
> **Breakdown:**
>
> - `ss`: Socket Statistics command.
> - `-tun`: **T**CP and **U**DP protocols, **N**umeric IPs (no hostname resolution, which is faster).
> - `state established`: Only show active, connected sessions (ignores listening ports).
> - `grep -vE "..."`: **V**erse match (exclude) the pattern. The pattern matches standard private IP ranges (Loopback, Class A, B, and C private networks).
>
> ------
>
> 
>
> ### 2. The "Full List" Command (All Details)
>
> 
>
> If you want to see *everything* (local and external) along with the **process name** responsible for the connection, use this:
>
> Bash
>
> ```bash
> sudo ss -tunap
> ```
>
> - `-a`: All (listening and established).
> - `-p`: Show the **P**rocess ID and name (requires `sudo`).
>
> **Tip:** If you want to highlight the external IPs visually in this full list (instead of hiding the others), you can use `grep` to color the output while still printing everything:
>
> Bash
>
> ```bash
> # This prints all lines but colors external IPs in red
> sudo ss -tunap | grep --color=always -E "^|[^0-9]([1-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]{1,3}\.){2}[0-9]{1,3}"
> ```
>
> *(Note: This uses a regex to match generic public IP patterns. It may occasionally color local IPs if they don't match strict private ranges, but it is effective for a quick visual scan.)*
>
> ------
>
> 
>
> ### 3. Real-Time Monitoring
>
> 
>
> To watch your external connections in real-time (updating every 2 seconds), combine the first command with `watch`:
>
> Bash
>
> ```bash
> watch -n 2 'ss -tun state established | grep -vE "127\.|192\.168\.|10\.|172\.(1[6-9]|2[0-9]|3[0-1])\."'
> ```
>
> 
>
> ### Summary of Flags
>
> 
>
> | **Flag** | **Meaning**                                                  |
> | -------- | ------------------------------------------------------------ |
> | `-t`     | Show TCP connections (Web, SSH, etc.)                        |
> | `-u`     | Show UDP connections (DNS, Streaming)                        |
> | `-n`     | **Numeric** (Show IPs like `8.8.8.8` instead of `dns.google`) |
> | `-p`     | **Process** (Show which program opened the connection)       |
> | `-a`     | **All** (Show listening ports too, not just active connections) |
>
> **Next Step:** Would you like a script that automatically checks the geolocation of these external IPs to tell you which country they are connected to?
>
> [Linux netstat Command Explained](https://www.youtube.com/watch?v=nlULYj6S8Ws)
>
> This video explains the columns and output of `netstat` (the predecessor to `ss`), which is helpful for understanding what "State," "Recv-Q," and "Foreign Address" mean when analyzing your network traffic.

### What I learned

Using Gemini allowed me to understand more about the commands and the options that i can use in order to adapt them more to my specific script. Linux documentation is typically more sparse and might not explain the options very completely as well as their limitations, where as with Gemini it does. For example it helped me to learn more about using regex matching in order to filter IP addresses as well as files.



# How Gemini helped me refined my commands

Gemini allowed me to understand the commands that I was using and how different options affect the ways in which commands run and what responses the return. I could also see using Gemini would be helpful to maybe point me in the right direction when I encounter a problem in the code that i can not figure out with my own debuggi