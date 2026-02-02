import subprocess

def git_push(msg="auto update by nika"):
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", msg])
    subprocess.run(["git", "push"])
