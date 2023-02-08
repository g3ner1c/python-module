import enum
from typing import Generator


class Category(enum.Enum):
    """
    A enum of the categories in the QB Reader database.
    """

    AMERICAN_LITERATURE = "American Literature"
    BRITISH_LITERATURE = "British Literature"
    CLASSICAL_LITERATURE = "Classical Literature"
    EUROPEAN_LITERATURE = "European Literature"
    WORLD_LITERATURE = "World Literature"
    OTHER_LITERATURE = "Other Literature"
    AMERICAN_HISTORY = "American History"
    ANCIENT_HISTORY = "Ancient History"
    EUROPEAN_HISTORY = "European History"
    WORLD_HISTORY = "World History"
    OTHER_HISTORY = "Other History"
    BIOLOGY = "Biology"
    CHEMISTRY = "Chemistry"
    PHYSICS = "Physics"
    MATH = "Math"
    OTHER_SCIENCE = "Other Science"
    VISUAL_FINE_ARTS = "Visual Fine Arts"
    AUDITORY_FINE_ARTS = "Auditory Fine Arts"
    OTHER_FINE_ARTS = "Other Fine Arts"
    RELIGION = "Religion"
    MYTHOLOGY = "Mythology"
    PHILOSOPHY = "Philosophy"
    SOCIAL_SCIENCE = "Social Science"
    CURRENT_EVENTS = "Current Events"
    GEOGRAPHY = "Geography"
    OTHER_ACADEMIC = "Other Academic"
    TRASH = "Trash"
    LITERATURE = "Literature"
    HISTORY = "History"
    SCIENCE = "Science"
    FINE_ARTS = "Fine Arts"

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.__str__()


class Difficulty(enum.Enum):
    """
    A enum of the difficulties in the QB Reader database.
    """

    UNRATED = 0
    MS = 1
    HS_EASY = 2
    HS_REGULAR = 3
    HS_HARD = 4
    HS_NATS = 5
    COLLEGE_EASY = 6
    COLLEGE_REGULAR = 7
    COLLEGE_HARD = 8
    COLLEGE_NATS = 9
    OPEN = 10

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.__str__()


class Tossup:
    def __init__(
        self,
        question: str,
        answer: str,
        formatted_answer: str,
        category: str | Category,
        subcategory: str | Category,
        packet_number: int,
        question_number: int,
        difficulty: int | Difficulty,
        set_name: str,
    ):
        self.question = question
        self.answer = answer
        self.formatted_answer = formatted_answer
        self.category = Category(category)
        self.subcategory = Category(subcategory)
        self.packet_number = packet_number
        self.question_number = question_number
        self.difficulty = Difficulty(difficulty)
        self.set_name = set_name

        self.powerable = "(*)" in self.question

    def __str__(self) -> str:
        return self.question

    def __repr__(self) -> str:
        return self.__str__()


class BonusPart:
    def __init__(self, question: str, answer: str, formatted_answer: str):
        self.question = question
        self.answer = answer
        self.formatted_answer = formatted_answer

    def __str__(self) -> str:
        return self.question

    def __repr__(self) -> str:
        return self.__str__()


class Bonus:
    def __init__(
        self,
        leadin: str,
        parts: list[str],
        answers: list[str],
        formatted_answers: list[str],
        category: str | Category,
        subcategory: str | Category,
        packet_number: int,
        question_number: int,
        difficulty: int | Difficulty,
        set_name: str,
    ):
        self.leadin = leadin

        self.parts: list[BonusPart] = [
            BonusPart(part, answer, formatted_answer)
            for part, answer, formatted_answer in zip(parts, answers, formatted_answers)
        ]

        self.category = Category(category)
        self.subcategory = Category(subcategory)
        self.packet_number = packet_number
        self.question_number = question_number
        self.difficulty = Difficulty(difficulty)
        self.set_name = set_name

    def __str__(self) -> list[str]:
        return [self.leadin] + [str(part) for part in self.parts]

    def __repr__(self) -> list[str]:
        return self.__str__()


class Packet:
    def __init__(
        self,
        tossups: list[Tossup],
        bonuses: list[Bonus],
        packet_number: int,
        difficulty: int | Difficulty,
        set_name: str,
    ):
        self.tossups = tossups
        self.tossups.sort(key=lambda tossup: tossup.question_number)
        self.bonuses = bonuses
        self.bonuses.sort(key=lambda bonus: bonus.question_number)
        self.packet_number = packet_number
        self.difficulty = Difficulty(difficulty)
        self.set_name = set_name

    def __str__(self) -> str:
        return f"Packet {self.packet_number} of {self.set_name}"

    def __repr__(self) -> str:
        return self.__str__()

    def __iter__(self) -> Generator:
        yield from zip(self.tossups, self.bonuses)
