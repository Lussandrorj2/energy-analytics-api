import os
import multiprocessing

# Pega a porta do Render ou usa 8000 por padrão
port = os.environ.get("PORT", "10000")
bind = f"0.0.0.0:{port}"

workers = multiprocessing.cpu_count() * 2 + 1
threads = 2
timeout = 120  # Aumentado para evitar timeout no boot
accesslog = "-"
errorlog = "-"
loglevel = "info"