
class FilterIPMiddleware(object):

    # Check if client IP is allowed
    def process_request(self, request):
        allowed_ips = ['192.168.1.1', '127.0.0.1']  # Authorized ip's
        ip = request.META.get('REMOTE_ADDR')  # Get client IP
        print "REMOTE_ADDR=", ip
        if ip not in allowed_ips:
            # raise Http403 # If user is not allowed raise Error
            print "Error!!!"
        # If IP is allowed we don't do anything
        return None