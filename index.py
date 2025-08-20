from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret")

# Importar blueprints
from views import index_bp

# Registrar blueprints
app.register_blueprint(index_bp)

if __name__ == "__main__":
    app.run(debug=True)