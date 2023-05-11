from django.utils import timezone

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from datetime import timedelta

# Bearer token to be used for authentication
BEARER_TOKEN = 'mf8nrqICaHYD1y8wRMBksWm7U7gLgXy1mSWjhI0q'

# Keep track of number of attempts made by IP
ip_attempts = {}

# Keep track of the time when the IP is allowed to access again
ip_access_times = {}


@api_view(['GET'])
def my_api_view(request):
    """
    API view that authenticates using a bearer token and blocks requests based on rate limiting and DDoS protection.
    """
    # Check if the authorization header contains the bearer token
    auth_header = request.META.get('HTTP_AUTHORIZATION')

    if not auth_header:
    	return Response({'error': '"Bearer token is missing.'}, status=400)

    if not auth_header.startswith('Bearer '):
        return Response({'error': 'Bearer token is missing or invalid.'}, status=400)
    token = auth_header.split(' ')[1]
    
    if token != BEARER_TOKEN:
        return Response({'error': 'Bearer token is missing or invalid.'}, status=400)

    # Get the IP address from the request
    ip_address = request.META.get('REMOTE_ADDR')


    # Check if the IP has exceeded the maximum number of attempts in a minute
    if ip_address in ip_attempts and ip_attempts[ip_address] >= 100:
        return Response({'error': 'IP is blocked permanently.'}, status=400)

    # Check if the IP has exceeded the maximum number of attempts in 20 seconds
    if ip_address in ip_attempts and ip_attempts[ip_address] >= 10:
        # Check if the IP is still blocked for DDoS protection
        if ip_address in ip_access_times and timezone.now() < ip_access_times[ip_address]:
            return Response({'error': 'IP is blocked for DDoS protection.'}, status=400)
        # If the IP is no longer blocked, reset the number of attempts
        else:
            del ip_attempts[ip_address]

    data = {
   		"id":"18th Floor",
   		"first_name":"Angoon Seaplane Base",
   		"last_name":"com.blogger.Flexidy",
   		"email":"bcapron9@dagondesign.com",
	}  

    # Generate some random data for the response
    response_data = {'message': 'Success!', 'data': data}

    # Increment the number of attempts for the IP
    if ip_address in ip_attempts:
        ip_attempts[ip_address] += 1
    else:
        ip_attempts[ip_address] = 1

    # Set the time when the IP will be allowed to access again
    if ip_address not in ip_access_times:
        ip_access_times[ip_address] = timezone.now() + timedelta(minutes=20)
    
    # Return the response
    return Response(response_data, status=200)
