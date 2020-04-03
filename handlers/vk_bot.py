from handlers.quiz import handle_new_question_request, handle_surrender, handle_stat_request, handle_solution_attempt


def hadle_message(text, user_id, redis_db):
    if text == 'Новый вопрос':
        message = handle_new_question_request(user_id, redis_db)
    elif text == 'Сдаться':
        message = handle_surrender(user_id, redis_db)

    elif text == 'Моя статистика':
        message = handle_stat_request(user_id, redis_db)

    else:
        message = handle_solution_attempt(text, user_id, redis_db)

    return message
