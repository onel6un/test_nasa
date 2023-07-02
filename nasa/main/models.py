from django.db import models
from django.utils.safestring import mark_safe


class Slide(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(
        'Картинка',
        upload_to='slider/',
        blank=True
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
