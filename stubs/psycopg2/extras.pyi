# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-self-use
# pylint: disable=unused-argument
# pylint: disable=multiple-statements
# pylint: disable=super-init-not-called

from typing import Any, Optional
# from .compat import PY2 as PY2, PY3 as PY3, lru_cache as lru_cache
# from .extensions import connection as _connection, cursor as _cursor, quote_ident as quote_ident
# from collections import OrderedDict
# from psycopg2._ipaddress import register_ipaddress as register_ipaddress
from psycopg2._json import Json as Json
# from psycopg2._json import Json as Json, json as json, register_default_json as register_default_json, register_default_jsonb as register_default_jsonb, register_json as register_json
# from psycopg2._psycopg import REPLICATION_LOGICAL as REPLICATION_LOGICAL, REPLICATION_PHYSICAL as REPLICATION_PHYSICAL, ReplicationConnection as _replicationConnection, ReplicationCursor as _replicationCursor, ReplicationMessage as ReplicationMessage
# from psycopg2._range import DateRange as DateRange, DateTimeRange as DateTimeRange, DateTimeTZRange as DateTimeTZRange, NumericRange as NumericRange, Range as Range, RangeAdapter as RangeAdapter, RangeCaster as RangeCaster, register_range as register_range
#
#
# class DictCursorBase(_cursor):
#     row_factory: Any = ...
#     def __init__(self, *args: Any, **kwargs: Any) -> None: ...
#     def fetchone(self): ...
#     def fetchmany(self, size: Optional[Any] = ...): ...
#     def fetchall(self): ...
#     def __iter__(self) -> Any: ...
#
#
# class DictConnection(_connection):
#     def cursor(self, *args: Any, **kwargs: Any): ...
#
#
# class DictCursor(DictCursorBase):
#     def __init__(self, *args: Any, **kwargs: Any) -> None: ...
#     index: Any = ...
#     def execute(self, query: Any, vars: Optional[Any] = ...): ...
#     def callproc(self, procname: Any, vars: Optional[Any] = ...): ...
#
#
# class DictRow(list):
#     def __init__(self, cursor: Any) -> None: ...
#     def __getitem__(self, x: Any): ...
#     def __setitem__(self, x: Any, v: Any) -> None: ...
#     def items(self): ...
#     def keys(self): ...
#     def values(self): ...
#     def get(self, x: Any, default: Optional[Any] = ...): ...
#     def copy(self): ...
#     def __contains__(self, x: Any): ...
#     def __reduce__(self): ...
#
#
# class RealDictConnection(_connection):
#     def cursor(self, *args: Any, **kwargs: Any): ...
#
#
# class RealDictCursor(DictCursorBase):
#     def __init__(self, *args: Any, **kwargs: Any) -> None: ...
#     column_mapping: Any = ...
#     def execute(self, query: Any, vars: Optional[Any] = ...): ...
#     def callproc(self, procname: Any, vars: Optional[Any] = ...): ...
#
#
# class RealDictRow(OrderedDict):
#     def __init__(self, *args: Any, **kwargs: Any) -> None: ...
#     def __setitem__(self, key: Any, value: Any) -> None: ...
#
#
# class NamedTupleConnection(_connection):
#     def cursor(self, *args: Any, **kwargs: Any): ...
#
#
# class NamedTupleCursor(_cursor):
#     Record: Any = ...
#     MAX_CACHE: int = ...
#     def execute(self, query: Any, vars: Optional[Any] = ...): ...
#     def executemany(self, query: Any, vars: Any): ...
#     def callproc(self, procname: Any, vars: Optional[Any] = ...): ...
#     def fetchone(self): ...
#     def fetchmany(self, size: Optional[Any] = ...): ...
#     def fetchall(self): ...
#     def __iter__(self) -> Any: ...
#
#
# class LoggingConnection(_connection):
#     log: Any = ...
#     def initialize(self, logobj: Any) -> None: ...
#     def filter(self, msg: Any, curs: Any): ...
#     def cursor(self, *args: Any, **kwargs: Any): ...
#
#
# class LoggingCursor(_cursor):
#     def execute(self, query: Any, vars: Optional[Any] = ...): ...
#     def callproc(self, procname: Any, vars: Optional[Any] = ...): ...
#
#
# class MinTimeLoggingConnection(LoggingConnection):
#     def initialize(self, logobj: Any, mintime: int = ...) -> None: ...
#     def filter(self, msg: Any, curs: Any): ...
#     def cursor(self, *args: Any, **kwargs: Any): ...
#
#
# class MinTimeLoggingCursor(LoggingCursor):
#     timestamp: Any = ...
#     def execute(self, query: Any, vars: Optional[Any] = ...): ...
#     def callproc(self, procname: Any, vars: Optional[Any] = ...): ...
#
#
# class LogicalReplicationConnection(_replicationConnection):
#     def __init__(self, *args: Any, **kwargs: Any) -> None: ...
#
#
# class PhysicalReplicationConnection(_replicationConnection):
#     def __init__(self, *args: Any, **kwargs: Any) -> None: ...
#
#
# class StopReplication(Exception):
#     ...
#
#
# class ReplicationCursor(_replicationCursor):
#     def create_replication_slot(
#         self, slot_name: Any, slot_type: Optional[Any] = ..., output_plugin: Optional[Any] = ...) -> None: ...
#
#     def drop_replication_slot(self, slot_name: Any) -> None: ...
#     def start_replication(self, slot_name: Optional[Any] = ..., slot_type: Optional[Any] = ..., start_lsn: int = ...,
#                           timeline: int = ..., options: Optional[Any] = ..., decode: bool = ..., status_interval: int = ...) -> None: ...
#
#     def fileno(self): ...
#
#
# class UUID_adapter:
#     def __init__(self, uuid: Any) -> None: ...
#     def __conform__(self, proto: Any): ...
#     def getquoted(self): ...
#
#

