"""
CodeFactory Solutions - Task Manager API
Aplicação de exemplo usada para demonstrar a adoção da Cultura DevOps
(versionamento, containerização e integração contínua).
"""
import os
from datetime import datetime

from flask import Flask, jsonify, request

app = Flask(__name__)

# "Banco de dados" em memória apenas para fins didáticos.
# Em um cenário real, isso seria substituído por Postgres/MySQL
# (ver serviço "db" no docker-compose.yml).
tasks = []
next_id = 1


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "app": "CodeFactory Solutions - Task Manager",
        "status": "online",
        "timestamp": datetime.utcnow().isoformat()
    })


@app.route("/health", methods=["GET"])
def health():
    """Endpoint usado por health checks do Docker e do pipeline de CI."""
    return jsonify({"status": "healthy"}), 200


@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(tasks), 200


@app.route("/tasks", methods=["POST"])
def create_task():
    global next_id
    data = request.get_json(silent=True) or {}
    title = data.get("title")

    if not title:
        return jsonify({"error": "O campo 'title' é obrigatório"}), 400

    task = {
        "id": next_id,
        "title": title,
        "done": False,
        "created_at": datetime.utcnow().isoformat()
    }
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json(silent=True) or {}
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = data.get("done", task["done"])
            return jsonify(task), 200
    return jsonify({"error": "Tarefa não encontrada"}), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
