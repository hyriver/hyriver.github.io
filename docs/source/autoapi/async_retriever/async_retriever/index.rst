:py:mod:`async_retriever.async_retriever`
=========================================

.. py:module:: async_retriever.async_retriever

.. autoapi-nested-parse::

   Core async functions.



Module Contents
---------------

.. py:function:: clean_cache(cache_name)

   Remove expired responses from the cache file.


.. py:function:: retrieve(urls, read, request_kwds = None, request_method = 'GET', max_workers = 8, cache_name = None, family = 'both', timeout = 5.0, expire_after = _EXPIRE)

   Send async requests.

   :Parameters: * **urls** (:class:`list` of :class:`str`) -- List of URLs.
                * **read** (:class:`str`) -- Method for returning the request; ``binary``, ``json``, and ``text``.
                * **request_kwds** (:class:`list` of :class:`dict`, *optional*) -- List of requests keywords corresponding to input URLs (1 on 1 mapping), defaults to None.
                  For example, ``[{"params": {...}, "headers": {...}}, ...]``.
                * **request_method** (:class:`str`, *optional*) -- Request type; ``GET`` (``get``) or ``POST`` (``post``). Defaults to ``GET``.
                * **max_workers** (:class:`int`, *optional*) -- Maximum number of async processes, defaults to 8.
                * **cache_name** (:class:`str`, *optional*) -- Path to a file for caching the session, defaults to ``./cache/aiohttp_cache.sqlite``.
                * **family** (:class:`str`, *optional*) -- TCP socket family, defaults to both, i.e., IPv4 and IPv6. For IPv4
                  or IPv6 only pass ``ipv4`` or ``ipv6``, respectively.
                * **timeout** (:class:`float`, *optional*) -- Timeout for the request, defaults to 5.0.
                * **expire_after** (:class:`int`, *optional*) -- Expiration time for the cache in seconds, defaults to 24 hours.

   :returns: :class:`list` -- List of responses in the order of input URLs.

   .. rubric:: Examples

   >>> import async_retriever as ar
   >>> stations = ["01646500", "08072300", "11073495"]
   >>> url = "https://waterservices.usgs.gov/nwis/site"
   >>> urls, kwds = zip(
   ...     *[
   ...         (url, {"params": {"format": "rdb", "sites": s, "siteStatus": "all"}})
   ...         for s in stations
   ...     ]
   ... )
   >>> resp = ar.retrieve(urls, "text", request_kwds=kwds)
   >>> resp[0].split('\n')[-2].split('\t')[1]
   '01646500'


