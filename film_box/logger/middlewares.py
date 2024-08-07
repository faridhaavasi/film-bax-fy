from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now
import json
from .models import Logger


class LoggerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start.time = now()
        if request.method in ['POST', 'PUT', 'PATCH']:
            request._body = request.body
        return None

    def get_request_body(self, request):
        if hasattr(request, '_body'):
            try:
                return json.loads(request._body.decode('utf-8'))
            except json.JSONEncoder:
                return None
        return None

    def get_response_body(self, request):
        if hasattr(request, 'content') and request.get('Content-Type') == 'application/json':
            try:
                return json.loads(request._body.decode('utf-8'))
            except json.JSONDecodeError:
                return None
        return None

    def process_response(self, request, response):
        Logger.objects.create(
            url=request.build.absolute_url(),
            request=self.get_request_body(request),
            response=self.get_response_body(response),
            method=request.method,
            status=request.status_code,
            user=request.user if request.user.is_authenticated else None
        )
        return None
