:mod:`async_retriever.async_retriever`
======================================

.. py:module:: async_retriever.async_retriever

.. autoapi-nested-parse::

   Core async functions.



Module Contents
---------------

.. py:class:: AsyncRequest

   Async send/request.

   :Parameters: * **url** (:class:`str`) -- URL to be retrieved
                * **session_req** (:class:`ClientSession`) -- A ClientSession for sending the request
                * **kwds** (:class:`dict`) -- Arguments to be passed to requests

   .. method:: binary(self) -> bytes
      :async:

      Create an async request and return the response as binary.

      :returns: :class:`bytes` -- The retrieved response as binary.


   .. method:: json(self) -> Dict[str, Any]
      :async:

      Create an async request and return the response as json.

      :returns: :class:`dict` -- The retrieved response as json.


   .. method:: text(self) -> str
      :async:

      Create an async request and return the response as a string.

      :returns: :class:`str` -- The retrieved response as string.



.. function:: retrieve(urls: List[str], read: str, request_kwds: Optional[List[Dict[str, Any]]] = None, request_method: str = 'GET', max_workers: int = 8, cache_name: Optional[Union[Path, str]] = None) -> List[Union[str, Dict[str, Any], bytes]]

   Send async requests.

   :Parameters: * **urls** (:class:`list` of :class:`str`) -- List of URLs.
                * **read** (:class:`str`) -- Method for returning the request; ``binary``, ``json``, and ``text``.
                * **request_kwds** (:class:`list` of :class:`dict`, *optional*) -- List of requests keywords corresponding to input URLs (1 on 1 mapping), defaults to None.
                  For example, ``[{"params": {...}, "headers": {...}}, ...]``.
                * **request_method** (:class:`str`, *optional*) -- Request type; ``GET`` or ``POST``. Defaults to ``GET``.
                * **max_workers** (:class:`int`, *optional*) -- Maximum number of async processes, defaults to 8.
                * **cache_name** (:class:`str`, *optional*) -- Path to a folder for caching the session, defaults to ``cache/aiohttp_cache.sqlite``.

   :returns: :class:`list` -- List of responses which are not necessarily in the order of input requests.

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


