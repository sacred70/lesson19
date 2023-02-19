from flask_restx import Resource, Namespace
from dao.model.genre import GenreSchema
from implemented import genre_service
from flask import request
from dec_cons.decorators import admin_required, auth_requiest

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_requiest
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        req_json = request.json
        genres = genre_service.create(req_json)
        return "", 201, {"location": f"/directors/{genres.id}"}


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_requiest
    def get(self, rid):
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, gid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = gid
        genre_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, gid):
        genre_service.delete(gid)
        return "", 204