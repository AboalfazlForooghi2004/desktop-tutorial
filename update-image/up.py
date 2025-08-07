import pexpect
import getpass
import sys
import io

# -------- Get user input --------
console_ip = "192.168.30.20"
console_pass = "123"
switch_user = "admin"
switch_pass = "zharfpouyan"
webserver_ip = "192.168.0.19"
default_gw = "192.168.30.2"

console_user = input(" Console server username: ")
image_file = input(" Image filename : ")
mgmt_ip = input(" Management IP with subnet (e.g. 192.168.30.34/24): ")

print("\n🔌 Connecting to console server...\n")
child = pexpect.spawn(f"ssh {console_user}@{console_ip}", timeout=30)

child.expect("password:")
child.sendline(console_pass)

# Select serial port (default: 1)
child.expect(r"#\?")
child.sendline("1")

# Send ENTERs to trigger login prompt
child.sendline("")
child.sendline("")
child.sendline("")

# Try to detect switch state
index = child.expect([
    "login:",
    "Password:",
    "#",  # already in CLI
], timeout=10)

if index == 0:
    child.sendline(switch_user)
    child.expect("Password:")
    child.sendline(switch_pass)
elif index == 1:
    child.sendline(switch_pass)
else:
    print("✅ Already inside switch CLI.")

# Enter enable and config mode
child.expect(".*#")
child.sendline("enable")
child.expect(".*#")
child.sendline("configure terminal")
child.expect(".*\\(config\\)#")

# Build and send update command
update_cmd = f"update image http {webserver_ip} {image_file} {mgmt_ip} {default_gw}"
print(f"\n🚀 Sending update command: {update_cmd}\n")
child.sendline(update_cmd)

# Confirm update
child.expect("Are you sure to update device\\?\\(yes/no\\)")
child.sendline("yes")

# Respond to config/restore question
child.expect("Would you like to restore config and storage after update image\\?\\(yes/no\\)")
child.sendline("no")

# ✅ Now start showing CLI output live
print("\n⏳ Updating... Please wait.\n")
child.logfile = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# Wait for update to complete
index = child.expect([
    "Update completed",
    pexpect.TIMEOUT,
    pexpect.EOF
], timeout=600)

if index == 0:
    print("\n✅ Update completed successfully.")
else:
    print("\n❌ Error or timeout during update.")

child.close()
