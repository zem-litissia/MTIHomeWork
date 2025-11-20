from flask import Blueprint, render_template, request, redirect, url_for
from ..models.member import Member
from ..storage.csv_storage import CSVStorage

bp = Blueprint('members', __name__, url_prefix='/members')

@bp.route('/')
def list_members():
    members = CSVStorage.load_members()
    return render_template('members.html', members=members)

@bp.route('/add', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        name = request.form['name']
        major = request.form['major']
        skills = request.form['skills'].split(',')
        member = Member(name=name, major=major, skills=skills)
        CSVStorage.save_member(member)
        return redirect(url_for('members.list_members'))
    return render_template('add_member.html')
# controller