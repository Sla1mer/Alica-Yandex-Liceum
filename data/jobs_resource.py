from flask import jsonify
from flask_restful import abort, Resource

from data import db_session
from data.jobs import Jobs
from data.reqparse import parser
from data.users import User


def abort_if_news_not_found(jobs_id):
    session = db_session.create_session()
    jobs = session.query(User).get(jobs_id)
    if not jobs:
        abort(404, message=f"Jobs {jobs_id} not found")


class JobsResource(Resource):
    def get(self, jobs_id):
        abort_if_news_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        return jsonify({'users': jobs.to_dict(
            only=('title', 'content', 'user_id', 'is_private'))})

    def delete(self, jobs_id):
        abort_if_news_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'users': [item.to_dict(
            only=('title', 'content', 'user_id', 'is_private')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        jobs = Jobs(
            id=args['id'],
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=args['start_date'],
            end_date=args['end_date'],
            is_finished=args['is_finished']
        )
        session.add(jobs)
        session.commit()
        return jsonify({'success': 'OK'})