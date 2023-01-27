from pygeocoder import Geocoder

endereco = 'avenida paulista, 100 Sao Paulo'
print(Geocoder('AIzaSyANRBN8b4VZm6K1qdRpsruGji4FnKBjyj4').geocode(endereco))
print(Geocoder('AIzaSyANRBN8b4VZm6K1qdRpsruGji4FnKBjyj4').geocode(endereco).postal_code)
print(Geocoder('AIzaSyANRBN8b4VZm6K1qdRpsruGji4FnKBjyj4').geocode(endereco).coordinates)
print(Geocoder('AIzaSyANRBN8b4VZm6K1qdRpsruGji4FnKBjyj4').reverse_geocode(-23.5709484, -46.644044))
