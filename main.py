import numpy as np
from NestedDict import nested_keys


class runner:
    # Sample nested Dictionary
    sample_dict = {"915714438273826858":
        [
            {"915714438823313420":
                 ["", 0]
             },
            [
                {"747797252105306212":
                     [1, 2]
                 },
                {"695390884291674153":
                     [3, 8]
                 }
            ]
        ]
    }
    # Initialize all_key (all root as a list), and all values. Final result will return root
    # for each values, so if value is a list, it will return same root for each value
    all_key = []
    all_values = []
    root = []
    nested_keys.main(sample_dict, all_key, all_values, root)
    print(all_key)
    print(all_values)
