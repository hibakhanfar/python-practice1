def save_and_read_notes(filename: str, read_user_input: str) -> str:
    with open(filename, "a") as file:
        file.write(read_user_input + "\n")
    with open(filename, "r") as file:
        return file.read()


def show_last_notes(filename: str, limit: int = 5) -> None:
    try:
        with open(filename, "r") as file:
            notes = file.readlines()
    except FileNotFoundError:
        print(f"No notes found. '{filename}' does not exist yet.")
        return

    last_notes = notes[-limit:]

    print("\n--- Recent Notes ---")
    if not last_notes:
        print("(No notes to display.)")
    else:
        for note in last_notes:
            print(note.strip())

