from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage
comments_data = {}

# POST: Add a new comment
@app.route("/api/tasks/<int:task_id>/comments", methods=["POST"])
def add_comment(task_id):
    data = request.get_json()
    if not data.get("content") or not data.get("author"):
        return jsonify({"error": "Missing content or author"}), 400

    if task_id not in comments_data:
        comments_data[task_id] = []

    # Assign incremental ID
    next_id = len(comments_data[task_id]) + 1
    data["id"] = next_id
    data["task_id"] = task_id
    now = datetime.now().isoformat()
    data["created_at"] = now
    data["updated_at"] = now

    comments_data[task_id].append(data)
    return jsonify({"task_id": task_id, "comment": data}), 201

# GET: List all comments for a task
@app.route("/api/tasks/<int:task_id>/comments", methods=["GET"])
def get_comments(task_id):
    task_comments = comments_data.get(task_id, [])
    return jsonify(task_comments), 200

# PUT: Update a comment
@app.route("/api/tasks/<int:task_id>/comments/<int:comment_id>", methods=["PUT"])
def update_comment(task_id, comment_id):
    task_comments = comments_data.get(task_id)
    if not task_comments:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    for comment in task_comments:
        if comment["id"] == comment_id:
            comment.update(data)
            comment["updated_at"] = datetime.now().isoformat()
            return jsonify(comment), 200

    return jsonify({"error": "Comment not found"}), 404

# DELETE: Remove a comment
@app.route("/api/tasks/<int:task_id>/comments/<int:comment_id>", methods=["DELETE"])
def delete_comment(task_id, comment_id):
    task_comments = comments_data.get(task_id)
    if not task_comments:
        return jsonify({"error": "Task not found"}), 404

    for i, comment in enumerate(task_comments):
        if comment["id"] == comment_id:
            task_comments.pop(i)
            return jsonify({"message": "Comment deleted"}), 200

    return jsonify({"error": "Comment not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
