from django.conf.urls.defaults import patterns, url

js_info_dict = {
    'packages': ('geonode.maps','geonode.capabilities'),
    }

urlpatterns = patterns('geonode.maps.views',
    url(r'^$', 'maps', name='maps_home'),
    url(r'^new/?$', 'newmap', name="maps_new"),
    url(r'^new/data$', 'newmapJSON', name='maps_new_JSON'),
    (r'^(?P<mapid>\d+)/share/?$', 'map_share'),
    (r'^(?P<mapid>\d+)/info/?$', 'map_controller'),
    (r'^(?P<mapid>\d+)/info/describe/?$', 'describemap'),
    url(r'^(?P<mapid>\d+)/download/$', 'map_download', name='maps_download'),
    url(r'^check/$', 'check_download', name='maps_download_check'),
    (r'^checkurl/?$', 'ajax_url_lookup'),
    (r'^history/(?P<mapid>\d+)/?$', 'ajax_snapshot_history'),
    (r'^embed/$', 'embed'),
    (r'^(?P<mapid>[^/]+)/embed/?$', 'embed'),
    (r'^(?P<mapid>[^/]+)/mobile/?$', 'mobilemap'),
    (r'^print/?$', 'printmap'),
    url(r'^(?P<mapid>\d+)/data$', 'mapJSON', name='maps_JSON'),
    (r'^addgeonodelayer/?$', 'addLayerJSON'),
    (r'^snapshot/create/?$', 'snapshot_create'),
    url(r'^search/?$', 'maps_search_page', name='maps_search'),
    url(r'^search/api/?$', 'maps_search', name='maps_search_api'),
    url(r'^search/detail/?$', 'maps_search_result_detail', name='map_search_detail'),
    url(r'^(?P<mapid>\d+)/ajax-permissions$', 'ajax_map_permissions', name='maps_ajax_perm'),
    url(r'^change-poc/(?P<ids>\w+)$', 'change_poc', name='maps_change_poc'),
    url(r'^(?P<mapid>\d+)/ajax-permissions-email/?$', 'ajax_map_permissions_by_email',
        name='ajax_map_permissions_by_email'),
    (r'^(?P<mapid>[^/]+)/(?P<snapshot>[A-Za-z0-9_\-]+)/?$', 'view'),
    (r'^(?P<mapid>[^/]+)/(?P<snapshot>[A-Za-z0-9_\-]+)/embed/?$', 'embed'),
    (r'^(?P<mapid>[^/]+)/(?P<snapshot>[A-Za-z0-9_\-]+)/mobile/?$', 'mobilemap'),   
    (r'^(?P<mapid>[^/]+)/?$', 'view'),
)

datapatterns = patterns('geonode.maps.views',
    url(r'^resolve_user/?$', 'resolve_user', name='layer_resolve_user'),
    url(r'^$', 'browse_data', name='data_home'),
    url(r'^acls/?$', 'layer_acls', name='data_acls'),
    url(r'^search/?$', 'search_page', name='data_search'),
    url(r'^search/api/?$', 'metadata_search', name='data_search_api'),
    url(r'^search/detail/?$', 'search_result_detail', name='data_search_detail'),
    url(r'^api/batch_permissions/?$', 'batch_permissions', name='data_batch_perm'),
    url(r'^api/batch_permissions_by_email/?$', 'batch_permissions_by_email'),
    url(r'^api/batch_delete/?$', 'batch_delete', name='data_batch_del'),
    url(r'^upload/?', 'upload_layer', name='data_upload'),
    url(r'^download$', 'batch_layer_download', name='data_download'),
    url(r'^create_pg_layer', 'create_pg_layer', name='create_pg_layer'),
    url(r'^addlayers/?$', 'addlayers', name='addlayers'),
    (r'^layerstats/?$', 'ajax_increment_layer_stats'),
    # Local layers
    url(r'^(?P<layername>[^/]*)$', 'layer_detail', name="data_detail"),
    url(r'^(?P<layername>[^/]*)/metadata$', 'layer_metadata', name="data_metadata"),
    url(r'^(?P<layername>[^/]*)/contacts$', 'layer_contacts', name="layer_contacts"),
    url(r'^(?P<layername>[^/]*)/remove$', 'layer_remove', name="data_remove"),
    url(r'^(?P<layername>[^/]*)/replace$', 'layer_replace', name="data_replace"),
    url(r'^(?P<layername>[^/]*)/style$', 'layer_style', name="data_style"),
    url(r'^(?P<layername>[^/]*)/ajax-permissions$', 'ajax_layer_permissions', name='data_ajax_perm'),
    url(r'^(?P<layername>[^/]*)/ajax-permissions-email$', 'ajax_layer_permissions_by_email', name="data_ajax_perm_email"),

    (r'^(?P<layername>[^/]*)/ajax-edit-check/?$', 'ajax_layer_edit_check'),
    (r'^(?P<layername>[^/]*)/ajax_layer_update/?$', 'ajax_layer_update'),
    (r'^layerstats/?$', 'ajax_increment_layer_stats'),
    url(r'^addlayers/?$', 'addlayers', name='addlayers'),
    url(r'^api/batch_permissions_by_email/?$', 'batch_permissions_by_email'),
    url(r'^create_pg_layer', 'create_pg_layer', name='create_pg_layer'),

    # Remote layers

    url(r'^(?P<service>[^/]*)/(?P<layername>[^/]*)/metadata$', 'layer_metadata', name="data_metadata"),
    url(r'^(?P<service>[^/]*)/(?P<layername>[^/]*)/contacts$', 'layer_contacts', name="layer_contacts"),
    url(r'^(?P<service>[^/]*)/(?P<layername>[^/]*)/remove$', 'layer_remove', name="data_remove"),
    url(r'^(?P<service>[^/]*)/(?P<layername>[^/]*)/ajax-permissions$', 'ajax_layer_permissions', name='data_ajax_perm'),
    url(r'^(?P<service>[^/]*)/(?P<layername>[^/]*)/ajax-permissions-email$', 'ajax_layer_permissions_by_email', name="data_ajax_perm_email"),
    url(r'^(?P<service>[^/]*)/(?P<layername>[^/]*)/?$', 'layer_detail', name="data_detail"),
)

