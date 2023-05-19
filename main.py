from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_indexhtml():
  return render_template('index.html')


@app.route('/send_data', methods=['POST'])
def get_data_from_html():
  yt = YouTube(request.form['pay'])
  ytob = yt.streams.get_by_itag(22).url
  return f"""
  <head>
    <title>Video</title>
  </head>
  <body>
    <center>
      <video width='100%' height='100%' controls> 
        <source src='{ytob}' type='video/mp4'>  
      </video>
    </center>
  </body>
  """


if __name__ == '__main__':
    app.run()
