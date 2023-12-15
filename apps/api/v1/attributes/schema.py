from drf_spectacular.utils import extend_schema

from .serializers import AttributesSerializer


attrs_schema = {
    "get": extend_schema(
        summary="Список аттрибутов", responses={200: AttributesSerializer}
    )
}
