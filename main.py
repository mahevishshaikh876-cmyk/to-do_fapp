from flask import Flask,render_template,request

app=Flask(__name__, template_folder="template")

todolist=[]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add',methods=['POST'])
def add():

    todo=request.form.get('todo')
    des=request.form.get('des')

    print(todo, des)

    tododict={
        "todo":todo,
        "des":des
    }

    todolist.append(tododict)

    return render_template('index.html', todo=todolist)
 

if __name__=='__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)