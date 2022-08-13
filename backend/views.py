from rest_framework.views import APIView
from .utils import json_response
from .models import UserData

from .serializers import ChartDataSerializer


class ChartData(APIView):
    def post(self, request):
        data = request.data
        serializer = ChartDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        description = serializer.validated_data["description"]
        from_age = serializer.validated_data["from_age"]
        to_age = serializer.validated_data["to_age"]
        amount = serializer.validated_data["amount"]
        income_grows = serializer.validated_data["income_grows"]

        UserData.objects.create(description=description, amount=amount, from_age=from_age, to_age=to_age,
                                               income_grows=income_grows)
        return json_response(True, message='Data is Stored')

    def get(self, request):
        response = []
        user_data = UserData.objects.filter(id__gt=0)
        for data in user_data:
            dic = {
                "id": data.id,
                "description": data.description,
                "amount": data.amount,
                "from_age": data.from_age,
                "to_age": data.to_age,
                "income_grows": data.income_grows
            }
            response.append(dic)
        return json_response(True, data=response)


class FetchData(APIView):
    def get(self, request):
        response = []
        user_id = int(request.query_params["id"])
        user_data = UserData.objects.filter(id=user_id)
        for data in user_data:
            dic = {
                "id": data.id,
                "description": data.description,
                "amount": data.amount,
                "from_age": data.from_age,
                "to_age": data.to_age,
                "income_grows": data.income_grows
            }
            response.append(dic)
        return json_response(True, data=response)

    def put(self, request):
        serializer = ChartDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = request.data["id"]
        description = serializer.validated_data["description"]
        from_age = serializer.validated_data["from_age"]
        to_age = serializer.validated_data["to_age"]
        amount = serializer.validated_data["amount"]
        income_grows = serializer.validated_data["income_grows"]
        UserData.objects.filter(id=user_id).update(description=description, amount=amount, from_age=from_age, to_age=to_age,
                                                   income_grows=income_grows)

        return json_response(True, message='Data is Updated')



