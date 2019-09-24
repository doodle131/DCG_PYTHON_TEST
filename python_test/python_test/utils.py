# utility class for viewsets 
class ApiViewSetMixin(object):
    
    def perform_create(self, serializer, **kwargs):
        instance = serializer.save(**kwargs)
        self.post_perform(serializer, instance)

    def perform_update(self, serializer, **kwargs):
        instance = serializer.save(**kwargs)

    def post_perform(self, serializer, instance):
        pass
