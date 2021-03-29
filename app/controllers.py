from flask import render_template, Blueprint, redirect, url_for, request, jsonify, Response
import json
from uuid import uuid4
from datetime import date, datetime
from uszipcode import SearchEngine
from app.forms import *


base = Blueprint('base', __name__, url_prefix='/', template_folder='templates')


@base.route('/', methods=['GET', 'POST'])
def home():

    form = NewCity()

    if form.validate_on_submit():
        zipcode = form.zipcode.data
        return redirect(url_for('base.city', zipcode=zipcode))

    return render_template('home.html')


@base.route('/city/<zipcode>', methods=['GET', 'POST'])
def city(zipcode):

    search = SearchEngine(simple_zipcode=True)
    city_data = search.by_zipcode(zipcode)

    return render_template('city.html', city_data=city_data)
