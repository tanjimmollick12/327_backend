from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import Complain
from .serializers import ComplainSerializer, ComplainListSerializer, ComplainRespSerializer


class createComplain(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        current_user = request.user
        request.data["author"] = current_user.username
        request.data["role"] = current_user.role
        serializer = ComplainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComplainList(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        model = Complain.objects.all()
        serializer = ComplainListSerializer(model, many=True)
        return Response(serializer.data)


class respComplain(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def getComplain(self, complain_id):
        try:
            model = Complain.objects.get(id=complain_id)
            return model
        except Complain.DoesNotExist:
            return

    def put(self, request, complain_id):
        if not self.getComplain(complain_id):
            return Response(f"Complain with id: {complain_id} is not found", status=status.HTTP_404_NOT_FOUND)
        serializer = ComplainRespSerializer(self.getComplain(complain_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': f"Responded to {complain_id}'s Complain"}, status=status.HTTP_201_CREATED)
