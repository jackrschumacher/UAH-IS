**Part 1: File Analysis and Editing**

**Tasks:**

1.  **File Validation:**
    
    *   Prompt the user to input a file name and validate its existence.
        
    *   If the file exists, print: `"File Load Operation Successful"`
        
    *   If the file does not exist, exit with an error message.
        
2.  **Security String Search:**
    
    *   Search for the pattern `"administrator"` in the file:
        
        *   If found, print `"Match found: Please check all security logs"`
            
        *   If not found, print `"Match not found: Please proceed with system update"`
            
    *   Search for `"Logon ID"` and print all matching lines to the terminal.
        
3.  **Text Replacement:**
    
    *   Modify the file content as follows:
        
        *   Replace `"Account"` with `"Local"`
            
        *   Replace `"administrator"` with `"local_user"`
            
    *   Display all modified lines to the terminal.
        
4.  **Data Analysis:**
    
    *   Count and display the total occurrences of `"Security ID"`.
        
    *   Find all lines containing timestamps in the format `YYYY-MM-DD HH:MM:SS` and sort them chronologically.
        
5.  **(Optional) IP Address Extraction:**
    
    *   Extract all unique IP addresses (in the format `xxx.xxx.xxx.xxx`) from the file and save them to a new file called `"ip_addresses.txt"`.
        

**Part 2: System Log Analysis**

**Tasks:**

1.  **Log File Identification:**
    
    *   Locate a system log file (`/var/log/syslog`, `/var/log/messages`, `/var/log/kern.log`, or `/var/log/auth.log`).
        
    *   Use `find` to search for log files, e.g., `sudo find /var/log -name "*.log"`.
        
2.  **Security Vulnerability Check:**
    
    *   Search for `"Speculative Store Bypass"` in the selected log file:
        
        *   If `"Speculative Store Bypass is enabled"` is found, print `"This system is vulnerable to Speculative Store Bypass"`.
            
        *   If `"Speculative Store Bypass is disabled"` is found, print `"This system is not vulnerable to Speculative Store Bypass"`.
            
        *   If the pattern is not found, print `"Could not determine if this system is vulnerable to Speculative Store Bypass"`.
            
3.  **Authentication Failure Detection:**
    
    *   Search for `"authentication failure"` and `"failed login"` in the log file.
        
    *   If found, print the line along with its line number.
        
4.  **Log Severity Count:**
    
    *   Count the number of occurrences of `"error"`, `"warning"`, and `"info"` messages in the log file.
        
    *   Display the count of each type.
        
5.  **Summary Report Generation:**
    
    *   Generate a summary report containing:
        
        *   Total number of lines in the log file.
            
        *   The number of `"error"` messages.
            
        *   The number of `"warning"` messages.
            

**Part 3: Text Processing with Grep and Sed,**

**Tasks:**

1.  **Log File Analysis with Grep:**
    
    *   Search for all lines in the system log file that contain **either** `"error"` **or** `"critical"`.
        
    *   Save these lines to a new file named `"critical_errors.log"`.
        
2.  **Text Replacement with Sed:**
    
    *   Using `sed`, modify `"critical_errors.log"` to:
        
        *   Replace all instances of `"ERROR"` with `"error"`.
            
        *   Replace all instances of `"CRITICAL ALERT"` with `"critical"`.
            
    *   Save the modified output as `"formatted_critical_errors.log"`.
        
3.  **Pattern-Based Data Extraction:**
    
    *   Extract and display only the **timestamp** and **error message** from `"formatted_critical_errors.log"`.
        
    *   Assume timestamps follow the pattern `YYYY-MM-DD HH:MM:SS`.
        
4.  **Summarizing Log File Content:**
    

*   Count the number of unique **IP addresses** in `"formatted_critical_errors.log"`.
    
*   Extract all lines containing `"failed"` and display only the first **10 occurrences**.
    

_**Please submit three separate .sh files on on Canvas with the names:**_

1.  _**PC\_8\_Part\_1.sh**_
2.  _**PC\_8\_Part\_2.sh**_
3.  _**PC\_8\_Part\_3.sh**_