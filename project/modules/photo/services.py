from modules.photo.models import Photo

def get_photo_by_id(id: str):
    return Photo.objects.filter(id=id).first()

def create_photo(base64: str):
    return Photo.objects.create(base64=base64)