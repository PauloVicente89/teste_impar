from modules.photo.models import Photo

class PhotoService:

    @staticmethod
    def get_photo_by_id(id: str) -> Photo:
        return Photo.objects.filter(id=id).first()

    @staticmethod
    def create_photo(base64: str) -> Photo:
        return Photo.objects.create(base64=base64)