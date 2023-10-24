def load_categories():
    return[{
        'id':1,
        'name':'Mobile'
    },
        {
            'id': 2,
            'name': 'Tablet'
        }
    ]
def load_products(kw=None):
    products = [{
        'id': 1,
        'name': 'Mobile',
        'price': 2000000,
        'image':'https://cdn.tgdd.vn/Products/Images/42/289700/iphone-14-pro-max-bac-thumb-600x600.jpg'
    },
        {
            'id': 2,
            'name': 'iphone',
            'price': 2000000,
            'image': 'https://cdn.tgdd.vn/Products/Images/42/289700/iphone-14-pro-max-bac-thumb-600x600.jpg'
        },
        {
            'id': 3,
            'name': 'iphone',
            'price': 2000000,
            'image': 'https://cdn.tgdd.vn/Products/Images/42/289700/iphone-14-pro-max-bac-thumb-600x600.jpg'
        },
        {
            'id': 4,
            'name': 'iphone',
            'price': 2000000,
            'image': 'https://cdn.tgdd.vn/Products/Images/42/289700/iphone-14-pro-max-bac-thumb-600x600.jpg'
        },
        {
            'id': 5,
            'name': 'iphone',
            'price': 2000000,
            'image': 'https://cdn.tgdd.vn/Products/Images/42/289700/iphone-14-pro-max-bac-thumb-600x600.jpg'
        },
        {
            'id': 6,
            'name': 'iphone',
            'price': 2000000,
            'image': 'https://cdn.tgdd.vn/Products/Images/42/289700/iphone-14-pro-max-bac-thumb-600x600.jpg'
        }
    ]

    if kw:
        products = [p for p in products if p['name'].find(kw)>=0]
    return products