import sqlite3
from bottle import route, run, debug, template, request

conn = sqlite3.connect('lb1.db')
cursor = conn.cursor()


@route('/item<item:re:[0-9]+>')
def show_item(item):

    cursor.execute("SELECT quote FROM quotes WHERE id LIKE ?", (item),)
    result = cursor.fetchall()

    if not result:
        return 'This item number does not exist!'
    else:
        return 'QUOTE: %s' % result[0]


@route('/insert', method='GET')
def insert():
    if request.GET.save:
        id = 102
        quote = request.GET.quote.strip()
        author = request.GET.author.strip()
        link = request.GET.link.strip()
        cursor.execute("INSERT INTO quotes VALUES(?,?,?,?)",
                       (id, quote, author, link))

        conn.commit()

        return '<p>>The new task was inserted into the database, the ID is %s</p>' % id
    else:
        return template('new.tpl')


@route('/update/<no:int>', method='GET')
def update_item(no):
    if request.GET.save:
        quote = request.GET.quote.strip()
        author = request.GET.author.strip()
        cursor.execute(
            "UPDATE quotes SET quote = ?, author = ? WHERE id LIKE ?", (quote, author, no))
        conn.commit()

        return '<p>The item number %s was successfully updated</p>' % no
    else:
        cursor.execute("SELECT * FROM quotes WHERE id LIKE ?", str((no)))
        cur_data = cursor.fetchone()
        print(cur_data)

        return template('update', old=cur_data, no=no)


@route('/delete/<no:int>', method="GET")
def delete_item(no):
    cursor.execute("DELETE FROM quotes WHERE id=?", str(no))
    conn.commit()
    return '<p>The item number %s was successfully deleted</p>' % no


run(host='localhost', port=8080, debug=True)
