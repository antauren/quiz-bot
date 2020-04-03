from handlers.question import get_random_question_answer
from handlers.db import get_user_data, update_user_data
from handlers.answer import is_answer_true


def handle_surrender(user_id, redis_db):
    user_data = get_user_data(user_id, redis_db)

    update_user_data(user_id, redis_db, {'is_answered': True})

    return 'Правильный ответ:\n\n{}'.format(user_data['answer'])


def handle_stat_request(user_id, redis_db):
    user_data = get_user_data(user_id, redis_db)

    return 'Количество угаданных вопросов: {}'.format(user_data['stat'])


def handle_new_question_request(user_id, redis_db):
    question, answer = get_random_question_answer()

    update_user_data(user_id, redis_db,
                     {'question': question, 'answer': answer, 'is_answered': False})

    return 'Вопрос:\n\n{}'.format(question)


def handle_solution_attempt(text, user_id, redis_db):
    request_answer = text

    user_data = get_user_data(user_id, redis_db)
    true_answer = user_data['answer']

    if is_answer_true(request_answer, true_answer):

        stat = user_data['stat'] if user_data['is_answered'] else user_data['stat'] + 1

        update_user_data(user_id, redis_db, {'stat': stat, 'is_answered': True})

        message = 'Правильно! Поздравляю! Для следующего вопроса нажми «Новый вопрос»'

    else:
        message = 'Неправильно... Попробуешь ещё раз?'

    return message
