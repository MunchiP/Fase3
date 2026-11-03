
# DATA ABSTRACTION TABLE

**Student Name:** Paula Amaya

**Problem Statement:**

Develop a desktop application for the family compensation fund
"Compensándote" to manage affiliate registrations using linear
data structures (stacks, queues and lists), object-oriented
programming and a graphical user interface in Python.

## 1. Class: Affiliate

**Visibility:** Public

**Attributes:**

| Attribute | Data Type |
|---|---|
| id_type | str |
| id_number | str |
| full_name | str |
| current_income | float |
| desired_service | str |
| employment_type | str |
| membership_fee | float |
| registration_date | str |

**Data Structure:** None.

**Methods:**

| Method | Description |
|---|---|
| __init__() | Initializes the affiliate attributes. |
| get_details() | Returns all affiliate information. |
| __str__() | Returns a textual representation of the affiliate. |

## 2. Class: AffiliateDataStructure

**Visibility:** Public

**Attributes:**

| Attribute | Data Type |
|---|---|
| stack | deque |
| queue | deque |
| affiliate_list | list |

**Data Structures:** Stack, Queue and List.

**Methods:**

| Method | Description |
|---|---|
| __init__() | Initializes the three data structures. |
| push_affiliate() | Adds an affiliate to the stack. |
| pop_affiliate() | Removes the last affiliate from the stack. |
| get_stack() | Returns stack records. |
| get_stack_fee_total() | Calculates the total membership fees. |
| enqueue_affiliate() | Adds an affiliate to the queue. |
| dequeue_affiliate() | Removes the first affiliate from the queue. |
| get_queue() | Returns queue records. |
| get_queue_count() | Counts queue records. |
| add_to_list() | Adds an affiliate to the list. |
| remove_from_list() | Removes an affiliate by identification number. |
| find_in_list() | Searches for an affiliate by identification number. |
| get_list() | Returns list records. |
| get_list_income_average() | Calculates the average income. |
| affiliate_exists() | Checks for duplicate identification numbers. |
| get_records() | Returns records from the selected structure. |
| get_report() | Generates the corresponding structure report. |

## 3. Class: LoginWindow

**Visibility:** Public

**Attributes:**

| Attribute | Data Type |
|---|---|
| parent | tk.Tk |
| on_success | Callable |
| student_name | str |
| course_name | str |
| group_number | str |
| password | str |

**Data Structure:** None.

**Methods:**

| Method | Description |
|---|---|
| __init__() | Initializes login information. |
| create_interface() | Builds the login form. |
| validate_login() | Validates the password. |
| show_about() | Displays student information. |
| exit_application() | Closes the application. |

## 4. Class: AffiliateApplication

**Visibility:** Public

**Attributes:**

| Attribute | Data Type |
|---|---|
| parent | tk.Tk |
| affiliate_data | AffiliateDataStructure |
| id_types | list |
| services | list |
| employment_types | list |
| structures | list |
| id_type_var | tk.StringVar |
| id_number_var | tk.StringVar |
| full_name_var | tk.StringVar |
| current_income_var | tk.StringVar |
| desired_service_var | tk.StringVar |
| employment_type_var | tk.StringVar |
| membership_fee_var | tk.StringVar |
| selected_structure_var | tk.StringVar |
| report_var | tk.StringVar |
| treeview | ttk.Treeview |

**Data Structures:** Stack, Queue and List.

**Methods:**

| Method | Description |
|---|---|
| __init__() | Initializes the application. |
| create_variables() | Initializes interface variables. |
| create_interface() | Builds the main interface. |
| create_form() | Creates affiliate input fields. |
| create_structure_selector() | Creates the structure selector. |
| create_treeview() | Creates the affiliate table. |
| create_report_section() | Creates the report field. |
| create_action_buttons() | Creates action buttons. |
| validate_id_input() | Allows numeric identification input. |
| calculate_fee_event() | Handles automatic fee calculation events. |
| calculate_fee() | Calculates the membership fee. |
| validate_form() | Validates required information. |
| register_affiliate() | Registers an affiliate. |
| clear_form() | Clears input fields. |
| refresh_treeview() | Updates displayed records. |
| generate_report() | Displays the selected structure report. |
| delete_affiliate() | Deletes an affiliate according to the structure. |
| exit_application() | Closes the application. |
