from rest_framework.viewsets import ViewSet 
from rest_framework.decorators import action
from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
import pandas as pd

class UploadViewset(ViewSet):
    """
    Viewset for csv file upload api
    """
    @action(detail=False, methods=['post'])
    def upload_file(self, request):
        print(request.data.get('file'))
        csv_file = request.data.get('file', None)
        if not csv_file:
             return JsonResponse({"Error Message": "Input csv is not given"}, status=HTTP_400_BAD_REQUEST)
        df = pd.read_csv(csv_file)
        print(df.head())
        return JsonResponse({"Result": "Okay"}, status=HTTP_200_OK)

# class FileUploadView(views.APIView):
#     parser_classes = (FileUploadParser,)

#     def put(self, request, filename, format=None):
#         file_obj = request.FILES['file']
#         # do some stuff with uploaded file
#         return Response(status=204)