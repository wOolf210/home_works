import os
import subprocess
import sys

def create_venv():
    if not has_python():
        print("Python3 не найден. Пожалуйста, установите Python3.")
        sys.exit(1)

    subprocess.check_call([sys.executable, "-m", "venv", "venv"])
    activate_venv()

def has_python():
    return subprocess.call(["python3", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

def activate_venv():
    if sys.platform == "win32":
        activate_script = os.path.join("venv", "Scripts", "activate_this.py")
    else:
        activate_script = os.path.join("venv", "bin", "activate_this.py")

    with open(activate_script) as f:
        exec(f.read(), {'__file__': activate_script})

    install_dependencies()

def install_dependencies():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-docx"])

if __name__ == "__main__":
    create_venv()
    print("Виртуальное окружение создано и библиотека python-docx установлена.")
