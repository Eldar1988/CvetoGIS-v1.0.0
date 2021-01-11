import telebot
from telebot import types

bot = telebot.TeleBot('1373937202:AAGwGGK8hHPBbM-M95w8RbnqbpJZHS1hxdo')
chat_id = '-1001462058223'


def new_order(send_data):
    message_header = f"=====  \nНовый заказ - {send_data['city']} \n===== \n"
    bot.send_message(chat_id, message_header)
    for i in send_data['products']:
        caption = f"{i['title']} \n{i['quantity']} x {i['price']} = {i['sum']}\n-------------------------\n" \
                  f"Продавец: \n{i['seller']} ({i['seller_phone']})"
        bot.send_photo(chat_id, i['image'], caption)

    message_footer = f"=====   Детали заказа   =====\n\nТоваров на сумму: {send_data['products_sum_price']} \n" \
                     f"Стоимость доставки: {send_data['order_sum'] - send_data['products_sum_price']}\n" \
                     f"Итого к оплате: {send_data['order_sum']}\n\n" \
 \
                     f"Имя заказчика: {send_data['name']}\n" \
                     f"Телефон заказчика: {send_data['phone']}\n" \
                     f"Имя получателя: {send_data['receiver_name']}\n" \
                     f"Телефон получателя: {send_data['receiver_phone']}\n" \
                     f"Адрес доставки: {send_data['address']}\n" \
                     f"Заказчик сам получит заказ: {send_data['bayer_is_receiver']}\n" \
                     f"Дата доставки:\n{send_data['delivery_date']}\n" \
                     f"Открытка: {send_data['postcard']}\n" \
                     f"===========================\n" \
                     f"Способ оплаты: {send_data['payment_method']}\n" \
                     f"===========================\n" \

    bot.send_message(chat_id, message_footer)
    bot.send_message(chat_id, text=' +     +\n ++++\n    +\n')
