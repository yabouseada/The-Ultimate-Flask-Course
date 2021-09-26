from flask import Flask,jsonify,request,url_for,redirect,session

app= Flask(__name__)
app.config['DEBUG']=True
app.config['SECRET_KEY']='Yahia'
app.secret_key="Hello"


@app.route('/')
def index():
    return '<h1>Hello,World!<h1>'

@app.route('/home', methods=['POST','GET'], defaults={'name':'User'})
@app.route('/home/<name>', methods=['POST','GET'])
def home(name):
    session["name"]= name
    return '<h1>Home {}, you are on the Home Page!<h1>'.format(name)

@app.route('/json')
def json():
    if "name" in session:
        name = session["name"]
        
    else:
        name = 'name not in session'
        
    return jsonify({'key':'value','listkey':[1,2,3], 'name': name})
@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>hi {}, you are from {} you are on query page!<h1>'.format(name,location)


@app.route('/theform', methods=['POST','GET'])
def theform():
    if request.method == 'GET':

        return '''<form method ="POST" action ="/theform">
                    <input type ="text" name="name">
                    <input type ="text" name="location">
                    <input type ="submit" name="Submit">
            </form>'''
    else:
        name= request.form['name']
        location = request.form['location']
        #return '<h1>hi {}, you are from {} you are on proces page!<h1>'.format(name,location)
        return redirect(url_for('home', name = name , location = location))

@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()

    name = data['name'] 
    location = data['location'] 
    randomlist = data['randomlist'] 

    return jsonify({'result':'success','name':name,'location':location,'randomlist':randomlist[1]})



if __name__=='__main__':
    app.run()
