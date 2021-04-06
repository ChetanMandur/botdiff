from sys import breakpointhook


class BuildPage:
    def __init__(self, champ, role):
        self.champ_searched = champ
        self.role_searched = role
        self.core_build = []
        self.starter_items = []
        self.boots = []
        self.extra_items = []

    def pretty_print(self):
        return f"""> __**{self.champ_searched.upper()} ({self.role_searched.upper()})**__
                > **Starting Items**
                {self.pretty_item_list(self.starter_items)}
                > **Core Build**
                {self.pretty_core_build()} 
                > **Boots**
                {self.pretty_item_list(self.boots)} 
                > **Extra Items**
                {self.pretty_extra_items()}"""

    def pretty_item_list(self, item_list):
        output = ""
        current_index = 1
        for item in item_list:
            if current_index != 1:
                output = output + "\n"
            new_item = f"> {current_index}. {item[0]} | *Cost: {item[1]}*"
            output = output + new_item
            current_index += 1

        return output

    def pretty_core_build(self):
        if not self.core_build:
            return (
                "> This champ and role combo does not have a determined core build  :("
            )

        else:
            return self.pretty_item_list(self.core_build)

    def pretty_extra_items(self):
        reduced_extra_items = []
        for current_extra_item in self.extra_items:
            if (
                current_extra_item not in self.core_build
                and current_extra_item not in self.boots
                and current_extra_item not in self.starter_items
            ):
                reduced_extra_items.append(current_extra_item)

        return self.pretty_item_list(reduced_extra_items[:5])
