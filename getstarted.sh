# おやくそく
sudo apt update -y
sudo apt upgrade -y
sudo apt install portaudio19-dev -y
sudo apt install libfuse2 -y
sudo apt install libsndfile1 -y
sudo apt install p7zip -y
sudo apt install curl -y
sudo apt install libnss3 -y
sudo apt install libatk-bridge2.0-0 -y
sudo apt install libatk1.0-0 -y
sudo apt install libx11-xcb1 -y
sudo apt install libxcomposite1 -y
sudo apt install libxcursor1 -y
sudo apt install libxdamage1 -y
sudo apt install libxi6 -y
sudo apt install libxtst6 -y
sudo apt install libappindicator3-1 -y
sudo apt install libnss3 -y
sudo apt install libxss1 -y
sudo apt install libxrandr2 -y
sudo apt install libasound2 -y
sudo apt install libatk1.0-0 -y
sudo apt install libcups2 -y
sudo apt install libdbus-1-3 -y
sudo apt install libgdk-pixbuf2.0-0 -y
sudo apt install libglib2.0-0 -y
sudo apt install libgtk-3-0 -y
sudo apt install libgtk2.0-0 -y
sudo apt install libgtk-3-dev -y
sudo apt install libgtk2.0-dev -y
sudo apt install libpango-1.0-0 -y
sudo apt install libpangocairo-1.0-0 -y
sudo apt install libpangoft2-1.0-0 -y
sudo apt install libpangoxft-1.0-0 -y
sudo apt install libpango-1.0-dev -y
sudo apt install libpangocairo-1.0-dev -y
sudo apt install libpangoft2-1.0-dev -y
sudo apt install libpangoxft-1.0-dev -y

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
sudo echo

#pulseaudio
sudo apt install pulseaudio-utils -y
sudo apt install pulseaudio -y
echo >> ~/.bashrc
echo "export PULSE_SERVER=tcp:$(grep nameserver /etc/resolv.conf | awk '{print $2}');" >> ~/.bashrc
source ~/.bashrc

# ボイボ
curl -L https://github.com/VOICEVOX/voicevox/releases/download/0.19.1/voicevox-linux-cpu-0.19.1.tar.gz --progress-bar -o voicevox-linux-cpu-0.19.1.tar.gz
#tar -xvf voicevox-linux-cpu-0.19.1.tar.gz
