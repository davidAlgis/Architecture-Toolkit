#This script is called when blender is open
import bpy 

#is needed to open port at start
bpy.ops.wm.open_command_port()

#remove the view different from view_3d 
for window in bpy.context.window_manager.windows:
    screen = window.screen

    for area in screen.areas:
        if area.type == 'VIEW_3D':
            override = {'window': window, 'screen': screen, 'area': area}
            bpy.ops.screen.screen_full_area(override)
            break

#deletes all the default object in the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False, confirm=False)
