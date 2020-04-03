def is_answer_true(request_answer: str, true_answer: str) -> bool:
    handled_request_answer = handle_text(request_answer)
    handled_true_answer = handle_text(true_answer)

    for sym in {'.', '(', ',', ' - '}:
        handled_true_answer = handled_true_answer.split(sym, 1)[0]

    handled_true_answer = handled_true_answer.strip()

    return handled_true_answer == handled_request_answer


def handle_text(text: str) -> str:
    handled_text = text

    handled_text = handled_text.strip('.,"-!?# ')
    handled_text = handled_text.lower()
    handled_text = replace_yo(handled_text)

    return handled_text


def replace_yo(text):
    return text.replace('ё', 'е')
