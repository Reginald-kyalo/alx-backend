#!/usr/bin/env python3
from typing import Tuple
"""Pagination"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Implements index range"""
    if page == 0 or page_size == 0:
        return
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
