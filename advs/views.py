from flask import jsonify, request
from flask.views import MethodView
from flask_login import current_user

from validate import validate, CreateUserSchema, CreateAdvSchema, hash_password
from errors import ApiError
from models import Advertisement, User, get_session_maker
from crud import get_item, create_item, delete_item, patch_item

Session = get_session_maker()


class UserView(MethodView):

    def get(self, user_id: int):
        with Session() as session:
            user = session.query(User).get(user_id)
            if user is None:
                raise ApiError(404, 'User not exists')
            return jsonify({'id': user.id, 'email': user.email})

    def post(self):
        user_data = validate(request.json, CreateUserSchema)
        with Session() as session:
            user_data['password'] = hash_password(user_data['password'])
            new_user = create_item(session, User, **user_data)
            return jsonify({'status': 'ok', 'id': new_user.id, 'email': new_user.email})


class AdvertisementView(MethodView):

    def get(self, adv_id):
        with Session() as session:
            adv = get_item(session, Advertisement, adv_id)
            return jsonify({
                'title': adv.title,
                'description': adv.description,
                'created_at': adv.created_at,
                'user_id': adv.user_id
            })

    def post(self):
        new_data = request.json
        new_data['user_id'] = current_user.get_id()
        new_data = validate(new_data, CreateAdvSchema)

        with Session() as session:

            new_adv = create_item(session, Advertisement, **new_data)
            return jsonify({
                'status': 'ok',
                'id': new_adv.id,
                'title': new_adv.title,
                'user_id': new_adv.user_id
            })

    def patch(self, adv_id: int):
        adv_data = request.json
        with Session() as session:
            adv = get_item(session, Advertisement, adv_id)
            if current_user.get_id() == adv.user_id:
                patch_adv = patch_item(session, adv, **adv_data)
                return jsonify({
                    'status': 'ok',
                    'id': patch_adv.id,
                    'title': patch_adv.title,
                    'user_id': patch_adv.user_id
                })
            raise ApiError(403, 'Access denied')

    def delete(self, adv_id: int):
        with Session() as session:
            adv = get_item(session, Advertisement, adv_id)
            if current_user.get_id() == adv.user_id:
                delete_item(session, adv)
                return jsonify({'status': 'deleted'})
            raise ApiError(403, 'Access denied')
