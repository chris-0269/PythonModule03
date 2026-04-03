import sys


def validate_input() -> list[int]:
    prog_name = sys.argv[0]
    raw_scores = sys.argv[1:]

    if len(raw_scores) < 1:
        raise ValueError("No scores provided.\n"
            f"USAGE ==> python3 {prog_name} <score1> <score2> ...")

    scores = []
    for arg in raw_scores:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid score: {arg}")
            continue

    if not scores:
        raise ValueError(
            "No scores provided.\n"
            f"USAGE ==> python3 {prog_name} <score1> <score2> ..."
        )
    return scores


def print_scores() -> None:
    print("=== Player Score analytics ===")
    scores = validate_input()

    players = len(scores)
    total_score = sum(scores)
    average_score = total_score / players
    highest_score = max(scores)
    lowest_score = min(scores)
    score_range = highest_score - lowest_score

    print(f"Total players: {players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {highest_score}")
    print(f"Lowest score: {lowest_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    try:
        print_scores()
    except ValueError as error:
        print(error)
