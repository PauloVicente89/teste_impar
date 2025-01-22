import base64
from rest_framework import status
from rest_framework.response import Response
from modules.photo.services import create_photo, get_photo_by_id
import uuid

def photo_validation(photo_file: str):
    if isinstance(photo_file, str) and _is_valid_uuid(photo_file):
        photo = get_photo_by_id(photo_file)
        if photo:
            return photo
        else:
            return Response({"error": "A foto com o UUID fornecido não foi encontrada."}, status=status.HTTP_400_BAD_REQUEST)
    else:
        photo_base64 = _process_photo(photo_file)
        if photo_base64:
            photo = create_photo(photo_base64)
            return photo
        else:
            return Response({"error": "Formato de foto inválido."}, status=status.HTTP_400_BAD_REQUEST)
        
def _is_valid_uuid(value: str) -> bool:
    if uuid.UUID(value):
        return True
    return False

def _process_photo(photo_file: str) -> str | None:
    if isinstance(photo_file, bytes) or hasattr(photo_file, 'read'):
        return base64.b64encode(photo_file.read()).decode('utf-8')
    return None