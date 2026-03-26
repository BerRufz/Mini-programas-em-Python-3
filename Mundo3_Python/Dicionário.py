pessoas = {'nome': 'Bernardo', 'gênero':  'Masculino', 'idade': 19}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

del pessoas['gênero']
pessoas['peso'] = 89
for k, v in pessoas.items():
    print(f'{k} = {v}')