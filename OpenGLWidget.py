from PyQt5.QtWidgets import QMainWindow, QOpenGLWidget, QApplication
from PyQt5.QtCore import QTimer
from OpenGL.GL import glEnable, glMatrixMode, glClear, glClearColor, glColor3f, glBegin, glVertex3f, glEnd, GL_PROJECTION, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_LINE_STRIP, GL_POLYGON
import sys

class MainWindow(QMainWindow):
    def __init__(self, parent=None, map=None):
        QMainWindow.__init__(self, parent)
        self.openglwidget = OpenGLWidget(self)
        self.setCentralWidget(self.openglwidget)
        self.setWindowTitle("Test OpenGLWidget")
        self.setGeometry(200, 200, 200, 200)
        if map:
            self._map = map
        else:
            self._map = None


class OpenGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setGeometry(-parent.frameGeometry().width(), 0, parent.frameGeometry().width() * 2, parent.frameGeometry().height() * 2)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1)
        self._map = None

    def paintGL(self):
        glMatrixMode(GL_PROJECTION)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glColor3f(1.0, 1.0, 1.0)
        DIAMOND_RADIUS = 0.02
        for street_coord, street in self._map.get_graph().items():
            vec1, vec2 = street_coord
            glBegin(GL_LINE_STRIP)
            x, y = vec1
            x2, y2 = vec2
            glVertex3f(x, y, 0.0)
            glVertex3f(x2, y2, 0.0)
            glEnd()

            if x == x2:
                for building in street.buildings:
                    glBegin(GL_POLYGON)
                    yc = y + building.point_on_street
                    glVertex3f(x + DIAMOND_RADIUS, yc, 0.0)
                    glVertex3f(x, yc - DIAMOND_RADIUS, 0.0)
                    glVertex3f(x - DIAMOND_RADIUS, yc, 0.0)
                    glVertex3f(x, yc + DIAMOND_RADIUS, 0.0)
                    glEnd()
            else:
                for building in street.buildings:
                    glBegin(GL_POLYGON)
                    xc = x + building.point_on_street
                    glVertex3f(xc + DIAMOND_RADIUS, y, 0.0)
                    glVertex3f(xc, y - DIAMOND_RADIUS, 0.0)
                    glVertex3f(xc - DIAMOND_RADIUS, y, 0.0)
                    glVertex3f(xc, y + DIAMOND_RADIUS, 0.0)
                    glEnd()



    def set_map(self, map):
        self._map = map


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
