from flask import Flask, request, jsonify
import os
from redis.cluster import RedisCluster as Redis
from redis.cluster import ClusterNode

# Define Redis Cluster nodes
startup_nodes = [
    ClusterNode(os.environ["REDIS_HOST1"], int(os.environ["REDIS_PORT1"])),
    ClusterNode(os.environ["REDIS_HOST2"], int(os.environ["REDIS_PORT2"])),
    ClusterNode(os.environ["REDIS_HOST3"], int(os.environ["REDIS_PORT3"]))
]

# Create a Redis Cluster instance
redis_cluster = Redis(startup_nodes=startup_nodes, decode_responses=True)

# Create a Flask application
app = Flask(__name__)

# API endpoint to create a key-value pair in Redis
@app.route('/key', methods=['POST'])
def create_key():
    data = request.json
    key = data.get('key')
    value = data.get('value')
    if key and value:
        redis_cluster.set(key, value)
        return jsonify({'message': f'Key "{key}" created successfully.'}), 200
    else:
        return jsonify({'error': 'Key and value are required.'}), 400

# API endpoint to update the value of a key in Redis
@app.route('/key', methods=['PUT'])
def update_key():
    data = request.json
    key = data.get('key')
    value = data.get('value')
    if key and value:
        if redis_cluster.exists(key):
            redis_cluster.set(key, value)
            return jsonify({'message': f'Value of key "{key}" updated successfully.'}), 200
        else:
            return jsonify({'error': f'Key "{key}" does not exist.'}), 404
    else:
        return jsonify({'error': 'Key and value are required.'}), 400

# API endpoint to get the value of a key from Redis
@app.route('/key', methods=['GET'])
def get_key():
    key = request.args.get('key')
    if key:
        value = redis_cluster.get(key)
        if value is not None:
            return jsonify({'value': value}), 200
        else:
            return jsonify({'error': f'Key "{key}" not found.'}), 404
    else:
        return jsonify({'error': 'Key is required.'}), 400

# API endpoint to delete a key from Redis
@app.route('/key', methods=['DELETE'])
def delete_key():
    key = request.args.get('key')
    if key:
        if redis_cluster.exists(key):
            redis_cluster.delete(key)
            return jsonify({'message': f'Key "{key}" deleted successfully.'}), 200
        else:
            return jsonify({'error': f'Key "{key}" does not exist.'}), 404
    else:
        return jsonify({'error': 'Key is required.'}), 400

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
