from django.db import models
from django.utils.safestring import mark_safe
from filer.fields.image import FilerImageField


class Slide(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    image = FilerImageField(
        null=True,
        blank=True,
        related_name="slide_image",
        on_delete=models.CASCADE
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['order']

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 200px; height:150px;"/>' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self) -> str:
        return self.title
