import OpenGL
import os
os.environ["PYOPENGL_PLATFORM"] = "glx"
import numpy as np
import glfw
import OpenGL.GL
from OpenGL.GL import *


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
    primitive = {glfw.KEY_1: GL_POINTS,
            glfw.KEY_2: GL_LINES, 
            glfw.KEY_3: GL_LINE_STRIP, 
            glfw.KEY_4: GL_LINE_LOOP, 
            glfw.KEY_5: GL_TRIANGLES, 
            glfw.KEY_6: GL_TRIANGLE_STRIP, 
            glfw.KEY_7: GL_TRIANGLE_FAN, 
            glfw.KEY_8: GL_QUADS, 
            glfw.KEY_9: GL_QUAD_STRIP, 
            glfw.KEY_0: GL_POLYGON}

    ppppprimnew = {glfw.KEY_Q: GL_LINES,
            glfw.KEY_E: GL_LINES,
            glfw.KEY_A: GL_LINES,
            glfw.KEY_D: GL_LINES}

    if key >= glfw.KEY_0 and key <= glfw.KEY_9:
        if action == glfw.PRESS:
            val = primitive[key]
        elif action == glfw.RELEASE:
            print('digitkey released')
        elif action == glfw.REPEAT:
            print('digitkey repeated')

    if key == glfw.KEY_Q or key == glfw.KEY_E or key == glfw.KEY_A or key == glfw.KEY_D:
        if action == glfw.PRESS:
            print('')
        elif action == glfw.RELEASE:
            print('charkey released')
        elif action == glfw.REPEAT:
            print('charkey repeated')




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
        T = np.array([[1.,0.,0.],[0.,1.,0.],[1.,1.,1.]])

        render(T)
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
