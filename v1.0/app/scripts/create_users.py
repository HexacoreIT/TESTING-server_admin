import subprocess

def crear_usuario(username, password):
    try:
        subprocess.run(['sudo', 'useradd', '-m', username], check=True)
        subprocess.run(['sudo', 'chpasswd'], input=f"{username}:{password}".encode(), check=True)
        return True
    except subprocess.CalledProcessError:
        return False
