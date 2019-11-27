import os
import sentry_sdk

from bottle import route, run
# from bottle import Bottle, request
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://a80d45492b1040088e074568dde55569@sentry.io/1832576",
    integrations=[BottleIntegration()]
)

# app = Bottle()

@route('/success')  
def index():  
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Генератор утверждений</title>
  </head>
  <body>
    <div class="container">
      <h1>Коллеги, добрый день!</h1>
      <p>OK</p>
      <p class="small">Чтобы обновить это заявление, обновите страницу</p>
    </div>
  </body>
</html>
"""
    return html


@route('/fail')  
def index():  
    raise RuntimeError("There is an error!")  
    return  
  
  
if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
