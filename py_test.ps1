if (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole("Administrators")) { Start-Process powershell.exe "-File `"$PSCommandPath`"" -Verb RunAs; exit }

# Chocolateyをインストール
Set-ExecutionPolicy Bypass -Scope Process -Force;
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;
Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# インストールが完了したら、PythonとGitをインストール
choco install python3 -y
choco install git -y

# Gitリポジトリをクローン
git clone https://github.com/ogawa3427/helloKU

# pipをアップグレード
python -m pip install --upgrade pip

# 必要なPythonパッケージをインストール
pip install openai
pip install json
pip install whisper-openai
pip install whisper-mic
pip install threading
pip install requests
pip install soundcard
pip install soundfile
pip install SpeechRecognition