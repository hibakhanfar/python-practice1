def read_raw_input(prompt: str ) -> str:
    return input(prompt).strip()


def get_user_info() -> str:
    name = read_raw_input("Name: ")
    topic = read_raw_input("Topic: ")

    return f"Hello {name}! Welcome to learning {topic}."

