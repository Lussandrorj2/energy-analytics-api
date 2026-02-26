from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .services import calcular_media_consumo


class MediaConsumoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cliente_id = request.query_params.get("cliente_id")

        if not cliente_id:
            return Response({"error": "cliente_id é obrigatório"}, status=400)

        try:
            cliente_id = int(cliente_id)
        except ValueError:
            return Response({"error": "cliente_id deve ser inteiro"}, status=400)

        data = calcular_media_consumo(cliente_id)

        if data is None:
            return Response({"error": "Cliente não possui consumos"}, status=404)

        return Response(data)