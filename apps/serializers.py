import xml.etree.ElementTree as ET

from PIL import Image
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.models import UploadedFile


def get_svg_size(file):
    tree = ET.parse(file)
    root = tree.getroot()
    width = root.attrib.get('width')
    height = root.attrib.get('height')
    return (width, height)


class UploadedFileSerializer(ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ('id', 'name', 'file', 'type')

    def validate_file(self, value):
        if value.content_type == 'image/svg+xml':
            width, height = get_svg_size(value)
            if width == 32 and height == 32:
                return value
        elif value.content_type == 'image/jpeg':
            img = Image.open(value)
            width, height = img.size
            if width == 120 and height == 60:
                return value
        else:
            raise ValidationError('Invalid file format or size')
