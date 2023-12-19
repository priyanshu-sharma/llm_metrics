import json
import uuid
import re
import pandas as pd
from evaluation_domain.models import Prompt

def upload_file_api(serialied_data):
    prompt = serialied_data.get('prompt')
    metrics = serialied_data.get('metrics')
    llm_models = serialied_data.get('llm_models')
    csv_file = serialied_data.get('csv_file')
    columns = re.findall(r'\{([^}]+)\}', prompt)
    print(prompt, metrics, csv_file, columns, llm_models)
    if len(columns) == 0:
        run_id = uuid.uuid4()
        Prompt.create([Prompt(run_id=run_id, sentence=prompt, llm_models=llm_models, meta={"metrics": metrics}, active=True)])
    elif len(columns) > 0 and csv_file:
        df = pd.read_csv(csv_file)
        if (set(columns) - set(df.columns)):
            raise NotImplementedError("Missing data in csv {}".format(set(columns) - set(df.columns)))
        create_prompt_list = []
        for index, row in df.iterrows():
            output_value = {}
            for column in columns:
                output_value[column] = row[column]
            sentence = prompt.format(**output_value)
            print(sentence)
            run_id = uuid.uuid4()
            create_prompt_list.append(Prompt(run_id=run_id, sentence=sentence, llm_models=llm_models, meta={"metrics": metrics}, active=True))
        Prompt.create(create_prompt_list)
    else:
        raise NotImplementedError("No csv present") 
    return