from handlers.quiz import handle_new_question_request, handle_surrender, handle_stat_request, handle_solution_attempt


def add_vk_prefix(id):
    return 'vk_{}'.format(id)


def hadle_message(text, user_id, redis_db, encoding):
    vk_user_id = add_vk_prefix(user_id)

    if text == 'Новый вопрос':
        message = handle_new_question_request(vk_user_id, redis_db, encoding)

    elif text == 'Сдаться':
        message = handle_surrender(vk_user_id, redis_db)

    elif text == 'Моя статистика':
        message = handle_stat_request(vk_user_id, redis_db)

    else:
        message = handle_solution_attempt(text, vk_user_id, redis_db)

    return message
