app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

card_bucket_list = []
next_id = 1

return render_template('index.html', cards=card_bucket_list)

@app.route('/add', methods=['POST'])
def add_card():
    ...
    card_bucket_list.append({...})