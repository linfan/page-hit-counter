from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host= "redis", port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'You have hit this page {0} times. - Edition v1' . format (redis.get( 'hits' ))

if __name__ == "__main__":
    app.run(host= "0.0.0.0", debug=False)
