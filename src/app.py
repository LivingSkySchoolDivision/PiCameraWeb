from flask import Flask, render_template, request

app = Flask(__name__)

# Video command is:
# raspivid -o - -t 0 -vf -hf -fps 30 -w 1280 -h 720 -b 2000000 | ffmpeg -f h264 -r 30 -i - -itsoffset 5.5 -fflags nobuffer -f alsa -ac 1 -i hw:1,0 -vcodec copy -acodec aac -ac 1 -ar 8000 -ab 32k -map 0:0 -map 1:0 -strict experimental -f flv  rtmp://a.rtmp.youtube.com/live2/<insert youtube live stream ID here>

@app.route("/", methods=['GET', 'POST'])
def home_page():
    print("HOME!")
    if request.form.get('triggered_action') == 'reboot':
        print("Reboot!")
    if request.form.get('triggered_action') == 'start_stream':
        print("start stream!")
    if request.form.get('triggered_action') == 'kill_stream':
        print("kill stream!")
    return render_template('default.html')