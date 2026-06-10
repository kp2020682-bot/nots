from flask import Flask, request

app = Flask(__name__)

users = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')

        if name and age:
            users.append({"name": name, "age": age})
            return "<h2>User Added ✅<br><a href='/users'>View Users</a></h2>"

    return '''
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                font-family: Arial;
                padding: 20px;
            }
            input, button {
                width: 100%;
                padding: 15px;
                margin: 10px 0;
                font-size: 18px;
            }
            button {
                background: green;
                color: white;
                border: none;
            }
        </style>
    </head>
    <body>
        <h2>Add User</h2>
        <form method="POST">
            <input type="text" name="name" placeholder="Enter Name">
            <input type="number" name="age" placeholder="Enter Age">
            <button type="submit">Submit</button>
        </form>
    </body>
    </html>
    '''

@app.route('/users')
def users_list():
    html = '''
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { font-family: Arial; padding: 20px; }
            li { margin: 10px 0; font-size: 18px; }
        </style>
    </head>
    <body>
        <h2>Users</h2>
        <ul>
    '''

    for i, user in enumerate(users):
        html += f"<li>{user['name']} ({user['age']}) - <a href='/delete/{i}'>Delete</a></li>"

    html += "</ul><a href='/'>Home</a></body></html>"

    return html

@app.route('/delete/<int:index>')
def delete(index):
    if index < len(users):
        users.pop(index)
    return "<h3>Deleted! <a href='/users'>Back</a></h3>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
