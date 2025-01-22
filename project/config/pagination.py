from rest_framework import pagination
from urllib.parse import urlparse, urlunparse
from django.conf import settings

class CustomGeneralPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'per_page'
    max_page_size = 20

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)

        def override_domain(url):
            if url:
                parsed_url = urlparse(url)
                new_url = parsed_url._replace(scheme='', netloc=settings.DOMAIN)
                return urlunparse(new_url).replace('//https', 'https')
            return url

        response.data['next'] = override_domain(response.data.get('next'))
        response.data['previous'] = override_domain(response.data.get('previous'))
        return response