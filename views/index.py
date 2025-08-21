from flask import Blueprint, render_template

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    return render_template('index.html')

@index_bp.route('/navbar-demo')
def navbar_demo():
    return render_template('navbar-demo.html')

@index_bp.route('/sidebar-demo')
def sidebar_demo():
    return render_template('sidebar-demo.html')