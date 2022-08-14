from rest_framework.views import APIView
from .utils import json_response
from .models import UserData

from .serializers import ChartDataSerializer
from rest_framework.generics import get_object_or_404


class ChartData(APIView):
    """
    In  this class we can recieved the user data and store in table in post function call
    and send all the data to frontend in get function call
    delete function recieved the id and delete the data of this id
    """
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

    def delete(self, request):
        user_id = int(request.query_params["id"])
        user_data = get_object_or_404(UserData, id=user_id)
        user_data.delete()
        return json_response(True, message='Data is deleted')


class FetchData(APIView):
    """
    In this class the get function recieved the id and send it according to id
    the put function recieved all user data for update the information.
    """
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



