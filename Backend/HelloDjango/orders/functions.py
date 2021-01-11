from shop.models import Product, City
from shop.serializers import ProductDetailSerializer
from .models import PaymentMethod
from .tgbot import new_order


def get_order_products(order):
    data = order.data
    product_titles = [x for x in data['products'].split(',')]
    order_products = Product.objects.filter(title__in=product_titles)
    quantities = data['quantities'].split(',')
    send_data = {}
    index = 0
    products = []
    products_sum_price = 0

    for i in order_products:
        product = {
            'quantity': quantities[index],
            'title': i.title,
            'image': i.image.url,
            'price': i.price,
            'sum': i.price * int(quantities[index]),
            'seller': i.seller.title,
            'seller_phone': i.seller.phone
        }
        products_sum_price += product['sum']
        products.append(product)
        index += 1

    send_data['city'] = City.objects.get(id=data['city']).title
    send_data['products'] = products
    send_data['name'] = data['name']
    send_data['phone'] = data['phone']
    send_data['receiver_name'] = data['receiver_name']
    send_data['receiver_phone'] = data['receiver_phone']
    send_data['address'] = data['address']
    send_data['bayer_is_receiver'] = data['bayer_is_receiver']
    send_data['delivery_date'] = data['delivery_date']
    send_data['order_sum'] = data['order_sum']
    send_data['postcard'] = data['postcard']
    send_data['products_sum_price'] = products_sum_price
    send_data['payment_method'] = PaymentMethod.objects.get(id=data['payment']).title

    new_order(send_data)

