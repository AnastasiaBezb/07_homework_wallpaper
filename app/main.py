import os

import waitress

from flask import Flask, render_template, request

from app.lib import number_of_rolls


def start():
    app = Flask(__name__)

    @app.route('/')  # правило сопоставления запроса URL  фун-ии обработчика
    def frontpage():
        width = request.args.get('width')
        length = request.args.get('length')
        height = request.args.get('height')
        wallpaper_width = request.args.get('wallpaper_width')
        wallpaper_length = request.args.get('wallpaper_length')

        print(type(width))
        if width and length and height and wallpaper_width and wallpaper_length:
            total_number_of_rolls = number_of_rolls(float(width), float(length), float(height),
                                                    float(wallpaper_width), float(wallpaper_length))
            level = 'primary'
            return render_template('index.html', title='Wallpaper calculator',
                                   total_number_of_rolls=total_number_of_rolls,
                                   width=width, length=length, height=height, wallpaper_width=wallpaper_width,
                                   wallpaper_length=wallpaper_length,
                                   level=level
                                   )

        return render_template('index.html', title='Wallpaper calculator')

    print(os.getenv('APP_ENV'))
    print(os.getenv('PORT'))
    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9876, debug=True)


if __name__ == '__main__':
    start()
