
import re
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import date

from tkcalendar import DateEntry

from models.affiliate import Affiliate
from structures.affiliate_data_structure import AffiliateDataStructure


class AffiliateApplication:

    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Caja Compensándote – Control de Afiliados")
        self.parent.geometry("1150x750")
        self.parent.minsize(1000, 650)

        self.affiliate_data = AffiliateDataStructure()

        self.create_variables()
        self.create_interface()
        self.calculate_fee()

    # --------------------------------------------------
    # VARIABLES
    # --------------------------------------------------

    def create_variables(self):
        self.id_type_var = tk.StringVar(value="CC")
        self.id_number_var = tk.StringVar()
        self.full_name_var = tk.StringVar()
        self.income_var = tk.StringVar()
        self.service_var = tk.StringVar(
            value="Subsidio de desempleo"
        )
        self.employment_type_var = tk.StringVar(
            value="Empleado"
        )
        self.fee_var = tk.StringVar(value="$0")
        self.structure_var = tk.StringVar(value="Pila")

    # --------------------------------------------------
    # MAIN INTERFACE
    # --------------------------------------------------

    def create_interface(self):

        title_label = ttk.Label(
            self.parent,
            text="Caja Compensándote – Control de Afiliados",
            font=("Arial", 18, "bold")
        )
        title_label.pack(pady=15)

        self.create_form()
        self.create_structure_selector()
        self.create_treeview()
        self.create_buttons()

    # --------------------------------------------------
    # AFFILIATE FORM
    # --------------------------------------------------

    def create_form(self):

        form_frame = ttk.LabelFrame(
            self.parent,
            text="Información del afiliado",
            padding=15
        )
        form_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # Identification type
        ttk.Label(
            form_frame,
            text="Tipo de identificación:"
        ).grid(row=0, column=0, sticky="w", padx=5, pady=5)

        id_type_combo = ttk.Combobox(
            form_frame,
            textvariable=self.id_type_var,
            values=["CC", "CE", "NUIP", "PAS"],
            state="readonly",
            width=18
        )
        id_type_combo.grid(
            row=0, column=1, sticky="w", padx=5, pady=5
        )

        # Identification number
        ttk.Label(
            form_frame,
            text="Número de identificación:"
        ).grid(row=0, column=2, sticky="w", padx=5, pady=5)

        id_entry = ttk.Entry(
            form_frame,
            textvariable=self.id_number_var,
            width=22
        )
        id_entry.grid(
            row=0, column=3, sticky="w", padx=5, pady=5
        )

        self.id_number_var.trace_add(
            "write",
            self.validate_id_input
        )

        # Full name
        ttk.Label(
            form_frame,
            text="Nombre completo:"
        ).grid(row=1, column=0, sticky="w", padx=5, pady=5)

        name_entry = ttk.Entry(
            form_frame,
            textvariable=self.full_name_var,
            width=25
        )
        name_entry.grid(
            row=1, column=1, sticky="w", padx=5, pady=5
        )

        # Current income
        ttk.Label(
            form_frame,
            text="Ingresos actuales:"
        ).grid(row=1, column=2, sticky="w", padx=5, pady=5)

        income_entry = ttk.Entry(
            form_frame,
            textvariable=self.income_var,
            width=22
        )
        income_entry.grid(
            row=1, column=3, sticky="w", padx=5, pady=5
        )

        self.income_var.trace_add(
            "write",
            self.calculate_fee_event
        )

        # Desired service
        ttk.Label(
            form_frame,
            text="Servicio solicitado:"
        ).grid(row=2, column=0, sticky="w", padx=5, pady=5)

        service_combo = ttk.Combobox(
            form_frame,
            textvariable=self.service_var,
            values=[
                "Subsidio de desempleo",
                "Ingreso a parque",
                "Curso de formación",
                "Paquete de viaje",
                "Medicina preventiva"
            ],
            state="readonly",
            width=23
        )
        service_combo.grid(
            row=2, column=1, sticky="w", padx=5, pady=5
        )
        service_combo.bind(
            "<<ComboboxSelected>>",
            self.calculate_fee_event
        )

        # Employment type
        ttk.Label(
            form_frame,
            text="Modalidad:"
        ).grid(row=2, column=2, sticky="w", padx=5, pady=5)

        employment_frame = ttk.Frame(form_frame)
        employment_frame.grid(
            row=2, column=3, sticky="w", padx=5, pady=5
        )

        ttk.Radiobutton(
            employment_frame,
            text="Empleado",
            variable=self.employment_type_var,
            value="Empleado",
            command=self.calculate_fee
        ).pack(side="left", padx=5)

        ttk.Radiobutton(
            employment_frame,
            text="Independiente",
            variable=self.employment_type_var,
            value="Independiente",
            command=self.calculate_fee
        ).pack(side="left", padx=5)

        # Membership fee
        ttk.Label(
            form_frame,
            text="Tarifa calculada:"
        ).grid(row=3, column=0, sticky="w", padx=5, pady=5)

        fee_entry = ttk.Entry(
            form_frame,
            textvariable=self.fee_var,
            state="readonly",
            width=20
        )
        fee_entry.grid(
            row=3, column=1, sticky="w", padx=5, pady=5
        )

        # Registration date
        ttk.Label(
            form_frame,
            text="Fecha de registro:"
        ).grid(row=3, column=2, sticky="w", padx=5, pady=5)

        self.registration_date = DateEntry(
            form_frame,
            width=19,
            date_pattern="dd/mm/yyyy"
        )
        self.registration_date.grid(
            row=3, column=3, sticky="w", padx=5, pady=5
        )

    # --------------------------------------------------
    # STRUCTURE SELECTOR
    # --------------------------------------------------

    def create_structure_selector(self):

        selector_frame = ttk.LabelFrame(
            self.parent,
            text="Estructura de datos",
            padding=10
        )
        selector_frame.pack(
            fill="x",
            padx=20,
            pady=5
        )

        ttk.Label(
            selector_frame,
            text="Seleccione la estructura:"
        ).pack(side="left", padx=10)

        structure_combo = ttk.Combobox(
            selector_frame,
            textvariable=self.structure_var,
            values=["Pila", "Cola", "Lista"],
            state="readonly",
            width=15
        )
        structure_combo.pack(side="left", padx=10)

        structure_combo.bind(
            "<<ComboboxSelected>>",
            self.refresh_treeview
        )

    # --------------------------------------------------
    # TREEVIEW
    # --------------------------------------------------

    def create_treeview(self):

        table_frame = ttk.LabelFrame(
            self.parent,
            text="Registros de afiliados",
            padding=10
        )
        table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        columns = (
            "id_type",
            "id_number",
            "full_name",
            "income",
            "service",
            "employment",
            "fee",
            "date"
        )

        self.treeview = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=12
        )

        headings = {
            "id_type": "Tipo ID",
            "id_number": "Número ID",
            "full_name": "Nombre completo",
            "income": "Ingresos",
            "service": "Servicio",
            "employment": "Modalidad",
            "fee": "Tarifa",
            "date": "Fecha"
        }

        widths = {
            "id_type": 75,
            "id_number": 110,
            "full_name": 180,
            "income": 110,
            "service": 180,
            "employment": 110,
            "fee": 100,
            "date": 100
        }

        for column in columns:
            self.treeview.heading(
                column,
                text=headings[column]
            )
            self.treeview.column(
                column,
                width=widths[column],
                anchor="center"
            )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.treeview.yview
        )

        self.treeview.configure(
            yscrollcommand=scrollbar.set
        )

        self.treeview.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

    # --------------------------------------------------
    # BUTTONS
    # --------------------------------------------------

    def create_buttons(self):

        button_frame = ttk.Frame(self.parent)
        button_frame.pack(pady=15)

        ttk.Button(
            button_frame,
            text="Registrar",
            command=self.register_affiliate
        ).pack(side="left", padx=7)

        ttk.Button(
            button_frame,
            text="Limpiar",
            command=self.clear_form
        ).pack(side="left", padx=7)

        ttk.Button(
            button_frame,
            text="Reporte",
            command=self.generate_report
        ).pack(side="left", padx=7)

        ttk.Button(
            button_frame,
            text="Eliminar",
            command=self.delete_affiliate
        ).pack(side="left", padx=7)

        ttk.Button(
            button_frame,
            text="Salir",
            command=self.exit_application
        ).pack(side="left", padx=7)

    # --------------------------------------------------
    # INPUT VALIDATION
    # --------------------------------------------------

    def validate_id_input(self, *args):

        value = self.id_number_var.get()

        if value and not value.isdigit():
            cleaned_value = "".join(
                character
                for character in value
                if character.isdigit()
            )
            self.id_number_var.set(cleaned_value)

    def validate_name(self, name):

        pattern = r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s'-]+$"

        return bool(re.fullmatch(pattern, name))

    # --------------------------------------------------
    # FEE CALCULATION
    # --------------------------------------------------

    def calculate_fee_event(self, event=None):
        self.calculate_fee()

    def calculate_fee(self):

        income_text = self.income_var.get()

        if not income_text.isdigit():
            self.fee_var.set("$0")
            return

        income = int(income_text)

        if income < 1000000:
            self.fee_var.set("$0")
            return

        employment_type = self.employment_type_var.get()

        if employment_type == "Empleado":

            if income < 2000000:
                base_fee = 45000
            elif income < 3000000:
                base_fee = 60000
            elif income < 4000000:
                base_fee = 75000
            elif income <= 5000000:
                base_fee = 90000
            else:
                base_fee = 150000

        else:

            if income < 2000000:
                base_fee = 10000
            elif income < 3000000:
                base_fee = 20000
            elif income < 4000000:
                base_fee = 30000
            elif income <= 5000000:
                base_fee = 40000
            else:
                base_fee = 80000

        service = self.service_var.get()

        if service == "Subsidio de desempleo":
            additional_fee = 0

        elif service == "Ingreso a parque":
            additional_fee = 2500

        elif service == "Curso de formación":
            additional_fee = 7500

        elif service == "Paquete de viaje":
            additional_fee = 10000

        elif service == "Medicina preventiva":
            additional_fee = income * 0.10

        else:
            additional_fee = 0

        total_fee = base_fee + additional_fee

        self.fee_var.set(
            f"${total_fee:,.0f}".replace(",", ".")
        )

    # --------------------------------------------------
    # REGISTER AFFILIATE
    # --------------------------------------------------

    def register_affiliate(self):

        id_type = self.id_type_var.get()
        id_number = self.id_number_var.get().strip()
        full_name = self.full_name_var.get().strip()
        income_text = self.income_var.get().strip()
        service = self.service_var.get()
        employment_type = self.employment_type_var.get()

        # Validate identification number
        if not id_number:
            messagebox.showwarning(
                "Validación",
                "Ingrese el número de identificación."
            )
            return

        if not id_number.isdigit():
            messagebox.showwarning(
                "Validación",
                "El número de identificación solo debe contener números."
            )
            return

        # Validate full name
        if not full_name:
            messagebox.showwarning(
                "Validación",
                "Ingrese el nombre completo del afiliado."
            )
            return

        if not self.validate_name(full_name):
            messagebox.showwarning(
                "Validación",
                "El nombre solo debe contener letras y espacios."
            )
            return

        # Validate income
        if not income_text:
            messagebox.showwarning(
                "Validación",
                "Ingrese los ingresos actuales."
            )
            return

        if not income_text.isdigit():
            messagebox.showwarning(
                "Validación",
                "Los ingresos deben contener únicamente números."
            )
            return

        income = int(income_text)

        if income < 1000000:
            messagebox.showwarning(
                "Validación",
                "Los ingresos deben ser iguales o superiores a $1.000.000."
            )
            return

        if not service:
            messagebox.showwarning(
                "Validación",
                "Seleccione un servicio."
            )
            return

        # Calculate final fee
        self.calculate_fee()

        fee_text = self.fee_var.get()
        fee = int(
            fee_text.replace("$", "").replace(".", "").replace(",", "")
        )

        registration_date = self.registration_date.get()

        # Check duplicate identification in selected structure
        if self.affiliate_data.affiliate_exists(
            id_number,
            self.structure_var.get()
        ):
            messagebox.showwarning(
                "Registro duplicado",
                "Ya existe un afiliado con ese número de identificación en la estructura seleccionada."
            )
            return

        # Create affiliate object
        affiliate = Affiliate(
            id_type=id_type,
            id_number=id_number,
            full_name=full_name,
            current_income=income,
            desired_service=service,
            employment_type=employment_type,
            membership_fee=fee,
            registration_date=registration_date
        )

        # Store according to selected data structure
        selected_structure = self.structure_var.get()

        if selected_structure == "Pila":
            self.affiliate_data.push_affiliate(affiliate)

        elif selected_structure == "Cola":
            self.affiliate_data.enqueue_affiliate(affiliate)

        elif selected_structure == "Lista":
            self.affiliate_data.add_to_list(affiliate)

        messagebox.showinfo(
            "Registro exitoso",
            "El afiliado fue registrado correctamente."
        )

        self.refresh_treeview()
        self.clear_form()

    # --------------------------------------------------
    # REFRESH TREEVIEW
    # --------------------------------------------------

    def refresh_treeview(self, event=None):

        for item in self.treeview.get_children():
            self.treeview.delete(item)

        selected_structure = self.structure_var.get()

        if selected_structure == "Pila":
            affiliates = self.affiliate_data.get_stack()

        elif selected_structure == "Cola":
            affiliates = self.affiliate_data.get_queue()

        else:
            affiliates = self.affiliate_data.get_list()

        for affiliate in affiliates:

            self.treeview.insert(
                "",
                "end",
                values=(
                    affiliate.id_type,
                    affiliate.id_number,
                    affiliate.full_name,
                    f"${affiliate.current_income:,.0f}".replace(",", "."),
                    affiliate.desired_service,
                    affiliate.employment_type,
                    f"${affiliate.membership_fee:,.0f}".replace(",", "."),
                    affiliate.registration_date
                )
            )

    # --------------------------------------------------
    # CLEAR FORM
    # --------------------------------------------------

    def clear_form(self):

        self.id_type_var.set("CC")
        self.id_number_var.set("")
        self.full_name_var.set("")
        self.income_var.set("")
        self.service_var.set("Subsidio de desempleo")
        self.employment_type_var.set("Empleado")
        self.fee_var.set("$0")

        # Reset date to current date
        self.registration_date.set_date(date.today())

    # --------------------------------------------------
    # REPORTS
    # --------------------------------------------------

    def generate_report(self):

        selected_structure = self.structure_var.get()

        if selected_structure == "Pila":

            total = self.affiliate_data.get_stack_fee_total()

            messagebox.showinfo(
                "Reporte de Pila",
                f"La suma total de las tarifas registradas es:\n${total:,.0f}".replace(",", ".")
            )

        elif selected_structure == "Cola":

            total = self.affiliate_data.get_queue_count()

            messagebox.showinfo(
                "Reporte de Cola",
                f"La cantidad de afiliados registrados es: {total}"
            )

        elif selected_structure == "Lista":

            average = self.affiliate_data.get_list_income_average()

            messagebox.showinfo(
                "Reporte de Lista",
                f"El promedio de ingresos de los afiliados es:\n${average:,.0f}".replace(",", ".")
            )

    # --------------------------------------------------
    # DELETE AFFILIATE
    # --------------------------------------------------

    def delete_affiliate(self):

        selected_structure = self.structure_var.get()

        if selected_structure == "Pila":

            affiliates = self.affiliate_data.get_stack()

            if not affiliates:
                messagebox.showwarning(
                    "Eliminar",
                    "La pila está vacía."
                )
                return

            affiliate = affiliates[0]

            confirmation = messagebox.askyesno(
                "Confirmar eliminación",
                f"¿Desea desapilar al afiliado {affiliate.full_name}?"
            )

            if confirmation:
                self.affiliate_data.pop_affiliate()

                messagebox.showinfo(
                    "Eliminación",
                    "El último afiliado registrado fue eliminado de la pila."
                )

        elif selected_structure == "Cola":

            affiliates = self.affiliate_data.get_queue()

            if not affiliates:
                messagebox.showwarning(
                    "Eliminar",
                    "La cola está vacía."
                )
                return

            affiliate = affiliates[0]

            confirmation = messagebox.askyesno(
                "Confirmar eliminación",
                f"¿Desea desencolar al afiliado {affiliate.full_name}?"
            )

            if confirmation:
                self.affiliate_data.dequeue_affiliate()

                messagebox.showinfo(
                    "Eliminación",
                    "El primer afiliado registrado fue eliminado de la cola."
                )

        elif selected_structure == "Lista":

            affiliates = self.affiliate_data.get_list()

            if not affiliates:
                messagebox.showwarning(
                    "Eliminar",
                    "La lista está vacía."
                )
                return

            id_number = simpledialog.askstring(
                "Eliminar afiliado",
                "Ingrese el número de identificación del afiliado que desea eliminar:"
            )

            if id_number is None:
                return

            if not id_number.strip():
                messagebox.showwarning(
                    "Validación",
                    "Debe ingresar un número de identificación."
                )
                return

            affiliate = self.affiliate_data.find_in_list(
                id_number.strip()
            )

            if affiliate is None:
                messagebox.showwarning(
                    "No encontrado",
                    "No existe un afiliado con ese número de identificación."
                )
                return

            confirmation = messagebox.askyesno(
                "Confirmar eliminación",
                f"¿Está seguro de eliminar al afiliado {affiliate.full_name}?"
            )

            if confirmation:
                self.affiliate_data.remove_from_list(
                    id_number.strip()
                )

                messagebox.showinfo(
                    "Eliminación",
                    "El afiliado fue eliminado correctamente de la lista."
                )

        self.refresh_treeview()

    # --------------------------------------------------
    # EXIT APPLICATION
    # --------------------------------------------------

    def exit_application(self):

        confirmation = messagebox.askyesno(
            "Salir",
            "¿Está seguro de que desea salir de la aplicación?"
        )

        if confirmation:
            self.parent.destroy()
