import glfw
from OpenGL.GL import * 
from OpenGL.GLU import *
import numpy as np
import pdb
def drawUnitCube():
    glBegin(GL_QUADS)
    glVertex3f( 0.5, 0.5,-0.5)
    glVertex3f(-0.5, 0.5,-0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f( 0.5, 0.5, 0.5) 
                             
    glVertex3f( 0.5,-0.5, 0.5)
    glVertex3f(-0.5,-0.5, 0.5)
    glVertex3f(-0.5,-0.5,-0.5)
    glVertex3f( 0.5,-0.5,-0.5) 
                             
    glVertex3f( 0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5,-0.5, 0.5)
    glVertex3f( 0.5,-0.5, 0.5)
                             
    glVertex3f( 0.5,-0.5,-0.5)
    glVertex3f(-0.5,-0.5,-0.5)
    glVertex3f(-0.5, 0.5,-0.5)
    glVertex3f( 0.5, 0.5,-0.5)
 
    glVertex3f(-0.5, 0.5, 0.5) 
    glVertex3f(-0.5, 0.5,-0.5)
    glVertex3f(-0.5,-0.5,-0.5) 
    glVertex3f(-0.5,-0.5, 0.5) 
                             
    glVertex3f( 0.5, 0.5,-0.5) 
    glVertex3f( 0.5, 0.5, 0.5)
    glVertex3f( 0.5,-0.5, 0.5)
    glVertex3f( 0.5,-0.5,-0.5)
    glEnd()

def drawCubeArray():
    for i in range(5):
        for j in range(5):
            for k in range(5):
                glPushMatrix()
                glTranslatef(i,j,-k-1)
                glScalef(.5,.5,.5)
                drawUnitCube()
                glPopMatrix()

def drawFrame():
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(np.array([1.,0.,0.]))
    glColor3ub(0, 255, 0)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(np.array([0.,1.,0.]))
    glColor3ub(0, 0, 255)
    glVertex3fv(np.array([0.,0.,0]))
    glVertex3fv(np.array([0.,0.,1.]))
    glEnd()

def key_callback(window, key, scancode, action, mods):
    pass

def render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode( GL_FRONT_AND_BACK, GL_LINE )
    glLoadIdentity()

    glOrtho(-5,5, -5,5, -8,8)
    #gluLookAt(5,3,5,    1,1,-1,     0,1,0) # <-.. removed soon

    # skeleton -> goal -> change and set func call parameter values properly.
    #glRotatef(0,0,0,0) # (ang, x, y, z) params
    #glRotatef(0,0,0,0)
    #glTranslatef(0,0,0) # (x, y, z) params

    # draft-written code: beta version
    glTranslatef(-1,-1,-2)
    glRotatef(-30,0,1,0)
    glRotatef(30,1,0,0)
    glRotatef(-10,1,0,0)
    glRotatef(-11,0,0,1)
    # end of draft beta code. Also backup at github is completed.


    drawFrame()

    glColor3ub(255, 255, 255)
    drawCubeArray()

def main():
    if not glfw.init():
        return
    window = glfw.create_window(640,640, "3D Trans", None,None)
    if not window: 
        glfw.terminate() 
        return
    glfw.make_context_current(window) 
    glfw.set_key_callback(window, key_callback)
    glfw.swap_interval(1)
    while not glfw.window_should_close(window): 
        glfw.poll_events()
        t = glfw.get_time()
        render()


        glfw.swap_buffers(window) 
    glfw.terminate()

if __name__ == "__main__": 
    main()
