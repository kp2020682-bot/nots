from flask import Flask, request

app = Flask(__name__)

users = []

@app.route('/')
def home():
    return "<h1>Welcome</h1> <a href='/add-user'>Add User</a> | <a href='/users'>View Users</a>"


@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        return '''
        <h2>Add User</h2>
        <form method="POST">
            Name: <input type="text" name="name"><br>
            Age: <input type="text" name="age"><br>
            <button type="submit">Submit</button>
        </form>
        '''

    data = {
        "name": request.form.get('name'),
        "age": request.form.get('age')
    }

    users.append(data)

    return "<h3>User Added! <a href='/users'>See Users</a></h3>"


@app.route('/users')
def get_users():
    html = "<h2>Users List</h2><table border=1><tr><th>Index</th><th>Name</th><th>Age</th><th>Action</th></tr>"

    for i, user in enumerate(users):
        html += f"<tr><td>{i}</td><td>{user['name']}</td><td>{user['age']}</td><td><a href='/delete-user/{i}'>Delete</a></td></tr>"

    html += "</table><br><a href='/add-user'>Add More</a>"

    return html


@app.route('/delete-user/<int:index>')
def delete_user(index):
    if index < len(users):
        users.pop(index)
        return "<h3>Deleted! <a href='/users'>Back</a></h3>"
    else:
        return "Invalid index"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)