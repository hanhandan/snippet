# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals, division

from oslo_config import cfg
from oslo_db import concurrency
from oslo_log import log as logging

CONF = cfg.CONF
LOG = logging.getLogger(__name__)

_BACKEND_MAPPING = {'sqlalchemy': "{PROJECT}.db.sqlalchemy.api"}
IMPL = concurrency.TpoolDbapiWrapper(CONF, backend_mapping=_BACKEND_MAPPING)
api = IMPL
# import threading
# from oslo_db import api
#
# _IMPL = None
# _LOCK = threading.Lock()
# def get_api():
#     global _IMPL, _LOCK
#     if not _IMPL:
#         with _LOCK:
#             if not _IMPL:
#                 _IMPL = api.DBAPI.from_config(conf=CONF,
#                                               backend_mapping=_BACKEND_MAPPING)
#     return _IMPL


####################################
# API Interface
def get_data(id):
    return IMPL.get_data(id)


def set_data(data):
    return IMPL.set_data(data)
