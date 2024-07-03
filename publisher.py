import redis

# Conectar a Redis
r = redis.Redis(host='localhost', port=6379)

# Publicar mensajes
for i in range(5):
    r.publish('my_channel', f'Message {i}')
    print(f'Published: Message {i}')
