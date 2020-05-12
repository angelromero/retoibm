# app.py

from flask import jsonify
from flask import Flask
from flask import request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from config import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)


from models import *


@app.route('/api/sumar/<int:sumando01>/<int:sumando02>', methods=['GET'])
def do_sum(sumando01,sumando02):
    if request.method == 'GET':
        sumando01 = sumando01
        sumando02 = sumando02

        post = Post(sumando01,sumando02,sumando01+sumando02)
        db.session.add(post)
        db.session.commit()
        posts = Post.query.all()
    return jsonify(json_list=[{
                                'sumando01': i.sumando01,
                                'sumando02': i.sumando02,
                                'resultado': i.resultado
                              } for i in posts])

def serialize(self):
    return {
        'sumando01': self.sumando01,
        'sumando02': self.sumando02,
        'resultado': self.resultado
    }

if __name__ == '__main__':
    app.run()
