from evaluation_domain.enums import PromptType
from evaluation_domain.api.web.schemas import PromptCreationSchema

TYPE_PROMPT_MAP = {
    PromptType.QA : {
        'prompt_structure': 'With the following context - {}, can you answer this question - {}',
        'schema': PromptCreationSchema()
    }
}