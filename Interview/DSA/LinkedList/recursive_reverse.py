def rec_reverse(self):

        if self.head is None:
            return None

        self.rec_reverse_util(self.head, None)


def rec_reverse_util(self,current,prev):
    if current is None:
        self.head = prev
        current.nextnode = prev
        return

    next = current.nextnode
    current.nextnode = prev

    self.rec_reverse_util(next,current)