# pylint: disable=unsubscriptable-object
def register_uuid(oids: Optional[Any] = ...,
                  conn_or_curs: Optional[Any] = ...) -> None: ...
#
#
# class Inet:
#     addr: Any = ...
#     def __init__(self, addr: Any) -> None: ...
#     def prepare(self, conn: Any) -> None: ...
#     def getquoted(self): ...
#     def __conform__(self, proto: Any): ...
#
#
# def register_inet(oid: Optional[Any] = ...,
#                   conn_or_curs: Optional[Any] = ...): ...
#
#
# def wait_select(conn: Any) -> None: ...
#
#
# class HstoreAdapter:
#     wrapped: Any = ...
#     def __init__(self, wrapped: Any) -> None: ...
#     conn: Any = ...
#     getquoted: Any = ...
#     def prepare(self, conn: Any) -> None: ...
#     @classmethod
#     def parse(self, s: Any, cur: Any, _bsdec: Any = ...): ...
#     @classmethod
#     def parse_unicode(self, s: Any, cur: Any): ...
#     @classmethod
#     def get_oids(self, conn_or_curs: Any): ...
#
#
# def register_hstore(conn_or_curs: Any, globally: bool = ..., unicode: bool = ...,
#                     oid: Optional[Any] = ..., array_oid: Optional[Any] = ...) -> None: ...
#
#
# class CompositeCaster:
#     name: Any = ...
#     schema: Any = ...
#     oid: Any = ...
#     array_oid: Any = ...
#     attnames: Any = ...
#     atttypes: Any = ...
#     typecaster: Any = ...
#     array_typecaster: Any = ...
#     def __init__(self, name: Any, oid: Any, attrs: Any,
#                  array_oid: Optional[Any] = ..., schema: Optional[Any] = ...) -> None: ...
#
#     def parse(self, s: Any, curs: Any): ...
#     def make(self, values: Any): ...
#     @classmethod
#     def tokenize(self, s: Any): ...
#
#
# def register_composite(name: Any, conn_or_curs: Any,
#                        globally: bool = ..., factory: Optional[Any] = ...): ...
#
#
# def execute_batch(cur: Any, sql: Any, argslist: Any,
#                   page_size: int = ...) -> None: ...
#
#
# def execute_values(cur: Any, sql: Any, argslist: Any,
#                    template: Optional[Any] = ..., page_size: int = ..., fetch: bool = ...): ...
