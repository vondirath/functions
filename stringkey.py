class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """
            Input a string that's stored in the table. using hash
            helper calculator.
        """
        # uses helper to determine hash value
        hv = self.calculate_hash_value(string)
        # check if hash value exists
        if hv != -1:
            # if table is filled insert new data after
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
                # saves data to table if it is empty
                self.table[hv] = [string]


    def lookup(self, string):
        """
            Return the hash value if the string is already in the table.
            Return -1 otherwise.
        """
        # uses helper to determine hash value
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                if string in self.table[hv]:
                    return hv
        return -1

    def calculate_hash_value(self, string):
        """
            Helper function to calulate a hash value from a string. 
            ASCII value of first char * 100 + ASCII value of second char
        """
        # gets ASCII value of first char * 100 adds to second char
        value = ord(string[0]) * 100 + ord(string[1])
        return value



# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('OK')

# Test lookup edge case
# Should be -1
print hash_table.lookup('OK')

# Test store
hash_table.store('OK')
# Should be 8568
print hash_table.lookup('OK')

# Test store edge case
hash_table.store('OKLAHOMA')
# Should be 8568
print hash_table.lookup('OKLAHOMA')
