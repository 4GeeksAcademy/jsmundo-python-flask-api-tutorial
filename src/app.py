from flask import Flask, jsonify,request
app = Flask(__name__)

# Lista global de 'todos'
todos = [{"label":"My first task","done": False}]

# Ruta para '/myroute' que devuelve un mensaje HTML
@app.route('/myroute', methods=['GET'])
def hello_world():
  return "<h1>Hello!</h1>"


# Ruta para obtener la lista de todos (GET /todos)
@app.route('/todos',methods=['GET'])
def get_todos():
   return jsonify(todos)


# Ruta para agregar un nuevo todo (POST /todos)
@app.route('/todos',methods=['POST'])
def add_new_todo():
   request_body = request.json
   print("Incoming request with the following body",request_body)
   todos.append(request_body) # Agrega el nuevo todo a la lista 'todos'
   return jsonify(todos)# Devuelve la lista actualizada

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
   if position < 0 or position >= len(todos):
     return jsonify({"error": "Invalid position"}), 404 
   
   removed_task = todos.pop(position)
   print(f"Deleted task at position {position}: {removed_task}")
   return jsonify(todos), 200   
    






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
