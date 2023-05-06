from flask import Flask, render_template

app = Flask(__name__)

# Video command is:
# raspivid -o - -t 0 -vf -hf -fps 30 -w 1280 -h 720 -b 2000000 | ffmpeg -f h264 -r 30 -i - -itsoffset 5.5 -fflags nobuffer -f alsa -ac 1 -i hw:1,0 -vcodec copy -acodec aac -ac 1 -ar 8000 -ab 32k -map 0:0 -map 1:0 -strict experimental -f flv  rtmp://a.rtmp.youtube.com/live2/<insert youtube live stream ID here>

@app.route("/")
def home_page():
    return render_template('default.html')