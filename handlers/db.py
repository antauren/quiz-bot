import json


def get_user_data(user_id, redis_db) -> dict:
    user_data = redis_db.get(user_id)

    return {'stat': 0, 'answer': ''} if user_data is None else json.loads(user_data)


def update_user_data(user_id, redis_db, data: dict):
    user_data = get_user_data(user_id, redis_db)

    user_data.update(data)

    redis_db.set(user_id, json.dumps(user_data))
