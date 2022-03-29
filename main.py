from flask import Flask, make_response, jsonify
from flask_restful import Api

from data import db_session, news_api, jobs_api, users_resources

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)


@app.errorhandler(404)
def not_found(_):
    return make_response(jsonify({'error': 'Not found'}), 404)


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(news_api.blueprint)
    app.register_blueprint(jobs_api.blueprint)

    # для списка объектов
    api.add_resource(users_resources.UsersResource, '/api/v2/users')

    # для одного объекта
    api.add_resource(users_resources.UsersListResource, '/api/v2/users/<int:user_id>')

    app.run()


if __name__ == '__main__':
    main()
