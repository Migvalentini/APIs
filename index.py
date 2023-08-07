from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {'id': 1, 'titulo': 'Aprendendo Python', 'autor': 'Mark Lutz', 'ano_publicacao': 2013},
    {'id': 2, 'titulo': 'Clean Code', 'autor': 'Robert C. Martin', 'ano_publicacao': 2008},
    {'id': 3, 'titulo': 'The Pragmatic Programmer', 'autor': 'Andrew Hunt', 'ano_publicacao': 1999},
]

@app.route('/livros', methods=['GET'])
def get_livros():
    return jsonify({'livros': livros})

@app.route('/livros', methods=['POST'])
def add_livro():
    novo_livro = request.json
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

@app.route('/livros/<int:id>', methods=['PUT'])
def update_livro(id):
    livro_atualizado = request.json
    for livro in livros:
        if livro['id'] == id:
            livro.update(livro_atualizado)
            return jsonify(livro), 200
    return jsonify({'error': 'Livro não encontrado'}), 404

@app.route('/livros/<int:id>', methods=['DELETE'])
def delete_livro(id):
    for livro in livros:
        if livro['id'] == id:
            livros.remove(livro)
            return jsonify({'message': 'Livro removido com sucesso'}), 200
    return jsonify({'error': 'Livro não encontrado'}), 404

@app.route('/livros/<int:id>', methods=['PATCH'])
def patch_livro(id):
    atualizacao = request.json
    for livro in livros:
        if livro['id'] == id:
            livro.update(atualizacao)
            return jsonify(livro), 200
    return jsonify({'error': 'Livro não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
