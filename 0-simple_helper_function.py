#!/usr/bin/env python3
"""
0-simple_helper_function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    helper function to provide
    the start and end indexes for paginating
    a particular set
    Args:
        page (int): The Current Page Number
                    the user is On

        page_size (int): The number of records
                         displayed on each page

    Returns:
        tuple: start and end indexes
    """
    start_idx = (page - 1) * page_size
    end_idx = page * page_size

    return (start_idx, end_idx)
