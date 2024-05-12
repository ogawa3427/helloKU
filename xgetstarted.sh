pip install pyautogui

echo 'export DISPLAY=$(grep nameserver /etc/resolv.conf | awk '{print $2}'):0.0' >> ~/.bashrc
source ~/.bashrc

touch ~/.Xauthority
xauth generate $DISPLAY:0 . trusted

