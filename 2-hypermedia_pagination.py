#!/usr/bin/env python3
"""
2-hypermedia_pagination
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
        Returns the content of the page based on the page_size
        and required page
        Args:
            page (int, optional): The current page number the user on.
            Defaults to 1.
            page_size (int, optional): The number of records
            displayed on each page. Defaults to 10.

        Returns:
            List[List]: list of lists for the dataset based on
                        page and page_size
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Paginate With HyperMedia metadata
        Args:
            page (int, optional): The current page number the user on.
            Defaults to 1.
            page_size (int, optional): The number of records
            displayed on each page. Defaults to 10.

        Returns:
            dict: dictionary containing Hypermedia metadata
        """
        dataset = self.dataset()
        e_idx = page_size * page
        total_count = len(dataset)
        paginated_data = self.get_page(page, page_size)

        metadata = {
            "page_size": page_size,
            "page": page,
            "data": paginated_data,
            "next_page": page + 1 if e_idx < total_count else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_count // page_size,
        }

        return metadata
