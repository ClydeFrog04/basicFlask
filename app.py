from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
# db.init_app(app)

class Todo(db.Model):#Todo is the table name, it's automatically lowercase when it's created
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return'<Task %r>' % self.id
    
with app.app_context():
    db.create_all()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        taskContent = request.form['content']
        if len(taskContent) < 1:
            tasks = Todo.query.order_by(Todo.date_created).all()
            return render_template("index.html", tasks=tasks, error="Your task needs to have a name")
        newTask = Todo(content=taskContent)

        try:
            print("sss" + newTask.content, file=sys.stderr)
            db.session.add(newTask)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return "There was an issue adding your task" + str(e)
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:id>")
def delete(id):
    taskToDelete = Todo.query.get_or_404(id)

    try:
        db.session.delete(taskToDelete)
        db.session.commit()
        return redirect("/")
    
    except Exception as e:
            return "There was an issue deleting that task: " + str(e)

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form["content"]
        
        try:
            db.session.commit()
            return redirect("/")
        except:
            return "we couldn't update that"
    else:
        return render_template("update.html", task=task)


if __name__ == "__main__":
    app.run(debug=True)

