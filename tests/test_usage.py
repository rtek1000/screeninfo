import screeninfo

dict1 = get_screen()
print('width:', dict1.get('width'))

# screeninfo.get_monitors() sample:
# [Monitor(x=0, y=0, width=1920, height=1080, width_mm=309, height_mm=174, name='\\\\.\\DISPLAY1', is_primary=True), Monitor(x=1920, y=0, width=1366, height=768, width_mm=256, height_mm=144, name='\\\\.\\DISPLAY2', is_primary=False)]    
def get_screen(is_primary=True):
    for m1 in screeninfo.get_monitors():
        dict1 = m1.__dict__
        print(dict1)
        if is_primary == True and dict1.get('is_primary') == True:
            return dict1
        elif is_primary == False and dict1.get('is_primary') == False:
            return dict1
    dict0 = dict({'width': 0, 'height': 0})
    return dict0 
