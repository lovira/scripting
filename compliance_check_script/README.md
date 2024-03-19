<h1> Simple macOS Compliance Checker </h1>
<h2> Overview </h2>
The macOS Security Compliance Checker is a Python script designed to automate the evaluation of security compliance on macOS machines. Specifically, it checks if the firewall is activated and if FileVault encryption is enabled. This tool aims to streamline the compliance audit process, ensuring that macOS systems adhere to stringent security standards and best practices, thus mitigating the risk of cyber threats.
<br>
<br>

<h2> Features </h2>
Firewall Check: Verifies if the macOS firewall is active.
<br>
FileVault Encryption Check: Determines whether FileVault encryption is enabled, securing the machine's data.

<br>

<h2>Prerequisites</h2>
Before running this script, ensure you have the following:

- macOS operating system (version 10.15 or later recommended).
- Python 3.6 or higher installed.

<h2> Installation </h2>
Clone the repository or download the script to your local machine.
<br>
<br>
<code> git clone https://example.com/macos_security_compliance_checker.git
</code>
<br>
<br>
Navigate to the script's directory.
<code> 
cd macos_security_compliance_checker
</code>

Usage
To run the script, execute the following command in the terminal:

<code>
python3 security_compliance_checker.py
</code>

<h2>Output</h2>
The script outputs:

- Firewall Status: Enabled/Disabled
- FileVault Status: Enabled/Disabled



<h2> Dependencies </h2>

- os: For executing system-level commands in macOS.
- subprocess: For invoking commands that check the firewall and FileVault statuses.