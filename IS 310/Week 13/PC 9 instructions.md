**Part 1: System Hardening**

**Tasks**

1.  **Disable Unnecessary Services**

1.  *   Write command(s) to disable `telnet`, `ftp`, and `rsh` services.
        
    *   Ensure it checks if the service exists before disabling it.
        
2.  **Configure Firewall Rules**
    
    *   Write command(s) that:
        
        *   _Blocks all incoming traffic by default._
            
        *   _Allows `SSH` (port 22)._
            
        *   _Allows `HTTP` (port 80)._
            
        *   _Enables the `firewall`._
            
3.  **Secure User Accounts** 
    *   Write command(s) to:
        *   Expire the `root` password.
            
        *   Lock the `guest` account (if it exists).
            
        *   Ensure all users have a password (no empty entries in `/etc/shadow`).
            
4.  **Automate Updates**
    *   Write command(s) to:
        *   update the linux distribution
            
        *   upgrade all packages
            
        *   remove unused packages
            

**Part 2: Security Auditing**

**Tasks**

1.  **Audit User Accounts**
    *   Write command(s) to:
        
        *   List all users with empty passwords.
            
        *   Identify accounts with superuser access (besides root).
            
        *   Save results to `user_audit.txt`.
            
2.  **Check File Permissions**
    *   Write command(s) to:
        
        *   Find all world-writable files.
            
        *   List files with SUID/SGID permissions.
            
        *   Save results to `file_audit.txt`.
            
3.  **Network Configuration Audit**
    *   Write command(s) to:
        
        *   List all open ports using `netstat`.
            
        *   Check if IP forwarding is enabled.
            
        *   Save results to `network_audit.txt`.
            
4.  **Log Analysis**

1.  *   Write command(s) that:
        
        *   Searches `/var/log/auth.log` for "failed password" entries.
            
        *   Counts the number of failed login attempts.
            
        *   Saves the count to `failed_logins.txt`.
            

_**Please submit two separate .sh files on on Canvas with the names:**_

1.  _**PC\_9\_Part\_1.sh**_
2.  _**PC\_9\_Part\_2.sh**_