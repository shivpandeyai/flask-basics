"""
Part 4: Dynamic Routes - URL Parameters
========================================
How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Try different URLs like /user/YourName or /post/123
"""

from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/user/<username>')  # <username> captures any text from URL, visit: /user/Alice, /user/Bob
def user_profile(username):
    return render_template('user.html', username=username)


@app.route('/post/<int:post_id>')  # <int:post_id> captures only integers, /post/abc returns 404
def show_post(post_id):
    posts = {  # Simulated post data (in real apps, this comes from a database)
        1: {'title': 'Getting Started with Flask', 'content': 'Flask is a micro-framework...'},
        2: {'title': 'Understanding Routes', 'content': 'Routes map URLs to functions...'},
        3: {'title': 'Working with Templates', 'content': 'Jinja2 makes HTML dynamic...'},
    }
    post = posts.get(post_id)  # Get the post or None if not found
    return render_template('post.html', post_id=post_id, post=post)


@app.route('/user/<username>/post/<int:post_id>')  # Multiple dynamic segments, visit: /user/Alice/post/1
def user_post(username, post_id):
    return render_template('user_post.html', username=username, post_id=post_id)


@app.route('/about/')  # Trailing slash means both /about and /about/ work
def about():
    return render_template('about.html')


@app.route('/links')  # Demonstrates url_for() - generates URLs dynamically (better than hardcoding!)
def show_links():
    links = {
        'home': url_for('home'),
        'about': url_for('about'),
        'user_alice': url_for('user_profile', username='Alice'),
        'user_bob': url_for('user_profile', username='Bob'),
        'post_1': url_for('show_post', post_id=1),
        'post_2': url_for('show_post', post_id=2),
    }
    return render_template('links.html', links=links)



#Exercise 4.1: Create a product page
#   - Add route /product/<int:product_id>
#   - Create a products dictionary with id, name, price
#   - Display product details or "Not Found" message
# ...existing code...

@app.route('/products')  # New route to display all products
def products_list():
    products = {
        1: {'name': 'Laptop', 'price': 65000},
        2: {'name': 'Samsung Refrigerator', 'price': 35000},
        3: {'name': 'Study Table', 'price': 25000},
    }
    return render_template('products.html', products=products)

@app.route('/product/<int:product_id>')  # New route for individual product
def show_product(product_id):
    products = {
        1: {'name': 'Laptop', 'price': 65000},
        2: {'name': 'Samsung Refrigerator', 'price': 35000},
        3: {'name': 'Study Table', 'price': 25000},
    }
    product = products.get(product_id)
    return render_template('product.html', product_id=product_id, product=product)      

# Exercise 4.2: Category and product route

@app.route('/category/<category_name>/product/<int:product_id>')
def category_product(category_name, product_id):
    # Database with categories and products
    categories = {
        'electronics': {
            1: {'name': 'Laptop', 'price': 65000, 'description': 'High-performance laptop'},
            2: {'name': 'Smartphone', 'price': 35000, 'description': 'Latest smartphone model'},
            3: {'name': 'Tablet', 'price': 25000, 'description': 'Portable tablet device'},
        },
        'furniture': {
            1: {'name': 'Study Table', 'price': 15000, 'description': 'Wooden study table'},
            2: {'name': 'Office Chair', 'price': 8000, 'description': 'Ergonomic office chair'},
            3: {'name': 'Bookshelf', 'price': 12000, 'description': 'Wooden bookshelf'},
        },
        'appliances': {
            1: {'name': 'Samsung Refrigerator', 'price': 35000, 'description': 'Double door refrigerator'},
            2: {'name': 'Washing Machine', 'price': 28000, 'description': 'Automatic washing machine'},
            3: {'name': 'Microwave', 'price': 8000, 'description': 'Digital microwave oven'},
        }
    }
    
    # Get category data
    category = categories.get(category_name.lower())
    
    if not category:
        return render_template('category_product.html', 
                             category_name=category_name, 
                             product_id=product_id, 
                             product=None, 
                             error='Category not found')
    
    # Get product from category
    product = category.get(product_id)
    
    return render_template('category_product.html', 
                         category_name=category_name, 
                         product_id=product_id, 
                         product=product)

