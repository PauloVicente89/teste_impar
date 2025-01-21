SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': "Digite 'Bearer <token>' para autenticar"
        }
    },
    'DEFAULT_MODEL_DEPTH':-1
}