usuarios = {}
print(usuarios)

usuarios = {"Chaves": ["Chaves do 8", "24/12/2017", "Recepção 01"],
            "Quico": ["Quico das Flores", "20/12/2017", "Raio X 03"]
            }
print(usuarios)

usuarios["Florinda"] = ["Dona FLorinda", "24/12/2017", "Raio X 01"]
print(usuarios)

print("--------------")
print(usuarios.get("Quico"))