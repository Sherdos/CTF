import json
import paho.mqtt.client as mqtt

# Настройки подключения
MQTT_BROKER = "192.168.0.200"  # IP вашего брокера Mosquitto
MQTT_PORT = 1883              # Порт по умолчанию
MQTT_USERNAME = 'admin'          # Имя пользователя, если есть
MQTT_PASSWORD = '20072604sh'          # Пароль, если есть



# Функция для публикации сообщений
def publish_message(topic, payload):
    """
    Публикует сообщение в указанный топик.
    :param topic: MQTT-топик (например, 'house/1/floor/2')
    :param payload: Сообщение (например, {'action': 'off'})
    """
    try:
        # Инициализация клиента MQTT
        client = mqtt.Client()

        if MQTT_USERNAME and MQTT_PASSWORD:
            client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.publish(topic, json.dumps(payload))
        client.disconnect()
    except Exception as e:
        print(f"Error publishing MQTT message: {e}")
