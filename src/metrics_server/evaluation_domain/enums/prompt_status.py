from extensions.enums.choice_enum import ChoiceEnum


class PromptStatus(ChoiceEnum):
    CREATED = "CREATED"
    COMPLETED = "COMPLETED"
    RETRIGGERED = "RETRIGGERED"
