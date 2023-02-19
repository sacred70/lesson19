from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema
from implemented import director_service
from dec_cons.decorators import admin_required, auth_requiest
from flask import request

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_requiest
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        req_json = request.json
        director = director_service.create(req_json)
        return "", 201, {"location": f"/directors/{director.id}"}


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_requiest
    def get(self, did):
        r = director_service.get_one(did)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, did):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = did
        director_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, did):
        director_service.delete(did)
        return "", 204
