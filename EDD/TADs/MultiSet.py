class MultiSet:
    def __init__(self):
        # boolean presence per value and multiplicity per value
        self.data = []
        self.counts = []
        # distinct_count = number of different values present
        # total_count = total number of elements counting multiplicities
        self.distinct_count = 0
        self.total_count = 0

    def _ensure_capacity(self, value):
        if value >= len(self.data):
            new_len = value + 1
            self.data.extend([False] * (new_len - len(self.data)))
            self.counts.extend([0] * (new_len - len(self.counts)))

    def insert(self, value):
        if value < 0:
            raise Exception("Value must be non-negative")

        self._ensure_capacity(value)

        if not self.data[value]:
            # first time the value appears
            self.data[value] = True
            self.counts[value] = 1
            self.distinct_count += 1
        else:
            # already present, increment multiplicity
            self.counts[value] += 1

        self.total_count += 1

    def delete(self, value):
        if value < 0 or value >= len(self.data):
            raise Exception("Value out of bounds")

        if not self.data[value]:
            raise Exception("Value not present")

        if self.counts[value] > 1:
            self.counts[value] -= 1
        else:
            self.data[value] = False
            self.counts[value] = 0
            self.distinct_count -= 1

        self.total_count -= 1

    def exists(self, value):
        if value < 0 or value >= len(self.data):
            return False

        return self.data[value]

    def len(self):
        return self.distinct_count

    def cardinal(self):
        return self.total_count

    def multiplicity(self, value):
        if value < 0 or value >= len(self.data):
            return 0

        return self.counts[value] if self.data[value] else 0

    def __repr__(self):
        parts = []
        for i in range(len(self.data)):
            if self.data[i]:
                parts.append(f"{i}x{self.counts[i]}")
        return "{" + ",".join(parts) + "}"

    def __iter__(self):
        for i in range(len(self.data)):
            if self.data[i]:
                for _ in range(self.counts[i]):
                    yield i
