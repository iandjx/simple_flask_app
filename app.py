from flask import Flask

app = Flask(__name__)

# POST - used to receive data
# GET - used to send data back only

stores = [
    {
        'name': 'My Store',
        'item': [
            {
                'name': 'shirt',
                'price': 16.00
            }
        ]
    }
]


@app.route('/store', methods=['POST'])
def create_store():
    pass


@app.route('/store/<string:name>')
def get_store(name):
    pass


@app.route('/store')
def get_stores():
    pass


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass


###

# @app.route('/')
# def home():
#     return "Hello World"

app.run(port=5000)
