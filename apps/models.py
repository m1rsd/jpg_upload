from django.db.models import Model, FileField, CharField, TextChoices


class UploadedFile(Model):
    class TypeChoice(TextChoices):
        JPG = 'jpg', 'Jpg'
        SVG = 'svg', 'Svg'

    name = CharField(max_length=255, blank=True, null=True)
    file = FileField(upload_to='uploads/%Y/%m/')
    type = CharField(max_length=10, choices=TypeChoice.choices)
    # _MAX_SIZE = 120

    # def save(self, *args, **kwargs):
    #     super(UploadedFile, self).save(*args, **kwargs)
    #
    #     if self.type == self.TypeChoice.SVG:
    #         if self.file:
    #             filepath = self.file.path
    #             width = 120
    #             height = 60
    #
    #             max_size = max(width, height)
    #
    #             # if max_size > self._MAX_SIZE:
    #                 image = Image.open(filepath)
    #                 # resize - безопасная функция, она создаёт новый объект, а не
    #                 # вносит изменения в исходный, поэтому так
    #                 image = image.resize(
    #                     (round(width / max_size * self._MAX_SIZE),  # Сохраняем пропорции
    #                      round(height / max_size * self._MAX_SIZE)),
    #                     Image.ANTIALIAS
    #                 )
    #                 image.save(filepath)
