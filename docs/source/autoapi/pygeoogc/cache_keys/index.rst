:py:mod:`pygeoogc.cache_keys`
=============================

.. py:module:: pygeoogc.cache_keys

.. autoapi-nested-parse::

   Functions for creating unique keys based on web request parameters.

   This module is based on the ``aiohttp-client-cache`` package, which is
   licensed under the MIT license. See the ``LICENSE`` file for more details.



Module Contents
---------------

.. py:function:: create_request_key(method, url, params = None, data = None, json = None)

   Create a unique cache key based on request details.


