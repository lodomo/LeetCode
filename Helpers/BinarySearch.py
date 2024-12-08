class BinarySearch:
    condition_dict = {
        "gt": lambda x, target: x > target,
        "ge": lambda x, target: x >= target,
        "lt": lambda x, target: x < target,
        "le": lambda x, target: x <= target,
        "eq": lambda x, target: x == target,
        "ne": lambda x, target: x != target,
    }

    condition_dict[">"] = condition_dict["gt"]
    condition_dict[">="] = condition_dict["ge"]
    condition_dict["<"] = condition_dict["lt"]
    condition_dict["<="] = condition_dict["le"]
    condition_dict["=="] = condition_dict["eq"]
    condition_dict["!="] = condition_dict["ne"]

    condition_dict["greater than"] = condition_dict["gt"]
    condition_dict["greater than or equal"] = condition_dict["ge"]
    condition_dict["less than"] = condition_dict["lt"]
    condition_dict["less than or equal"] = condition_dict["le"]
    condition_dict["equal"] = condition_dict["eq"]
    condition_dict["not equal"] = condition_dict["ne"]

    def find(self, arr, target, condition="eq", position=None):
        # Check if condition is a lambda expression
        if callable(condition):
            condition = condition
        else:
            try:
                condition = BinarySearch.condition_dict[condition]
            except KeyError:
                raise ValueError(
                    "Invalid condition. Must be one of 'gt', 'lt', 'ge', 'le', 'eq' or a lambda expression"
                )

        get_val = (lambda x: x) if position is None else (lambda x: x[position])

        left = 0
        right = len(arr) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            val = get_val(arr[mid])
            if condition(val, target):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
