from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
data = [
    {'id': 1, 'name': 'John'},
    {'id': 2, 'name': 'Jane'}
]

# Endpoint to get all data
# @app.route('/api/data', methods=['GET'])
# def get_data():
#     return jsonify(data)

# # Endpoint to get data by ID
# @app.route('/api/data/<int:data_id>', methods=['GET'])
# def get_data_by_id(data_id):
#     item = next((item for item in data if item['id'] == data_id), None)
#     if item:
#         return jsonify(item)
#     else:
#         return jsonify({'message': 'Data not found'}), 404

@app.route('/hello')
def hello_world():
   return 'hello world'

app.add_url_rule('/', 'hello', hello_world)


if __name__ == '__main__':
    app.run(debug=True)
