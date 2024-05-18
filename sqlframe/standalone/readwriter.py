# This code is based on code from Apache Spark under the license found in the LICENSE file located in the 'dataframe' folder.

from __future__ import annotations

import typing as t

from sqlframe.base.readerwriter import _BaseDataFrameReader, _BaseDataFrameWriter

if t.TYPE_CHECKING:
    from sqlframe.standalone.dataframe import StandaloneDataFrame
    from sqlframe.standalone.session import StandaloneSession


class StandaloneDataFrameReader(_BaseDataFrameReader["StandaloneSession", "StandaloneDataFrame"]):
    pass


class StandaloneDataFrameWriter(_BaseDataFrameWriter["StandaloneSession", "StandaloneDataFrame"]):
    pass
