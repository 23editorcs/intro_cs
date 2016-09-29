# Song for 5 animals
# oldMcDonald.py

def main():
    oldMcDonald('cow', 'moo')
    oldMcDonald('pig', 'ec')    
    oldMcDonald('chicken', 'chip')
    oldMcDonald('goat', 'uhh')
    oldMcDonald('horse', 'hihi')

def oldMcDonald(animal, sound):
    print('Old McDonal had a farm, Ee-igh, Ee-igh, Oh! \n' \
          'And on that farm he had a {1}, Ee-igh, Ee-igh, Oh!\n' \
          'With a {0}, {0} here and a {0}, {0} there.\n' \
          'Here a {0}, there a {0}, everywhere a {0}, {0}.\n' \
          'Old McDonald had a farm, Ee-igh, Ee-igh, Oh!\n\n'.format(sound, animal))
main()
