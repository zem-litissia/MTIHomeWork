from flask import Blueprint, render_template, request, redirect, url_for
from ..services.member_service import MemberService

bp = Blueprint('members', __name__, url_prefix='/members')

@bp.route('/')
def list_members():
    members = MemberService.load_members()
    return render_template('members.html', members=members)

@bp.route('/add', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        name = request.form['name']
        major = request.form['major']
        skills = request.form['skills'].split(',')

        MemberService.add_member(
            name=name,
            major=major,
            skills=skills
        )

        return redirect(url_for('members.list_members'))
    return render_template('add_member.html')
