from rest_framework.viewsets import ViewSet 
from rest_framework.decorators import action
from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from evaluation_domain.api.public import upload_file_api
import ast
from evaluation_domain.api.web.schemas import PromptCreationSchema

class UploadViewset(ViewSet):
    """
    Viewset for csv file upload api
    """
    @action(detail=False, methods=['post'])
    def upload_file(self, request):
        try:
            data = request.data
            prompt = data.get('prompt', None)
            csv_file = data.get('file', None)
            llm_models = data.get('llm_models', 'CHAT_GPT')
            metrics = ast.literal_eval(data.get('metrics', "['all']"))
            data_dict = {
                'prompt': prompt,
                'metrics': metrics,
                'csv_file': csv_file,
                'llm_models': llm_models,
            }
            prompt_creation_schema = PromptCreationSchema()
            serialied_data = prompt_creation_schema.load(data=data_dict)
            upload_file_api(serialied_data)
            return JsonResponse({"Result": "File Uploaded"}, status=HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"Error Message": str(e)}, status=HTTP_400_BAD_REQUEST)