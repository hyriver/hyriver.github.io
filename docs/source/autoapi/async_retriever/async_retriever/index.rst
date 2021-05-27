:mod:`async_retriever.async_retriever`
======================================

.. py:module:: async_retriever.async_retriever

.. autoapi-nested-parse::

   Core async functions.



Module Contents
---------------

.. function:: retrieve(urls: List[str], read: str, request_kwds: Optional[List[Dict[str, Any]]] = None, request: str = 'GET', max_workers: int = 8, cache_name: Optional[Union[Path, str]] = None) -> List[Union[str, Dict[str, Any], bytes]]

   Send async requests.

   This function is based on
   `this <https://github.com/HydrologicEngineeringCenter/data-retrieval-scripts/blob/master/qpe_async_download.py>`__
   script.

   :Parameters: * **urls** (:class:`list` of :class:`str`) -- A list of URLs.
                * **read** (:class:`str`) -- The method for returning the request; binary, json, and text.
                * **request_kwds** (:class:`list` of :class:`dict`, *optional*) -- A list of requests kwds corresponding to input URLs (1 on 1 mapping), defaults to None.
                  For example, [{"params": {...}, "headers": {...}}, ...].
                * **request** (:class:`str`, *optional*) -- The request type; GET or POST, defaults to GET.
                * **max_workers** (:class:`int`, *optional*) -- The maximum number of async processes, defaults to 8.
                * **cache_name** (:class:`str`, *optional*) -- Path to a file for caching the session, default to None which uses a file
                  called aiohttp_cache.sqlite under the systems' cache directory: ~/.cache
                  for Linux and MacOS, and %Temp% for Windows.

   :returns: :class:`list` -- A list of responses which are not in the order of input requests.

   .. rubric:: Examples

   >>> import async_retriever as ar
   >>> stations = ["01646500", "08072300", "11073495"]
   >>> base = "https://waterservices.usgs.gov/nwis/site"
   >>> urls, kwds = zip(
   ...     *[
   ...         (base, {"params": {"format": "rdb", "sites": s, "siteStatus": "all"}})
   ...         for s in stations
   ...     ]
   ... )
   >>> resp = ar.retrieve(urls, "text", request_kwds=kwds)
   >>> resp[0].split('\n')[-2].split('\t')[1]
   '01646500'


