This project contains user register, login, profile add and profile update
Here is the following end points

    1. User register:
        method : POST
        http://127.0.0.1:8000/user_app/user-register/

    2. User login and it returns a access token
        method : POST
        http://127.0.0.1:8000/user_app/api/token/
    3. User profile creation 
        method : POST
        token : Bearer Token
        http://127.0.0.1:8000/user_profile/user-profile/
    4. User profile update
        method : PATCH
        token : Bearer Token
        http://127.0.0.1:8000/user_profile/user-profile-update/