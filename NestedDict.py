class nested_keys:
    @staticmethod
    def main(item, all_key, all_values, root):
        if isinstance(item, dict):
            nested_keys._dic_itration(item, all_key, all_values, root)
        elif isinstance(item, list):
            nested_keys._list_iteration(item, all_key, all_values, root)

        else:
            all_key.append(root)
            all_values.append(item)

    @staticmethod
    def _dic_itration(item, all_key, all_values, root):
        for items in item.keys():
            root_item = root.copy()
            root_item.append(items)
            nested_keys.main(item[items], all_key, all_values, root_item)
        return all_values, all_key, root

    @staticmethod
    def _list_iteration(item, all_key, all_values, root):
        for index, items in enumerate(item):
            if isinstance(items, dict):
                nested_keys.main(items, all_key, all_values, root)
            elif isinstance(items, list):
                nested_keys.main(items, all_key, all_values, root)
            else:
                all_key.append(root)
                all_values.append(items)
            # root = []
        return all_values, all_key, root
