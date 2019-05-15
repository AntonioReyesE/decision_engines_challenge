from flask import Flask
from routes.search_string_routes import search_bp
app = Flask(__name__)

app.register_blueprint(search_bp)

if __name__ == "__main__":
  app.run()
