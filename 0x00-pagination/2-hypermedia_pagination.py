import csv
import math
from typing import List, Any
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        try:
            assert (page > 0 or type(page) != int)
            assert (page_size > 0 or type(page_size) != int)
        except (AssertionError, TypeError):
            return []
        self.__dataset = self.dataset()
        start, end = index_range(page, page_size)
        dataset_list: List[List] = self.__dataset[start:end]
        return dataset_list

    def get_hyper(self, page: int = 1, page_size: int = 10):
        prev_page = next_page = total_pages = 0
        data = self.get_page(page, page_size)
        total_pages = math.ceil((len(self.__dataset)) / page_size)
        if ((len(self.__dataset) / page_size) > page):
            next_page = page + 1
            page_size = page_size
            if (page - 1) > 0:
                prev_page = page - 1
        else:
            next_page = None
            prev_page = None
            page_size = 0
        data_dict = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
            }
        return data_dict
