
import os
from collections.abc import Collection
from more_itertools import flatten
from os import PathLike
from os.path import isdir
from typing import Any, Iterator, Text, Union

from ..BIDSPathConstants import ENTITY_STRINGS
from ..core.BIDSPathAbstract import BIDSPathAbstract
from ..core.bids_file.BIDSFile import BIDSFile

_bases = (BIDSPathAbstract, Collection)

__path__ = [os.path.join('..', '__init__.py')]


class BIDSDirAbstract(*_bases):
    """
    Abstract base class for directories in a BIDS Dataset.

    """

    __slots__, __bases__ = ENTITY_STRINGS, _bases
    __fspath__ = BIDSPathAbstract.__fspath__
    def __type__(self): return type(self)

    def __get_entities__(self):
        return super().__get_entities__()

    def __subclasscheck__(self, subclass) -> bool:
        return all((hasattr(subclass, 'entities'),
                    self.isdir(subclass.path)))

    def __instancecheck__(self, instance) -> bool:
        return all((hasattr(instance, 'entities'),
                    isdir(instance.path)))

    def __getitem__(self, i: int): return tuple(self.iterdir())[i]

    def __contains__(self, item: Any) -> bool:
        as_cls = tuple(self.iterdir())
        as_path_type = map(lambda p: p.path, as_cls)
        as_str = map(lambda p: p.path.__fspath__(), as_cls)
        return item in set(flatten((as_cls, as_path_type, as_str)))

    def __len__(self) -> int:
        return len(os.listdir(self.path))

    def __iter__(self) -> Iterator:
        yield from self.iterdir()

    @classmethod
    def __prepare__(cls, src: Union[Text, PathLike]):
        subclass_dict = BIDSDirAbstract.subclass_dict()
        if not cls.isdir(src):
            return src
        _mapper = (
            (cls.is_datatype_dir(src), 'Datatype'),
            (cls.is_session_dir(src), 'Session'),
            (cls.is_subject_dir(src), 'Subject')
        )
        _cls = next(filter(lambda item: bool(item[0]), _mapper))
        keywords = dict(zip(cls.__slots__,
                            super().__get_entities__(src)))
        subclass = subclass_dict[_cls[1]](src)
        subclass.__set_from_dict__(keywords)
        return subclass

    def glob(self, pattern: Text) -> Iterator:
        """
        Yields all existing paths matching a relative pattern in this subtree.

        Files defined in the '.bidsignore' file are omitted.

        """
        _paths = set(self.path.glob(pattern)).difference(set(self.bidsignore))
        yield from map(BIDSDirAbstract.__prepare__, map(BIDSFile, _paths))

    def iterdir(self) -> Iterator:
        """
        Iterate over paths in this directory.

        Does not yield any result for the special paths
        '.' and '..'. and those defined in the '.bidsignore' file.
        """
        _paths = set(self.path.iterdir()).difference(set(self.bidsignore))
        yield from map(BIDSDirAbstract.__prepare__, map(BIDSFile, _paths))

    def rglob(self, pattern: Text) -> Iterator:
        """
        Recursively yields all paths matching ``pattern`` in this subtree.

        Paths defined in the '.bidsignore' file are omitted.
        Args:
            pattern: str
                Pattern relative to ``self.path``.

        Returns: Iterator
        """
        _paths = set(self.path.rglob(pattern)).difference(set(self.bidsignore))
        yield from map(BIDSDirAbstract.__prepare__, map(BIDSFile, _paths))
