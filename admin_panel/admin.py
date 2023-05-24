from django.contrib import admin
from admin_panel.models import *

admin.site.register(Categoriya)
admin.site.register(SubCategoriya)
admin.site.register(Flowers)
admin.site.register(FlowersCommentVideos)

admin.site.register(TypeDelivery)
admin.site.register(FlowersDelivery)
admin.site.register(FlowersImages)

admin.site.register(Blogs)
admin.site.register(SeoCategory)
admin.site.register(SeoContent)