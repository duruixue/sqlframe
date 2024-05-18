# This code is based on code from Apache Spark under the license found in the LICENSE file located in the 'dataframe' folder.

from __future__ import annotations

import typing as t

from sqlframe.base.mixins.readwriter_mixins import PandasLoaderMixin, PandasWriterMixin
from sqlframe.base.readerwriter import (
    _BaseDataFrameReader,
    _BaseDataFrameWriter,
)

if t.TYPE_CHECKING:
    from sqlframe.redshift.session import RedshiftSession  # noqa
    from sqlframe.redshift.dataframe import RedshiftDataFrame  # noqa


class RedshiftDataFrameReader(
    PandasLoaderMixin["RedshiftSession", "RedshiftDataFrame"],
    _BaseDataFrameReader["RedshiftSession", "RedshiftDataFrame"],
):
    pass


class RedshiftDataFrameWriter(
    PandasWriterMixin["RedshiftSession", "RedshiftDataFrame"],
    _BaseDataFrameWriter["RedshiftSession", "RedshiftDataFrame"],
):
    pass
