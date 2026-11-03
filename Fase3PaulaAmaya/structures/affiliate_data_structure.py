
from collections import deque


class AffiliateDataStructure:
    """
    Manages affiliate records using stack, queue and list structures.
    """

    def __init__(self):
        self.stack = deque()
        self.queue = deque()
        self.affiliate_list = []

    # ==========================================
    # STACK OPERATIONS - LIFO
    # ==========================================

    def push_affiliate(self, affiliate):
        """
        Adds an affiliate to the top of the stack.
        """
        self.stack.append(affiliate)

    def pop_affiliate(self):
        """
        Removes and returns the last affiliate in the stack.
        """
        if not self.stack:
            return None

        return self.stack.pop()

    def get_stack(self):
        """
        Returns stack records from newest to oldest.
        """
        return list(reversed(self.stack))

    def get_stack_fee_total(self):
        """
        Calculates the sum of membership fees in the stack.
        """
        return sum(
            affiliate.membership_fee
            for affiliate in self.stack
        )

    # ==========================================
    # QUEUE OPERATIONS - FIFO
    # ==========================================

    def enqueue_affiliate(self, affiliate):
        """
        Adds an affiliate to the end of the queue.
        """
        self.queue.append(affiliate)

    def dequeue_affiliate(self):
        """
        Removes and returns the first affiliate in the queue.
        """
        if not self.queue:
            return None

        return self.queue.popleft()

    def get_queue(self):
        """
        Returns queue records from first to last.
        """
        return list(self.queue)

    def get_queue_count(self):
        """
        Returns the number of affiliates in the queue.
        """
        return len(self.queue)

    # ==========================================
    # LIST OPERATIONS
    # ==========================================

    def add_to_list(self, affiliate):
        """
        Adds an affiliate to the end of the list.
        """
        self.affiliate_list.append(affiliate)

    def remove_from_list(self, id_number):
        """
        Searches for an affiliate by ID and removes it.
        Returns the removed affiliate or None.
        """
        for affiliate in self.affiliate_list:
            if affiliate.id_number == id_number:
                self.affiliate_list.remove(affiliate)
                return affiliate

        return None

    def find_in_list(self, id_number):
        """
        Searches for an affiliate by ID.
        """
        for affiliate in self.affiliate_list:
            if affiliate.id_number == id_number:
                return affiliate

        return None

    def get_list(self):
        """
        Returns all list records.
        """
        return list(self.affiliate_list)

    def get_list_income_average(self):
        """
        Calculates the average current income in the list.
        """
        if not self.affiliate_list:
            return 0

        total_income = sum(
            affiliate.current_income
            for affiliate in self.affiliate_list
        )

        return total_income / len(self.affiliate_list)

    # ==========================================
    # COMMON OPERATIONS
    # ==========================================

    def affiliate_exists(self, structure_name, id_number):
        """
        Checks whether an ID already exists in the selected structure.
        """
        records = self.get_records(structure_name)

        return any(
            affiliate.id_number == id_number
            for affiliate in records
        )

    def get_records(self, structure_name):
        """
        Returns records according to the selected structure.
        """
        if structure_name == "Pila":
            return self.get_stack()

        elif structure_name == "Cola":
            return self.get_queue()

        elif structure_name == "Lista":
            return self.get_list()

        return []

    def get_report(self, structure_name):
        """
        Generates the report for the selected structure.
        """
        if structure_name == "Pila":
            return self.get_stack_fee_total()

        elif structure_name == "Cola":
            return self.get_queue_count()

        elif structure_name == "Lista":
            return self.get_list_income_average()

        return 0
