from pygeocoder import Geocoder

endereco = 'avenida paulista, 100 Sao Paulo'
print(Geocoder('GoogleCloudAPIKey').geocode(endereco))
print(Geocoder('GoogleCloudAPIKey').geocode(endereco).postal_code)
print(Geocoder('GoogleCloudAPIKey').geocode(endereco).coordinates)
print(Geocoder('GoogleCloudAPIKey').reverse_geocode(-23.5709484, -46.644044))
