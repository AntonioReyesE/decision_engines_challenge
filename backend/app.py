"""
  Runs the application and starts the proper database connections.
"""
from flask import Flask
from routes.search_string_routes import search_bp
from general.databases.MongoDBHandler import MongoDBHandler
from general.settings import load_env
import os
app = Flask(__name__)

# Register the application's routes
app.register_blueprint(search_bp)


@app.before_first_request
def initialize():
  """
      Initializes the application connection to the Database
  """
  mongo_conn = MongoDBHandler()
  mongo_conn.init_db()
  load_env()



if __name__ == "__main__":
  app.run(debug=True)

