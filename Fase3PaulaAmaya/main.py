
import tkinter as tk

from views.login_windows import LoginWindow
from views.affiliate_window import AffiliateApplication


# ==========================================
# STUDENT INFORMATION
# ==========================================

STUDENT_NAME = "Paula Amaya"
COURSE_NAME = "Estructura de Datos"
GROUP_NUMBER = "301305_132"


# ==========================================
# MAIN APPLICATION
# ==========================================

def open_affiliate_application(root):
    """
    Replaces the login interface with the main application.
    """

    for widget in root.winfo_children():
        widget.destroy()

    AffiliateApplication(root)


def main():
    """
    Initializes the application.
    """

    root = tk.Tk()

    LoginWindow(
        parent=root,
        on_success=lambda: open_affiliate_application(root),
        student_name=STUDENT_NAME,
        course_name=COURSE_NAME,
        group_number=GROUP_NUMBER
    )

    root.mainloop()


if __name__ == "__main__":
    main()
