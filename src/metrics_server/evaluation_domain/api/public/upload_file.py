from evaluation_domain.enums import TYPE_PROMPT_MAP
from evaluation_domain.models import Prompt
import json
import uuid

def upload_file_api(dataframe):
    run_id = uuid.uuid4()
    records = dataframe.to_json(orient ='records')
    records = json.loads(records)
    for record in records:
        record_type = record.get('Type', None)
        if record_type in TYPE_PROMPT_MAP.keys():
            prompt_structure = TYPE_PROMPT_MAP[record_type]['prompt_structure']
            schema = TYPE_PROMPT_MAP[record_type]['schema']
            serialied_data = schema.load(data=record)
            sentence = prompt_structure.format(serialied_data.get('Context'), serialied_data.get('Question'))
            Prompt.get_or_create(run_id=run_id, sentence=sentence, llm_models=serialied_data.get('LlmModel'), prompt_type=record_type)
        else:
            raise NotImplementedError
    return