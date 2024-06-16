# File Path: API-Rock_of_Ages_NSS-Python-Django/rockapi/views/rock_view.py

from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rockapi.models import Rock
from rockapi.serializers import RockSerializer  # ! Updated import to use the new serializer

class RockView(ViewSet):
    """Rock view set"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized instance
        """
        try:
            user = request.auth.user  # ! Access authenticated user
            rock = Rock()
            rock.user = user  # ! Assign authenticated user to rock
            rock.name = request.data["name"]  # ! Assign name from request data
            rock.weight = request.data["weight"]  # ! Assign weight from request data
            rock.type_id = request.data["typeId"]  # ! Assign type from request data
            rock.save()

            serializer = RockSerializer(rock)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests for all items

        Returns:
            Response -- JSON serialized array
        """
        try:
            rocks = Rock.objects.all()
            serializer = RockSerializer(rocks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)
