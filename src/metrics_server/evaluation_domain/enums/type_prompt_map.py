from evaluation_domain.enums import PromptType
from evaluation_domain.api.web.schemas import PromptCreationSchema

TYPE_PROMPT_MAP = {
    PromptType.QA : {
        'prompt_structure': 'With the following {}, can you tell me the answer for the following question - {}',
        'schema': PromptCreationSchema()
    }
}