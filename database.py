import sqlite3

connection = sqlite3.connect('database.db', check_same_thread=False)
sql = connection.cursor()

#users
sql.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, number TEXT, location TEXT);')

#products
sql.execute('CREATE TABLE IF NOT EXISTS products '
            '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'name TEXT,'
            'quantity INTEGER,'
            'price REAL,'
            'description TEXT,'
            'photo TEXT);')
#cart
sql.execute('CREATE TABLE IF NOT EXISTS cart'
            '(id INTEGER,'
            'product TEXT,'
            'quantity INTEGER,'
            'total REAL);')

#methods
def register(id, name, number, location):
    sql.execute('INSERT INTO users VALUES(?,?,?,?)', (id, name, number, location))
    connection.commit()

def if_user_exist(id):
    data = sql.execute('SELECT id FROM users WHERE id=?;', (id,))
    if data.fetchone():
        return True
    else:
        return False

def add_product(pr_name, pr_amount, pr_price, pr_des, pr_photo):
    sql.execute('INSERT INTO products'
                '(name,'
                'quantity,'
                'price,'
                'description,'
                'photo) VALUES (?,?,?,?,?);', (pr_name, pr_amount, pr_price, pr_des, pr_photo))
    connection.commit()

def show_info(pr_id):
    sql.execute('SELECT name, quantity, price, description. photo FROM products WHERE id=?;', (pr_id,)).fetchone()


def show_all_products():
    all_products = sql.execute('SELECT * FROM products;')

    return all_products.fetchall()

def get_pr_name_id():
    products = sql.execute('SELECT id, name, quantity, price FROM products;')

    return products.fetchall()


def get_pr_id():
    prods = sql.execute('SELECT name, id, quantity FROM products;').fetchall()
    sorted_prods = [i[1] for i in prods if i[2]>0]

    return sorted_prods

def get_pr_name(id):
    product = sql.execute('SELECT name FROM products WHERE id=?;', (id,))
    return product.fetchone()

#add to cart
def add_to_cart(user_id, pr_name, pr_quantity, user_total = 0):
    sql.execute('INSERT INTO cart (id, product, quantity, total)'
                'VALUES (?,?,?,?);', (user_id, pr_name, pr_quantity, user_total))

    amount = sql.execute('SELECT quantity FROM products WHERE name=?;', (pr_name,)).fetchone()
    print(pr_name)
    sql.execute(f'UPDATE products SET quantity={amount[0] - pr_quantity} WHERE name=?;', (pr_name,))

    connection.commit()


def del_cart(user_id):
    pr_name = sql.execute('SELECT product FROM cart WHERE user_id=?', (user_id)).fetchone()
    amount = sql.execute('SELECT quantity FROM products WHERE name=?;', (pr_name)).fetchone()[0]
    pr_quantity = sql.execute('SELECT quantity FROM cart WHERE user_id=?;', user_id).fetchone()
    sql.execute(f'UPDATE products SET quantity={amount + pr_quantity} WHERE name=?;', (pr_name,))
    sql.execute('DELETE FROM cart WHERE id=?;', (user_id,))
    connection.commit()


def show_cart(user_id):
    cart = sql.execute('SELECT product, quantity, total FROM cart WHERE id=?;',(user_id,))
    return cart.fetchone()

print(sql.execute('SELECT * FROM products').fetchall())



