# This code is based on code from Apache Spark under the license found in the LICENSE file located in the 'dataframe' folder.

from __future__ import annotations

import typing as t

from sqlframe.base.group import _BaseGroupedData

if t.TYPE_CHECKING:
    from sqlframe.spark.dataframe import SparkDataFrame


class SparkGroupedData(_BaseGroupedData["SparkDataFrame"]):
    pass
