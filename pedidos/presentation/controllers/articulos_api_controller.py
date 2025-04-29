from flask import Blueprint, jsonify, request
from pedidos.adapters.articulos_adapter import ArticulosAdapter
from pedidos.application.articulo_service import ArticulosService
from pedidos.domain.articulo import Articulo
from pedidos import db

articulos_api = Blueprint("articulos_api", __name__, url_prefix="/api/articulos")

@articulos_api.route("/", methods=["GET"])
def get_all_articulos():
    articulos_repository = ArticulosAdapter(db)
    articulos_service = ArticulosService(articulos_repository)
    filtro = request.args.get("filtro", "")
    articulos = articulos_service.find_all(filtro)
    return jsonify([{
        "id": articulo.id(),        
        "codigo": articulo.codigo(),
        "nombre": articulo.nombre(),
        "precio": articulo.precio()
    } for articulo in articulos])

@articulos_api.route("/<int:id>", methods=["GET"])
def get_articulo_by_id(id):
    articulos_repository = ArticulosAdapter(db)
    articulos_service = ArticulosService(articulos_repository)
    articulo = articulos_service.get_by_id(id)
    if articulo is None:
        return jsonify({"error": "Artículo no encontrado"}), 404
    return jsonify({
        "id": articulo.id(),
        "codigo": articulo.codigo(),
        "nombre": articulo.nombre(),
        "precio": articulo.precio()
    })

@articulos_api.route("/", methods=["POST"])
def create_articulo():
    data = request.json
    articulos_repository = ArticulosAdapter(db)
    articulos_service = ArticulosService(articulos_repository)
    articulo_id = articulos_service.get_next_id()
    articulo = Articulo(
        id=articulo_id,
        codigo=data["codigo"],
        nombre=data["nombre"],
        precio=data.get("precio", 0.0)
    )
    articulos_service.add(articulo)
    return jsonify({"message": "Artículo creado exitosamente"}), 201

@articulos_api.route("/<int:id>", methods=["PUT"])
def update_articulo(id):
    data = request.json
    articulos_repository = ArticulosAdapter(db)
    articulos_service = ArticulosService(articulos_repository)
    articulo = articulos_service.get_by_id(id)
    if articulo is None:
        return jsonify({"error": "Artículo no encontrado"}), 404
    articulo.setCodigo(data["codigo"])
    articulo.setNombre(data["nombre"])
    articulo.setPrecio(data.get("precio", articulo.precio()))
    articulos_service.update(articulo)
    return jsonify({"message": "Artículo actualizado exitosamente"})

@articulos_api.route("/<int:id>", methods=["DELETE"])
def delete_articulo(id):
    articulos_repository = ArticulosAdapter(db)
    articulos_service = ArticulosService(articulos_repository)
    articulo = articulos_service.get_by_id(id)
    if articulo is None:
        return jsonify({"error": "Artículo no encontrado"}), 404
    articulos_service.delete(id)
    return jsonify({"message": "Artículo eliminado exitosamente"})

