from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import userSerializers, SentimentAnalysisSerializer
from django.contrib.auth.models import User
from myapp.views import analyze_sentiment
 
class userviewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializers
    permission_classes = [IsAuthenticated, IsAdminUser]

class SentimentAnalysisView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        serializer = SentimentAnalysisSerializer(data=request.data)
        if serializer.is_valid():
            input_text = serializer.validated_data['input_text']
            print(input_text)
            sentiment=analyze_sentiment(input_text)
            response_data = {
                'input_text': input_text,
                'sentiment': sentiment
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)