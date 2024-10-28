#!/usr/bin/env python3
"""
1-simple_pagination
"""
import importlib
import csv
from typing import List


index_range = importlib.import_module("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Server class constructor
        Initializes dataset private attr to None
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached Dataset

        Returns:
            List[List]: cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the content of the page based on the
        page_size and required page
        Args:
            page (int, optional): The current page number the user on.
            Defaults to 1.

            page_size (int, optional): The number of records
            displayed on each page. Defaults to 10.

        Returns:
            List[List]: list of lists for the dataset based on page
                        and page_size
                        if no such data available an empty list is returned
        """
        assert page is int and page > 0
        assert page_size is int and page_size > 0

        s_idx, e_idx = index_range(page, page_size)
        dataset = self.dataset()

        if e_idx > len(dataset):
            return []
        else:
            return dataset[s_idx:e_idx]
