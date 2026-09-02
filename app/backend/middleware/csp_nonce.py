import base64
import os


class ContentSecurityPolicyNonceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        random_base64_string = base64.b64encode(os.urandom(16)).decode("utf-8")
        request.csp_nonce = random_base64_string
        response = self.get_response(request)
        content_security_policy = (
            f"default-src 'self'; "
            f"script-src 'self' 'nonce-{random_base64_string}'; "
            f"style-src 'self' 'nonce-{random_base64_string}'; "
            f"style-src-elem 'self' 'nonce-{random_base64_string}'; "
            f"frame-ancestors 'self'; "
            f"form-action 'self';"
        )
        response["Content-Security-Policy"] = content_security_policy
        return response
