class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_address = ""
        split_addresses = address.split(".")
        for idx, val in enumerate(split_addresses):
            new_address += f"{val}"
            if idx != (len(split_addresses) - 1):
                new_address += "[.]"
        # return address.replace(".","[.]")
        return new_address
