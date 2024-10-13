
#Install Ubuntu
apt-get update
apt-get upgrade -y
apt-get install wget -y
apt-get install proot -y
apt-get install git -y
git clone https://github.com/MFDGaming/ubuntu-in-termux.git
cd ubuntu-in-termux
chmod +x ubuntu.sh
./ubuntu.sh -y
./startubuntu.sh

# Installing Sudo & Other packages

apt-get update 
apt-get upgrade 
apt-get install sudo
sudo apt update
sudo apt install build-essential python3-dev libcairo2-dev libpango1.0-dev ffmpeg

# Install Latex(TeX) & Configuration

cd texlive2024
chmod +x install-tl
sudo ./install-tl
I # Press capital i For install Latex
sudo apt install nano # Code Editor Like VSCode, Pycharm.
nano ~/.bashrc
# add them in the last
export PATH=/usr/local/texlive/2024/bin/aarch64-linux:$PATH
export INFOPATH=/usr/local/texlive/2024/texmf-dist/doc/info:$INFOPATH
export MAINPATH=/usr/local/texlive/2024/texmf-dist/doc/man:$MAINPATH
source ~/.bashrc # activate Latex If you want to check whether latex has been successfully installed on your device then use these commands - latex -v , tex -v, pdflatex -v

# Install Python & pip
sudo apt update
sudo apt install python3-pip
sudo apt install python3.10-venv

# Install git & wget
sudo apt install git
sudo apt install wget

# Install ManimCommunity Edition
mkdir manimce
cd manimce
git clone https://github.com/ManimCommunity/manim.git
python3 -m venv venv
source venv/bin/activate
cd manim
pip install e .
deactivate

# Install ManimCairo Version
mkdir manimcairo
cd manimcairo
git clone -b cairo-backend --single-branch https://github.com/3b1b/manim.git
python3 -m venv venv
source venv/bin/activate
cd manimlib
python3 -m pip install -r requirements.txt
deactivate

# Install ManimGL 3b1b
git clone https://github.com/3b1b/manim.git
cd manim
python3 -m venv venv
source venv/bin/activate
python3 -m pip install e .

# Error Fíx In ManimGL 
sudo apt install xvfb
python3 -m pip install setuptools
pip install PyOpenGL==3.1.1a1

# Whenever you render a ManimGL scene, use this

xvfb-run manimgl example.py -o # o for output
   ^ # Xvfb or X virtual framebuffer is a display server implementing the X11 display server protocol. In contrast to other display servers, Xvfb performs all graphical operations in virtual memory without showing any screen output
