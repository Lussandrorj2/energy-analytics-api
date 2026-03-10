import multiprocessing

import os

bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"

workers = multiprocessing.cpu_count() * 2 + 1

timeout = 30

accesslog = "-"
errorlog = "-"

loglevel = "info"