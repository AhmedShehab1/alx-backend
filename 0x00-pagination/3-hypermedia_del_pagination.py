#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Server class constructor
        Initializes dataset private attr to None
        """
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0

        Returns:
            dict[int, List]: _description_
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {i: dataset[i]
                                      for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Offset-Based Pagination with stable identifiers
        Args:
            index (int, optional): the current start index of the return page.
            Defaults to None.
            page_size (int, optional): the current page size. Defaults to 10.

        Returns:
            Dict: dictionary containing hypermedia along with requested data
        """
        if index is None:
            index = 0
        indexed_dataset = self.indexed_dataset()
        total_count = len(indexed_dataset)
        assert index > 0 and index < total_count
        next_index = None
        paginated_data = []
        i = 0
        for k, v in indexed_dataset.items():
            if k >= index:
                paginated_data.append(v)
            else:
                continue
            i += 1
            if i >= page_size:
                next_index = k
                break

        metadata = {
            "index": index,
            "data": paginated_data,
            "page_size": page_size,
            "next_index": next_index + 1 if paginated_data else None,
        }
        return metadata
