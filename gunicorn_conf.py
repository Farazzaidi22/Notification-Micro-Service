import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "app"))

bind = "0.0.0.0:80"
workers = 4
worker_class = "uvicorn.workers.UvicornWorker"
app_module = "app.main:app"  # Adjust this line based on your app structure
