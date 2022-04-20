class nested_keys:
    @staticmethod
    def main(item, all_key, all_values, root):
        method_name = '_' + type(item).__name__ + '_iteration' if type(item).__name__ in ['list',
                                                                                          'dict'] else '_' + 'other' + '_iteration'
        getattr(nested_keys, method_name)(item, all_key, all_values, root)
        ## without method_name version###
        # if isinstance(item, dict):
        #     nested_keys._dict_iteration(item, all_key, all_values, root)
        # elif isinstance(item, list):
        #     nested_keys._list_iteration(item, all_key, all_values, root)
        #
        # else:
        #     nested_keys._other_iteration(item, all_values, all_key, root)
        # all_key.append(root)
        # all_values.append(item)

    @staticmethod
    def _dict_iteration(item, all_key, all_values, root):
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
                nested_keys._other_iteration(items, all_values, all_key, root)
                # all_key.append(root)
                # all_values.append(items)
            # root = []
        return all_values, all_key, root

    @staticmethod
    def _other_iteration(item, all_key, all_values, root):
        all_key.append(root)
        all_values.append(item)
        return all_values, all_key, root
