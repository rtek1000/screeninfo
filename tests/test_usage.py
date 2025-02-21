import screeninfo

dict1 = get_screen()
print('width:', dict1.get('width'))

def get_screen(is_primary=True):
    for m1 in screeninfo.get_monitors():
        d1 = m1.__dict__
        print(d1)
        if d1.get('is_primary') == True:
            print("Screen 0: ", int(d1.get('width')), "x", int(d1.get('height')))
            return d1
