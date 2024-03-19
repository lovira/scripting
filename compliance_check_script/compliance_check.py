import subprocess

def check_filevault_status():
    try:
        result = subprocess.run(['fdesetup', 'status'], capture_output=True, text=True)
        if "FileVault is On" in result.stdout:
            print("FileVault Check: PASSED - FileVault is enabled.")
        else:
            print("FileVault Check: FAILED - FileVault is not enabled.")
    except Exception as e:
        print(f"An error occurred: {e}")

def check_firewall_status():
    try:
        result = subprocess.run(['sudo', '/usr/libexec/ApplicationFirewall/socketfilterfw', '--getglobalstate'], capture_output=True,text=True)
        if "Firewall is On" in result.stdout:
            print("Firewall Check: PASSED - Firewall is enabled.")
        else:
            print("Firewall Check: FAILED - Firewall is not enabled.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    check_firewall_status()
    check_filevault_status()
    
