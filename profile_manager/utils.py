from contextlib import contextmanager

from qgis.PyQt.QtCore import QCoreApplication, Qt
from qgis.PyQt.QtGui import QCursor, QGuiApplication


@contextmanager
def wait_cursor():
    try:
        QGuiApplication.setOverrideCursor(QCursor(Qt.CursorShape.WaitCursor))
        yield
    finally:
        QGuiApplication.restoreOverrideCursor()


def tr(self, message: str) -> str:
    """Get the translation for a string using Qt translation API.

    :param message: string to be translated.
    :type message: str

    :returns: Translated version of message.
    :rtype: str
    """
    return QCoreApplication.translate(self.__class__.__name__, message)
