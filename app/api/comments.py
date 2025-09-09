from flask import Blueprint, request, jsonify
from .. import db
from ..models import Task, Comment

# Define blueprint here 👇
bp = Blueprint("comments", __name__, url_prefix="/api")

@bp.route("/tasks/<int:task_id>/comments", methods=["POST"])
def create_comment(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json() or {}
    if not data.get("content"):
        return jsonify({"error": "Content is required"}), 400
    comment = Comment(task_id=task.id, content=data["content"], author=data.get("author"))
    db.session.add(comment)
    db.session.commit()
    return jsonify(comment.to_dict()), 201

@bp.route("/tasks/<int:task_id>/comments", methods=["GET"])
def list_comments(task_id):
    Task.query.get_or_404(task_id)
    comments = Comment.query.filter_by(task_id=task_id).all()
    return jsonify([c.to_dict() for c in comments]), 200

@bp.route("/comments/<int:comment_id>", methods=["PUT"])
def update_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    data = request.get_json() or {}
    if not data.get("content"):
        return jsonify({"error": "Content is required"}), 400
    comment.content = data["content"]
    db.session.commit()
    return jsonify(comment.to_dict()), 200

@bp.route("/comments/<int:comment_id>", methods=["DELETE"])
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({"message": "deleted"}), 200
