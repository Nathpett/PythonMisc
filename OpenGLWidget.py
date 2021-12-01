from PyQt5.QtWidgets import QMainWindow, QOpenGLWidget, QApplication
from PyQt5.QtCore import QTimer
from OpenGL.GL import glEnable, glMatrixMode, glClear, glClearColor, glColor3f, glBegin, glVertex3f, glEnd, GL_PROJECTION, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_LINE_STRIP
import sys

#Learning PyOpenGL and QOpenGLWidget, this is adapted code from https://www.youtube.com/watch?v=BMIHU54PsaE

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.openglwidget = OpenGLWidget(self)
        self.setCentralWidget(self.openglwidget)
        self.setWindowTitle("Test OpenGLWidget")
        self.setGeometry(200, 200, 200, 200)

class OpenGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(0)

    def paintGL(self):
        glMatrixMode(GL_PROJECTION)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glColor3f(1.0, 0.0, 0.0)
        for i in range(10):
            glBegin(GL_LINE_STRIP)
            glVertex3f(-1.0, i/10, 0.0)
            glVertex3f(1.0, -i/10, 0.0)
            glEnd()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())