import math

from flask import Flask, render_template, request, redirect
import dao
from app import app,login
from flask_login import login_user,logout_user
from app.models import Category, Product, User




@app.route('/')
def index():
    kw= request.args.get('kw')
    cates = dao.load_categories()
    cate_id=request.args.get('cate_id')
    page=request.args.get('page')
    product = dao.load_products(kw=kw,cate_id=cate_id,page=page)

    num = dao.count_product()

    return render_template('index.html', categories=cates, products=product,
                           pages=math.ceil(num/app.config['PAGE_SIZE']))
@app.route('/products/<id>')
def details(id):
    return render_template('detail.html')

# @app.route('/admin/login',methods=['post'])
# def login_admin_process():
#     request.form.get('name')
#     request.form.get('passwd')
@app.route('/admin/login',methods=['post'])
def login_admin():
    username = request.form.get('username')
    password = request.form.get('pwd')

    u = dao.auth_user(username=username, password=password)
    if u:
        login_user(user=u)

    return redirect('/admin')


@login.user_loader
def get_user_by_id(user_id):
    return User.query.get(user_id)



if __name__=='__main__':
    from app import admin
    app.run(debug=True)
