def make_shirt(size='large', message='I love Python'):
    print(f"Shirt size: {size}, with message: {message}")

make_shirt()
make_shirt('I love Python') # L'ordine dei parametri è importante
make_shirt(message='nike')
make_shirt(size='small', message='I Love Golang')