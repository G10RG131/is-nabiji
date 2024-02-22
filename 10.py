import requests


def get_products():
    api_url = "https://fakestoreapi.com/products"
    response = requests.get(api_url)
    print(response.status_code, "\n")
    return response.json()


def parese_data():
    products = get_products()

    products_price = []
    products_rating = []
    products_title = []
    products_category = set()

    for product in products:
        products_price.append(float(product['price']))
        products_category.add(str(product['category']))
        products_title.append({'title': product['title'], 'id': product['id']})
        products_rating.append(product['rating'])

    category = list(products_category)
    category.sort()
    print("max: ", max(products_price), "min: ", min(products_price), "average: ",
          sum(products_price) / len(products_price), "\n")
    print(category, "\n")
    print(sorted(products_title, key=lambda p: p['title']), "\n")
    print(sorted(products_rating, key=lambda p: p['rate']))


parese_data()
