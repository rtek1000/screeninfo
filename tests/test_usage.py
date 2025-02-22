import screeninfo

dict1 = get_screen()
print('width:', dict1.get('width'))

# screeninfo.get_monitors() sample:
# [Monitor(x=0, y=0, width=1920, height=1080, width_mm=309, height_mm=174, name='\\\\.\\DISPLAY1', is_primary=True), Monitor(x=1920, y=0, width=1366, height=768, width_mm=256, height_mm=144, name='\\\\.\\DISPLAY2', is_primary=False)]    
def get_screen(is_primary=True):
    if len(screeninfo.get_monitors()) >= 2:
        mon0 = screeninfo.get_monitors()[0]
        mon1 = screeninfo.get_monitors()[1]
        dict1 = mon0.__dict__
        dict2 = mon1.__dict__
        if is_primary == True and dict1.get('is_primary') == True:
            print(dict1)
            return dict1 # the primary screen
        elif is_primary == True and dict2.get('is_primary') == True:
            print(dict2)
            return dict2 # the primary screen
        elif is_primary == False and dict1.get('is_primary') == False:
            print(dict1)
            return dict1 # the secondary screen
        elif is_primary == False and dict2.get('is_primary') == False:
            print(dict2)
            return dict2 # the secondary screen
        else:
            dict0 = dict({'width': 0, 'height': 0})
        return dict0 # does not have two or more monitors
    else:
        dict0 = dict({'width': 0, 'height': 0})
        return dict0 # does not have two or more monitors
