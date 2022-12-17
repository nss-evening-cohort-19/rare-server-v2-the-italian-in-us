from rareapi.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated Gamer

    Method arguments:
      request -- The full HTTP request object
    '''
  
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    try:
        user = User.objects.get(uid=uid)

    # If authentication was successful, respond with their token
        data = {
            'id': user.id,
            'uid': user.uid,
            'bio': user.bio
        }
        return Response(data)
    except:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new gamer for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Now save the user info in the gamerraterapi_gamer table
    user = User.objects.create(
        bio=request.data['bio'],
        uid=request.data['uid'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        profile_image_url = request.data['profile_image_url'],
        email = request.data['email'],
        created_on = request.data['created_on'],
        active = True,
        is_staff = False
    )

    # Return the gamer info to the client
    data = {
            'id': user.id,
            'uid': user.uid,
            'bio': user.bio
    }
    return Response(data)
