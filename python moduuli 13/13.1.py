from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku')
def summa():
    args = request.args
    isPrime = True
    luku = int(args.get("luku"))
    for i in range(luku):
       if i == (luku-2):
           isPrime = True
           break
       luku2 = luku%(luku-(i+1))
       if int(luku2) == 0:
           isPrime = False
           break


    vastaus = {
        "Number" : luku, "isPrime" : isPrime
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
"""print("anna lukusi, selvitän onko se alkuluku: ")
#haluan että se yrittää jakaa itsensä luvuilla, jos siitä tulee jotain muuta kuin 0 se ei ole alkuluku
no = "tämä luku ei ole alkuluku. "
luku = int(input())
if luku < 1:
    print(no)
else:
   for i in range(luku):
       if i == (luku-2):
           print("tämä luku on alkuluku! ")
           break
       luku2 = luku%(luku-(i+1))
       if int(luku2) == 0:
           print(no)
           break
       else:
           print("trying...")"""