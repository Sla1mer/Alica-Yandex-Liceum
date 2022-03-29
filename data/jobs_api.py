import flask
from flask import request, jsonify

from . import db_session
from .jobs import Jobs
from .news import News

blueprint = flask.Blueprint('jobs_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {'jobs': [item.to_dict(only=('id', 'job', 'team_leader', 'work_size', 'collaborators',
                                     'start_date', 'end_date', 'is_finished',
                                     'category')) for item in jobs]})


@blueprint.route('/api/jobs/<int:job_id>')
def get_job_id(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    return jsonify({'jobs': job.to_dict(only=('id', 'job', 'team_leader', 'work_size', 'collaborators',
                                              'start_date', 'end_date', 'is_finished',
                                              'category'))})


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    job = Jobs(id=request.json['id'],
               team_leader=request.json['team_leader'],
               job=request.json['job'],
               work_size=request.json['work_size'],
               collaborators=request.json['collaborators'],
               start_date=request.json['start_date'],
               end_date=request.json['end_date'],
               is_finished=request.json['is_finished'])

    if job.id == db_sess.query(Jobs).get(job.id).id:
        return jsonify({'id': "Id already exists"})
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})
