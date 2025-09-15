import subprocess

def set_permisos(user, path, permisos):
    try:
        subprocess.run(['sudo', 'chown', f"{user}:{user}", path], check=True)
        subprocess.run(['sudo', 'chmod', permisos, path], check=True)
        return True
    except subprocess.CalledProcessError:
        return False
