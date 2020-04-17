from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# post処理の入力フォームを表示
@app.route("/request_post", methods=["GET"])
def post_sample():
    return render_template('send_post.html')

# postでの入力情報処理
@app.route("/request_post", methods=["POST"])
def post_action():
    if "gender" in request.form.keys():
        gender = request.form["gender"]
        if gender == "男":
            sex = '男性'
        elif gender == "女":
            sex = "女性"
    else:
        sex = '性別不明'
    if 'age' in request.form.keys():
        age_range = request.form['age']
    else:
        age_range = '年齢不詳'
    return f'あなたは{sex}で{age_range}です。'

app.run(debug=True)