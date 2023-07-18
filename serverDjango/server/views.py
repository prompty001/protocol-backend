from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer

import jwt, datetime
from .models import User

from server.codes.aleatoryCode import totpGenerator, emailSender, validateTotp
from server.codes.getPK import getPrivKey

from django.contrib.auth import authenticate, login, logout

from importlib import import_module
from django.conf import settings

#SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
#from django.contrib.sessions.models import Session


class Home(APIView):
    def __str__(self) -> str:
        #return HttpResponse(totpGenerator())
        return HttpResponse(":)))")
    

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        emailSender()

        serializer.save()
        print('user salvo')

        return Response(serializer.data)


#     email = request.POST['email']
#     password = request.POST['password']

#     print(email, password)
    
#     user = authenticate(email=email, password=password)
    
    
#     """if user:
#         print("seila")
#         #sessionInstance.create()

#     return HttpResponse(f"{s.session_key}, {s.get_decoded()}")"""
    

#     if user:
#         login(request, user)
#         return HttpResponse("logado")

#     return HttpResponse("oi")

# def LogoutTest(request):
#     logout(request)
#     return HttpResponse("Logout bem sucedido.")

# def UserTest(request):
#     token = request.COOKIES.get('sessionid')

#     if token is not None:
#         return HttpResponse(f"Session ID: {token}")

#     return HttpResponse("Usuário não logado.")


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        androidIdLogin = request.data['androidIdLogin']
    
        user = User.objects.filter(email=email).first()

        if user is None:
            print('user not found')
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            print('Incorrect password')
            raise AuthenticationFailed('Incorrect Password!')
        
        if user.androidId != androidIdLogin:
            print('Device not found!')
            raise AuthenticationFailed('Device not found!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30), 
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, getPrivKey(), algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True) #secure=True
        response.data = {
            'jwt': token,
        }

        return response


class UserView(APIView):
    def get(self, request):
        userToken = request.COOKIES.get('jwt')

        if not userToken:
            raise AuthenticationFailed('Usuário não autenticado.')

        try:
            payload = jwt.decode(userToken, getPrivKey(), algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expirado.')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        userToken = request.COOKIES.get('jwt', None)

        if userToken:
            response = Response()
            response.delete_cookie('jwt')
            response.data = {
                'message': 'Logout bem sucedido.'
            }

            return response

        response = Response()
        response.data = {
            'message': 'Usuário já não está logado.'
        }

        return response
        

class ValidateCodeView(APIView):
    def post(self, request):
        code = request.data['token']

        codeCheck = validateTotp(code)

        print("codigo = ", code)

        if codeCheck is True:
            print("O token é válido.")

            return Response({
            'message': 'Code matches.'
        })

        return Response({
            'message': 'Code doesn\'t match.'
        })


"""def formValidation(request):

    formulario = RegistrationForm(request.POST)

    if formulario.is_valid():
        email = request.POST['email']
        cpf = request.POST['cpf']

        userEmailExist = User.objects.filter(email=email).first()
        userCpfExist = User.objects.filter(cpf=cpf).first()
        #guidExist
        #androidIdExist

        if userEmailExist or userCpfExist:
            print("já existe um usuário com esse email ou cpf cadastrado")
            return HttpResponse("erro")

        else:
            emailSender()

            global val
            def val(): 
                return formulario.save()

    else:
        print("formulario invalido")
        return HttpResponse("form invalido")

    return HttpResponse('erro interno do sistema')
"""

