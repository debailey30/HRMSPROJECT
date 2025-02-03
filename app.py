import json
import os

# Step 1: Define the path to the config file
config_path = os.path.join(os.path.dirname(__file__), 'config.json')

# Step 2: Open and read the config file
try:
    with open(config_path, 'r', encoding='utf-8') as file:
        config = json.load(file)
except FileNotFoundError:
    print(f"Error: The config file at {config_path} was not found.")
    config = {}
except json.JSONDecodeError:
    print(f"Error: The config file at {config_path} is not a valid JSON.")
    config = {}

# Step 3: Access the configuration settings safely
database_host = config.get('database', {}).get('host', 'default_host')
server_port = config.get('server', {}).get('port', 'default_port')
logging_level = config.get('logging', {}).get('level', 'default_level')
jwt_secret = config.get('security', {}).get('jwtSecret', 'default_secret')
api_base_url = config.get('api', {}).get('baseUrl', 'default_url')
enable_feature_x = config.get('features', {}).get('enableFeatureX', False)

# Example usage in application logic
def connect_to_database(host):
    print(f"Connecting to database at {host}...")

def start_server(port):
    print(f"Starting server on port {port}...")

connect_to_database(database_host)
start_server(server_port)
print('JWT Secret:', jwt_secret)
print('API Base URL:', api_base_url)
print('Feature X Enabled:', enable_feature_x)