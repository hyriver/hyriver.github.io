:py:mod:`async_retriever.async_retriever`
=========================================

.. py:module:: async_retriever.async_retriever

.. autoapi-nested-parse::

   Core async functions.



Module Contents
---------------

.. py:function:: delete_url_cache(url, request_method = 'GET', cache_name = None, **kwargs)

   Delete cached response associated with ``url``, along with its history (if applicable).

   :Parameters: * **url** (:class:`str`) -- URL to be deleted from the cache
                * **request_method** (:class:`str`, *optional*) -- HTTP request method to be deleted from the cache, defaults to ``GET``.
                * **cache_name** (:class:`str`, *optional*) -- Path to a file for caching the session, defaults to
                  ``./cache/aiohttp_cache.sqlite``.
                * **kwargs** (:class:`dict`, *optional*) -- Keywords to pass to the ``cache.delete_url()``.


.. py:function:: retrieve(urls, read, request_kwds = None, request_method = 'GET', max_workers = 8, cache_name = None, family = 'both', timeout = 5.0, expire_after = EXPIRE, ssl = None, disable = False)

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
                * **expire_after** (:class:`int`, *optional*) -- Expiration time for response caching in seconds, defaults to -1 (never expire).
                * **ssl** (:class:`bool` or :class:`SSLContext`, *optional*) -- SSLContext to use for the connection, defaults to None. Set to False to disable
                  SSL cetification verification.
                * **disable** (:class:`bool`, *optional*) -- If ``True`` temporarily disable caching requests and get new responses
                  from the server, defaults to False.

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


