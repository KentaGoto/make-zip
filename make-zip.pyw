import shutil, glob, os, PySimpleGUI as sg

# Zip each folder.
def makeZip(dir):
    root_dir = dir
    root_dir = root_dir.strip('\"')
    root_dir = root_dir + '/*'

    for i in glob.glob(root_dir):
        if not os.path.isdir(i):
            continue
        
        shutil.make_archive(i, format='zip', root_dir=i)
    
    
if __name__ == '__main__':
    sg.theme('') # Random theme
    
    layout = [
        [sg.Text('Dir:'), sg.Input(key='-DIR-')],
        [sg.OK(), sg.Button('EXIT')]
    ]
    
    window = sg.Window('make-zip', layout)
    
    while True:
        event, values = window.read()
        # print(event)
        
        if event is None or event == 'EXIT':
            break
        
        if event == 'OK':
            root_dir = values["-DIR-"]
            
            if root_dir == '':
                sg.popup("Please enter a directory")
                continue
            
            makeZip(root_dir)
        
        sg.popup('Done!')
    
    window.close()