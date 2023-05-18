server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for serv, conf in server_data.items():
    print(serv + ':')
    for key, value in conf.items():
        print('\t' + key + ':' + value)