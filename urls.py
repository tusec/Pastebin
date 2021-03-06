from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',    	
	(r'^pastebin/index.*','pastebin.pasteapp.views.index'),	
    (r'^pastebin/([A-Za-z]+)','pastebin.pasteapp.views.text_by_user'),	
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^pastebin/*','pastebin.pasteapp.views.index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
