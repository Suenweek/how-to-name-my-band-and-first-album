from flask import render_template
from app import app, bl


@app.route('/')
def index():
    return render_template(
        'index.html',
        band_name=bl.get_random_band_name(),
        first_album_name=bl.get_random_first_album_name()
    )
