# from flaskwebgui import FlaskUI
from flask import Flask, request, url_for,render_template,redirect,flash
import pytube
app = Flask(__name__,template_folder="templates")
app.secret_key = 'secreto'
#---------------------------------------------------------------------
@app.route('/')
def Main ():
    return render_template('index.html')
#---------------------------------------------------------------------
@app.route('/add', methods = ['POST'])
def Gestion():
    try:
        if request.method == 'POST':
            #-------------------------------------
            link = request.form['link']
            op1 = request.form['opciones']
            youtube = pytube.YouTube(link)
            if op1 == '140':
                audio = youtube.streams.get_by_itag(op1).download('Audios')
                flash("Audio Descargado")
            if op1 == '18' or '22' or '137':
                video = youtube.streams.get_by_itag(op1).download('Videos')
                flash("Video Descargado")
            return redirect(url_for('Main'))
    except:
        print(f'Video {link} is unavaialable, skipping.')
#---------------------------------------------------------------------

#---------------------------------------------------------------------

#---------------------------------------------------------------------

#---------------------------------------------------------------------
if __name__=='__main__':
    app.run(port=5000,debug=True)
    # gui = FlaskUI(app,port=5000)
    # gui.run()