@app.route('/categories')
def categories():
    categories_info = {
        'electronics': {
            'description': 'Latest gadgets and electronic devices',
            'icon': '🖥️',
            'color': '#667eea',
            'products': {
                1: 'Laptop',
                2: 'Smartphone',
                3: 'Tablet'
            }
        },
        'electricals': {
            'description': 'Electrical supplies and wiring materials',
            'icon': '⚡',
            'color': '#f6ad55',
            'products': {
                1: 'LED Bulb',
                2: 'Switch Board',
                3: 'Extension Cord'
            }
        },
        'furniture': {
            'description': 'Quality furniture for home and office',
            'icon': '🪑',
            'color': '#48bb78',
            'products': {
                1: 'Study Table',
                2: 'Office Chair',
                3: 'Bookshelf'
            }
        }
    }
    return render_template('categories.html', categories=categories_info)

@app.route('/search', methods=['POST'])
def search_submit():
    query = (request.form.get('query') or '').strip()
    if not query:
        return redirect(url_for('home'))
    return redirect(url_for('search', query=query))


@app.route('/search/<query>')
def search(query):
    # same category data used elsewhere
    categories = {
        'electronics': {
            1: {'name': 'Laptop', 'price': 65000, 'description': 'High-performance laptop with Intel i7 processor'},
            2: {'name': 'Smartphone', 'price': 35000, 'description': 'Latest 5G smartphone with 128GB storage'},
            3: {'name': 'Tablet', 'price': 25000, 'description': '10-inch tablet perfect for entertainment'},
        },
        'electricals': {
            1: {'name': 'LED Bulb', 'price': 250, 'description': 'Energy-efficient 12W LED bulb'},
            2: {'name': 'Switch Board', 'price': 450, 'description': 'Modular switch board for home wiring'},
            3: {'name': 'Extension Cord', 'price': 350, 'description': '5-meter heavy-duty extension cord'},
        },
        'furniture': {
            1: {'name': 'Study Table', 'price': 15000, 'description': 'Wooden study table with storage drawers'},
            2: {'name': 'Office Chair', 'price': 8000, 'description': 'Ergonomic office chair with lumbar support'},
            3: {'name': 'Bookshelf', 'price': 12000, 'description': '5-shelf wooden bookshelf for home library'},
        }
    }

    q = query.lower()
    results = []
    for cat_name, prods in categories.items():
        for pid, pdata in prods.items():
            if (q in pdata['name'].lower()) or (q in pdata.get('description', '').lower()) or (q in cat_name):
                results.append({
                    'category': cat_name,
                    'id': pid,
                    'name': pdata['name'],
                    'price': pdata['price'],
                    'description': pdata.get('description', '')
                })

    return render_template('search_results.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# URL PARAMETER TYPES:
# =============================================================================
#
# <variable>         - String (default), accepts any text without slashes
# <int:variable>     - Integer, accepts only positive integers
# <float:variable>   - Float, accepts floating point numbers
# <path:variable>    - String, but also accepts slashes
# <uuid:variable>    - UUID strings
#
# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 4.1: Create a product page
#   - Add route /product/<int:product_id>
#   - Create a products dictionary with id, name, price
#   - Display product details or "Not Found" message
#
# Exercise 4.2: Category and product route
#   - Add route /category/<category_name>/product/<int:product_id>
#   - Display both the category and product information
#
# Exercise 4.3: Search route
#   - Add route /search/<query>
#   - Display "Search results for: [query]"
#   - Bonus: Add a simple search form that redirects to this route
#
# =============================================================================
