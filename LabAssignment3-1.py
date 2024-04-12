import OpenGL
import os
os.environ["PYOPENGL_PLATFORM"] = "glx"
import numpy as np
import glfw
import OpenGL.GL
from OpenGL.GL import *

M = np.array([[1.,0.,0.],[0.,1.,0.],[1.,1.,1.]])  # accumulation Matrix, global var


def translateX(dx):
    return np.array([
        [1, 0, dx],
        [0, 1, 0],
        [0, 0, 1]
    ])

# By default, positive angle -> counter clock wise rotation
def rotate_it_on_2D_plane(angle):
    theta = np.radians(angle)
    return np.array(
        [
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1],
        ]
    )

def render(T):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glLoadIdentity()
    glBegin(GL_LINES)
    glColor3ub(255,0,0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([1.,0.]))
    glColor3ub(0,255,0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([0.,1.]))
    glEnd()
    glBegin(GL_TRIANGLES)
    glColor3ub(255,255,255)
    glVertex2fv( (T @ np.array([.0, .5, 1.]))[:-1] )
    glVertex2fv( (T @ np.array([.0, .0, 1.]))[:-1] )
    glVertex2fv( (T @ np.array([.5, .0, 1.]))[:-1] )
    glEnd()


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def key_callback(window, key, scancode, action, mods):



    global M
    if key == glfw.KEY_Q or key == glfw.KEY_E or key == glfw.KEY_A or key == glfw.KEY_D:
        if action == glfw.PRESS:
            if key == glfw.KEY_Q:
                #M = M @ translateX(-0.1)   # potential problem exist <- this line
                M[0, 2] -= 0.1
            elif key == glfw.KEY_E:
                #M = M @ translateX(0.1)   # potential problem exist <- this line
                M[0, 2] += 0.1
            elif key == glfw.KEY_A:
                M = M @ rotate_it_on_2D_plane(10)
            else:                                # else block means -> key == KEY_D true condition!
                M = M @ rotate_it_on_2D_plane(-10)
        elif action == glfw.RELEASE:
            print('key released')
        elif action == glfw.REPEAT:
            print('key repeated')
    elif key == glfw.KEY_1:
        if action == glfw.PRESS:
            M = np.array([[1.,0.,0.],[0.,1.,0.],[1.,1.,1.]])
        elif action == glfw.RELEASE:
            print('reset released')
        elif action == glfw.REPEAT:
            print('reset repeated')
    else:
        return
        


def main():
    if not glfw.init():
        return
    window = glfw.create_window(480,480, "LabEx",None,None)
    
    if not window:
        glfw.terminate()
        return

    glfw.set_key_callback(window, key_callback)
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        global M
        T = M
        render(T)
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
