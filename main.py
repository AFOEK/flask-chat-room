from flask import *
from flask_socketio import *
import hashlib

app = Flask(__name__)
hash_obj = hashlib.sha512(b'0x9f17cd320d8d4abd9dc18535391dd0b09784dcd9590d9fc11764331eae69f0b1389d3582ab69ef71fa6605dc470b5f3737f581c2807f9f')
hash_dig = hash_obj.hexdigest()
app.config['SECRET_KEY'] = hash_dig
socketio = SocketIO(app)

@app.route('/')
def session():
    

if __name__ == '__main__':
    socketio.run(app, debug=True, port=80)