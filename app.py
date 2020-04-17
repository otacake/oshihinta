from flask import Flask,render_template,request
app = Flask(__name__)

hinata = ['潮紗理奈','影山優佳','加藤史帆','金村美玖','上村ひなの','河田陽菜','小坂奈緒','齊藤京子','佐々木久美','佐々木美玲','高瀬愛奈','高橋未来虹','高本彩花','富田鈴花','丹生明里','濱岸ひより','東村芽依','松田好花','宮田愛萌','森本茉莉','山口陽世','渡邉美穂']
lit = [2,4,5,12,21,13,14,6,7,8,9,22,10,15,16,17,11,18,19,23,24,20]
n = len(hinata)
dic = {}
for i in range(n):
    dic[hinata[i]] = lit[i]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/already_oshi')
def oshipic():
    return render_template('send_get.html')

@app.route('/already_oshi',methods = ["POST"])
def receive_get():
    hinata = ['潮紗理奈','影山優佳','加藤史帆','金村美玖','上村ひなの','河田陽菜','小坂奈緒','齊藤京子','佐々木久美','佐々木美玲','高瀬愛奈','高橋未来虹','高本彩花','富田鈴花','丹生明里','濱岸ひより','東村芽依','松田好花','宮田愛萌','森本茉莉','山口陽世','渡邉美穂']
    lit = [2,4,5,12,21,13,14,6,7,8,9,22,10,15,16,17,11,18,19,23,24,20]
    n = len(hinata)
    dic = {}
    for i in range(n):
        dic[hinata[i]] = lit[i]
    name = request.form["oshi_name"]
    ans = 0
    num = -10
    for i in range(n):
        if name == hinata[i]:
            num = dic[name]
            ans = 1
            break
    if ans == 1:
        return render_template('oshimen.html', num = num, name = name)
    if ans == 0:
        return '名前をもう一度確認してください'

@app.route('/notyet_oshi')
def kuji():
    import random
    num = random.randrange(n)
    oshi = hinata[num]
    indexa = dic[oshi]
    return render_template('decide.html',name = oshi,num = indexa)

app.run(debug=True)