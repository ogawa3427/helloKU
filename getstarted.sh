# おやくそく
sudo apt update -y
sudo apt upgrade -y
sudo apt install portaudio19-dev -y

# Python構築
sudo apt install python3-pip -y #要確認
pip install --upgrade pip
pip install -r requirements.txt
pip install json
pip install whisper-openai
pip install whisper-mic
pip install threading
pip install Requests
pip install soundcard
pip install soundfile
pip install SpeechRecognition

#pulseaudio
sudo apt install pulseaudio-utils
echo >> ~/.bashrc
echo "export __BASEIP=192" >> ~/.bashrc
echo "export __XSERVERHOST=NANOKO" >> ~/.bashrc
echo "export PULSE_SERVER=tcp:$(nslookup $__XSERVERHOST | grep " $__BASEIP" | awk '{print $2}');" >> ~/.bashrc
source ~/.bashrc

# ボイボ
#curl https://github.com/VOICEVOX/voicevox/releases/download/0.19.1/voicevox-linux-cpu-0.19.1.tar.gz
#tar -xvf voicevox-linux-cpu-0.19.1.tar.gz
