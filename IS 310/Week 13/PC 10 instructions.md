Use **advanced Bash commands** and **Linux threat-hunting tools** to identify potentially malicious activity on a Linux system. You are encouraged to **use ChatGPT** to research each step and explain how you found your answers.

**Scenario**

A Linux server has been acting strangely. Your task is to **create a small Bash script** (`hunt_process.sh`) that finds **suspicious processes or files** using built-in Linux tools. You should **use ChatGPT** to help you research each part: _include your prompts and summaries in your submission_.

**Task 1: Research with ChatGPT**

Ask ChatGPT questions like:

_“What Bash command can I use to list all running processes with their network connections?”_  
_“How can I identify processes running from /tmp or hidden directories?”_

Then, in a short text file (`chatgpt_notes.txt`), record:

*   2–3 questions you asked
*   1–2 lines summarizing what you learned

**Task 2: Build the Script**

Create `hunt_process.sh` that performs **three checks**:

1.  **List all running processes with full command paths**  
    → use something like `ps aux` or `ps -eo pid,user,cmd`
2.  **Find processes executing from unusual locations**  
    → e.g., anything in `/tmp`, `/dev/shm`, or hidden folders (names starting with .)
3.  **List network connections and highlight suspicious ones**  
    → e.g., connections to external IPs (not localhost)  
    Hint: use `ss -tunp` or `netstat -tulpn`
4.  Output the results to a text file `suspect_report.txt` with a timestamp.

**Task 3: Run the script and Explain**

Run your script and include:

*   The **output** of your script (`output.txt`)
*   2–3 sentences explaining **what you found** and **how ChatGPT helped you** refine your commands.

**Deliverables to submit:**

1.  `hunt_process.sh` = your Bash script
2.  `output.txt` = example output from running the script
3.  `chatgpt_notes.txt` = your ChatGPT prompts + short summaries