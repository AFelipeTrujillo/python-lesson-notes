planets = {'Mars', 'Jupiter', 'Venus'}
print(planets)
print(len(planets))
print('Mars' in planets)
planets.add('Earth')
print(f'Set content {planets}')
planets.add('Earth')
print(f'Set content {planets}')
planets.remove('Earth')
print(f'Set content {planets}')
planets.discard('Earth')
planets.clear()
print(f'Set content {planets}')
del planets
