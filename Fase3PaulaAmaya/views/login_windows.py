
import tkinter as tk
from tkinter import ttk, messagebox


class LoginWindow:
    """
    Handles the login interface and password validation.
    """

    def __init__(
        self,
        parent,
        on_success,
        student_name,
        course_name,
        group_number
    ):
        self.parent = parent
        self.on_success = on_success

        self.student_name = student_name
        self.course_name = course_name
        self.group_number = group_number

        self.password = "Caja"

        self.create_interface()

    def create_interface(self):
        """
        Creates the login interface.
        """
        self.parent.title("Login - Compensándote")
        self.parent.geometry("430x330")
        self.parent.resizable(False, False)

        main_frame = ttk.Frame(
            self.parent,
            padding=30
        )
        main_frame.pack(
            fill="both",
            expand=True
        )

        title_label = ttk.Label(
            main_frame,
            text="COMPENSÁNDOTE",
            font=("Arial", 20, "bold")
        )
        title_label.pack(pady=(10, 5))

        subtitle_label = ttk.Label(
            main_frame,
            text="Sistema de Control de Afiliados",
            font=("Arial", 10)
        )
        subtitle_label.pack(pady=(0, 25))

        password_label = ttk.Label(
            main_frame,
            text="Contraseña:"
        )
        password_label.pack(anchor="w")

        self.password_entry = ttk.Entry(
            main_frame,
            show="*",
            width=35
        )
        self.password_entry.pack(
            fill="x",
            pady=(5, 20)
        )

        self.password_entry.bind(
            "<Return>",
            lambda event: self.validate_login()
        )

        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill="x", pady=10)

        login_button = ttk.Button(
            button_frame,
            text="Ingresar",
            command=self.validate_login
        )
        login_button.pack(
            side="left",
            expand=True,
            fill="x",
            padx=5
        )

        exit_button = ttk.Button(
            button_frame,
            text="Salir",
            command=self.exit_application
        )
        exit_button.pack(
            side="left",
            expand=True,
            fill="x",
            padx=5
        )

        about_button = ttk.Button(
            main_frame,
            text="Acerca de",
            command=self.show_about
        )
        about_button.pack(pady=15)

        self.password_entry.focus_set()

    def validate_login(self):
        """
        Validates the entered password.
        """
        entered_password = self.password_entry.get()

        if entered_password == self.password:
            self.password_entry.delete(0, tk.END)

            self.parent.unbind_all("<Return>")

            self.on_success()

        else:
            messagebox.showerror(
                "Error de acceso",
                "La contraseña ingresada es incorrecta."
            )

            self.password_entry.delete(0, tk.END)
            self.password_entry.focus_set()

    def show_about(self):
        """
        Displays student and course information.
        """
        about_message = (
            f"Curso: {self.course_name}\n"
            f"Estudiante: {self.student_name}\n"
            f"Grupo colaborativo: {self.group_number}"
        )

        messagebox.showinfo(
            "Acerca de",
            about_message
        )

    def exit_application(self):
        """
        Closes the application.
        """
        self.parent.destroy()
