import redis

# Conectar a Redis
r = redis.Redis(host='localhost', port=6379)

# Crear un objeto de suscripción
pubsub = r.pubsub()

# Suscribirse al canal
pubsub.subscribe('my_channel')

# Procesar mensajes en tiempo real
for message in pubsub.listen():
    if message['type'] == 'message':
        print(f'Received: {message["data"].decode("utf-8")}')

