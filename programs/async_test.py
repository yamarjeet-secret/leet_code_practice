import subprocess
import paramiko

def ssh_connect(username,passowrd,ip):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"Connecting to {ip}...")
    ssh.connect(hostname=ip,username=username,password=passowrd,timeout=10)
    command = "uname -a"
    print(f"Connected to {ip}. Executing command: {command}")
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode().strip()
    error = stderr.read().decode().strip()
    ssh.close()


    
try:
    ans = subprocess.check_output(["uname", "-r"], text=True)
    print(ans)

except subprocess.CalledProcessError as e:
    print(f"Command failed with return code {e.returncode}")


lsProcess = subprocess.Popen(["ls"], stdout=subprocess.PIPE, text=True)
grepProcess = subprocess.Popen(
    ["grep", "flask"], stdin=lsProcess.stdout,
    stdout=subprocess.PIPE, text=True)
output, error = grepProcess.communicate()

print(output)
print(error)