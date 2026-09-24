def _validate_state(attempts: int, mastery: float) -> None:
    if attempts < 0:
        raise ValueError("attempts must be non-negative")
    if not 0.0 <= mastery <= 1.0:
        raise ValueError("mastery must be between 0 and 1")


def hint_level(attempts: int, mastery: float, requested_answer: bool = False) -> int:
    """Return 0 to 3, from monitoring to a worked sub-step."""
    _validate_state(attempts, mastery)
    if mastery >= 0.85 and attempts <= 1:
        return 0

    level = 1
    if attempts >= 2 or mastery < 0.55:
        level = 2
    if attempts >= 4 or mastery < 0.30:
        level = 3
    if requested_answer:
        level = min(level + 1, 3)
    return level


def tutor_move(problem: str, attempts: int, mastery: float) -> str:
    """Select a restrained tutoring move without revealing a full answer."""
    if not problem.strip():
        raise ValueError("problem must not be empty")
    level = hint_level(attempts, mastery)
    moves = {
        0: "Ask the learner to justify the next step before offering help.",
        1: "Ask a focused question that points to the relevant concept.",
        2: "Name the concept and ask the learner to apply it to one sub-part.",
        3: "Demonstrate one sub-step, then return control to the learner.",
    }
    return moves[level]
