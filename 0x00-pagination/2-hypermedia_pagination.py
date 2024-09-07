#!/usr/bin/env python3
import csv
import math
from typing import List
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
        """Implements get page"""
        assert (page > 0 or type(page) != int)
        assert (page_size > 0 or type(page_size) != int)
        self.__dataset = self.dataset()
        start, end = index_range(page, page_size)
        dataset_list: List[List] = self.__dataset[start:end]
        return dataset_list

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """Implements get_hyper"""
        start, end = index_range(page, page_size)
        data = self.get_page(page, page_size)
        total_pages = math.ceil((len(self.__dataset)) / page_size)
        page_info = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if end < len(self.__dataset) else None,
            'prev_page': page - 1 if start > 0 else None,
            'total_pages': total_pages,
        }
        return page_info
