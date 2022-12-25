from merge_sort import merge_sort
from radix_sort import radix_sort
from smoothsort import smoothsort
from timsort import timsort
from tree_sort import tree_sort
from bucket_sort import bucket_sort
from intro_sort import IntroSort
from sorts import *
import time
import copy
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

SORTS = {
        'heap_sort': heap_sort, 'merge_sort': merge_sort, 'radix_sort': radix_sort,
        'smooth_sort': smoothsort, 'timsort': timsort, 'tree_sort': tree_sort,
        'bubble_sort': bubble_sort, 'cocktail_sort': cocktail_sort, 'insertion_sort': insertion_sort,
        'gnome_sort': gnome_sort, 'selection_sort': selection_sort, 'comb_sort': comb_sort,
        'shell_sort': shell_sort, 'quicksort': quicksort, 'intro_sort': IntroSort().introsort,
        'bucket_sort': bucket_sort, 'counting_sort': counting_sort
    }
EXECUTION_TIME = dict().fromkeys(SORTS.keys())
BORDERS = (10, 100, 1000, 10**4, 10**5, 10**6)
LIST_SIZE = 10**3

if __name__ == '__main__':
    test_list = np.random.randint(-BORDERS[2], BORDERS[2], size=LIST_SIZE).tolist()
    test_list = sorted(test_list)
    for name in SORTS.keys():
        list_for_sort = copy.deepcopy(test_list)
        start_time = time.time()
        SORTS[name](list_for_sort)
        EXECUTION_TIME[name] = [time.time() - start_time]
    df = pd.DataFrame(data=EXECUTION_TIME).transpose().sort_values(by=0, ascending=False)
    func = lambda x:round(x, 4)
    df_for_plot = df.copy(deep=True)
    df_for_plot[0] = df_for_plot[0].apply(func)
    df_for_plot = df_for_plot.transpose()
    df = df.transpose()
    ax = sns.barplot(data=df_for_plot)
    sns.barplot(data=df)
    ax.bar_label(ax.containers[0])
    print(df.transpose().to_string())
    plt.show()
