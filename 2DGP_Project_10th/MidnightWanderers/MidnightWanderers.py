import platform
import os

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

import Game_Framework
import Start_State
import Main_State

Game_Framework.run(Start_State)
#Game_Framework.run(Main_State)
