from pygeocoder import Geocoder

endereco = '1222, Lins de Vasconcelos, Sao Paulo, SP'
print(Geocoder('GoogleCloudAPIKey').geocode(endereco).coordinates)
