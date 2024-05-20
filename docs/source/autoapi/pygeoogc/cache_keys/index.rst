pygeoogc.cache_keys
===================

.. py:module:: pygeoogc.cache_keys

.. autoapi-nested-parse::

   Functions for creating unique keys based on web request parameters.

   This module is based on the ``aiohttp-client-cache`` package, which is
   licensed under the MIT license. See the ``LICENSE`` file for more details.





Module Contents
---------------

.. py:function:: create_request_key(method, url, params = None, data = None, json = None)

   Create a unique cache key based on request details.

   :Parameters: * **method** (:class:`str`) -- The HTTP method used in the request. Must be either "GET" or "POST".
                * **url** (:class:`str` or :class:`yarl.URL`) -- The URL of the request.
                * **params** (:class:`dict` or :class:`list` or :class:`str` or :obj:`None`, *optional*) -- The query parameters of the request. Default is None.
                * **data** (:class:`dict` or :obj:`None`, *optional*) -- The data of the request. Default is None.
                * **json** (:class:`dict` or :obj:`None`, *optional*) -- The JSON data of the request. Default is None.

   :returns: :class:`str` -- The unique cache key based on the request details.


