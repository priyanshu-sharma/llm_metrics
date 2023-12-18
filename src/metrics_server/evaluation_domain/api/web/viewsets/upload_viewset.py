from rest_framework.viewsets import ViewSet 
from rest_framework.decorators import action
from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
import pandas as pd
from evaluation_domain.api.public import upload_file_api

class UploadViewset(ViewSet):
    """
    Viewset for csv file upload api
    """
    @action(detail=False, methods=['post'])
    def upload_file(self, request):
        try:
            csv_file = request.data.get('file', None)
            if not csv_file:
                return JsonResponse({"Error Message": "Input csv is not given"}, status=HTTP_400_BAD_REQUEST)
            df = pd.read_csv(csv_file)
            upload_file_api(df)
            return JsonResponse({"Result": "File Uploaded"}, status=HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"Error Message": str(e)}, status=HTTP_400_BAD_REQUEST)