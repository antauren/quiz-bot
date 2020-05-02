import os
import random


def get_random_question_answer(dir_path='questions', encoding='UTF-8') -> tuple:
    file_name = random.choice(os.listdir(dir_path))

    path = os.path.join(dir_path, file_name)

    text = read_file(path, encoding)

    question_answer_list = parse_questions(text)

    return random.choice(question_answer_list)


def read_file(path, encoding='UTF-8') -> str:
    with open(path, encoding=encoding) as fd:
        return fd.read()


def parse_questions(text: str) -> list:
    splitted_text = text.split('\n' * 2)

    question_answer_list = []

    for num, paragraph in enumerate(splitted_text[:-1]):
        paragraph = paragraph.strip()
        next_paragraph = splitted_text[num + 1].strip()

        if paragraph.startswith('Вопрос ') and next_paragraph.startswith('Ответ:'):
            question, answer = map(lambda paragraph_: paragraph_.split('\n', 1)[-1],
                                   (paragraph, next_paragraph))

            question_answer_list.append((question, answer))

    return question_answer_list
