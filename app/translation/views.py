# -*- coding: utf-8 -*-
from flask import render_template
from app.translation import blueprint


@blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html')
