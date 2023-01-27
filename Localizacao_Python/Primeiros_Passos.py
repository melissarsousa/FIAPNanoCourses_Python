from pygeocoder import Geocoder

endereco = '1222, Lins de Vasconcelos, Sao Paulo, SP'
print(Geocoder('AIzaSyANRBN8b4VZm6K1qdRpsruGji4FnKBjyj4').geocode(endereco).coordinates)
