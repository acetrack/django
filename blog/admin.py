# UserID: admin(local), acetrack(pythonanywhere)
# PassWD:

from django.contrib import admin
from .models import Post

admin.site.register(Post)