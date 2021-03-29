from flask import render_template, Blueprint, redirect, url_for, request, jsonify, Response
import json
from uuid import uuid4
from datetime import date, datetime


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/', methods=['GET', 'POST'])
def home():

    return render_template('home.html')

