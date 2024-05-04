# おやくそく
sudo apt update -y
sudo apt upgrade -y

# Python構築
sudo apt install python3-pip -y #要確認
pip install --upgrade pip

pip install requests
pip install json
pip install pygame
pip install whisper-openai
pip install whisper-mic
pip install threading
pip install soundcard
pip install soundfile
pip install numpy

# ボイボ
curl https://github.com/VOICEVOX/voicevox/releases/download/0.19.1/voicevox-linux-cpu-0.19.1.tar.gz
tar -xvf voicevox-linux-cpu-0.19.1.tar.gz
