# おやくそく
sudo apt update -y
sudo apt upgrade -y
sudo apt install portaudio19-dev -y

# Python構築
sudo apt install python3-pip -y #要確認
pip install --upgrade pip
sudo echo
pip install -r requirements.txt
sudo echo
pip install json
pip install whisper-openai
sudo echo
pip install whisper-mic
sudo echo
pip install threading
pip install Requests
sudo echo
pip install soundcard
pip install soundfile
sudo echo
pip install SpeechRecognition

#pulseaudio
sudo apt install pulseaudio-utils -y
sudo apt install pulseaudio -y
echo >> ~/.bashrc
echo "export PULSE_SERVER=tcp:$(grep nameserver /etc/resolv.conf | awk '{print $2}');" >> ~/.bashrc
source ~/.bashrc

# ボイボ
curl -L https://github.com/VOICEVOX/voicevox/releases/download/0.19.1/voicevox-linux-cpu-0.19.1.tar.gz --progress-bar -o voicevox-linux-cpu-0.19.1.tar.gz
#tar -xvf voicevox-linux-cpu-0.19.1.tar.gz
