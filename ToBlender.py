import socket

class ToBlender(object):

    def send_command(command):
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect(('localhost', 5000))
        clientsocket.sendall(command.encode())
        while True:
            res = clientsocket.recv(4096)
            if not res:
                break
            print(res.decode())
        clientsocket.close()

    

    def testAddCube():
        ToBlender.send_command("""bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))""")

    


