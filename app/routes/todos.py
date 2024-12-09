# app/routes/todos.py

from flask_restx import Namespace, Resource, fields
from flask import request
from app.models import Todo, db

todos_bp = Namespace('todos', description='Todo routes')

# API model for input validation
todo_model = todos_bp.model('Todo', {
    'title': fields.String(required=True, description='The title of the todo')
})

@todos_bp.route("/")
class TodoList(Resource):
    def get(self):
        """Get all todos."""
        todos = Todo.query.all()
        return [{"id": todo.id, "title": todo.title} for todo in todos], 200

    @todos_bp.expect(todo_model)
    def post(self):
        """Create a new todo."""
        data = request.get_json()
        title = data.get("title")
        new_todo = Todo(title=title)
        db.session.add(new_todo)
        db.session.commit()
        return {"message": "Todo created", "todo": {"id": new_todo.id, "title": new_todo.title}}, 201


@todos_bp.route("/<int:id>")
class TodoResource(Resource):
    def get(self, id):
        """Get a todo by ID."""
        todo = Todo.query.get_or_404(id)
        return {"id": todo.id, "title": todo.title}, 200

    @todos_bp.expect(todo_model)
    def put(self, id):
        """Update a todo by ID."""
        todo = Todo.query.get_or_404(id)
        data = request.get_json()
        todo.title = data.get("title", todo.title)
        db.session.commit()
        return {"message": "Todo updated", "todo": {"id": todo.id, "title": todo.title}}, 200

    def delete(self, id):
        """Delete a todo by ID."""
        todo = Todo.query.get_or_404(id)
        db.session.delete(todo)
        db.session.commit()
        return {"message": "Todo deleted"}, 200
