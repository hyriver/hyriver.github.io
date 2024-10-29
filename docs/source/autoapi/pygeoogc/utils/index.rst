pygeoogc.utils
==============

.. py:module:: pygeoogc.utils

.. autoapi-nested-parse::

   Some utilities for PyGeoOGC.







Module Contents
---------------

.. py:class:: RetrySession(retries = 3, backoff_factor = 0.3, status_to_retry = (500, 502, 504), prefixes = ('https://', ), cache_name = None, expire_after = EXPIRE_AFTER, disable = False, ssl = True)

   Configures the passed-in session to retry on failed requests.

   .. rubric:: Notes

   The fails can be due to connection errors, specific HTTP response
   codes and 30X redirections. The code was originally based on:
   https://github.com/bustawin/retry-requests

   :Parameters: * **retries** (:class:`int`, *optional*) -- The number of maximum retries before raising an exception, defaults to 5.
                * **backoff_factor** (:class:`float`, *optional*) -- A factor used to compute the waiting time between retries, defaults to 0.5.
                * **status_to_retry** (:class:`tuple`, *optional*) -- A tuple of status codes that trigger the reply behaviour, defaults to (500, 502, 504).
                * **prefixes** (:class:`tuple`, *optional*) -- The prefixes to consider, defaults to ("http://", "https://")
                * **cache_name** (:class:`str`, *optional*) -- Path to a folder for caching the session, default to None which uses
                  system's temp directory.
                * **expire_after** (:class:`int`, *optional*) -- Expiration time for the cache in seconds, defaults to -1 (never expire).
                * **disable** (:class:`bool`, *optional*) -- If ``True`` temporarily disable caching request/responses, defaults to ``False``.
                * **ssl** (:class:`bool`, *optional*) -- If ``True`` verify SSL certificates, defaults to ``True``.


   .. py:method:: close()

      Close the session.



   .. py:method:: get(url, payload = None, params = None, headers = None, stream = None)

      Retrieve data from a url by GET and return the Response.



   .. py:method:: head(url, params = None, data = None, json = None, headers = None)

      Retrieve data from a url by POST and return the Response.



   .. py:method:: post(url, payload = None, data = None, json = None, headers = None, stream = None)

      Retrieve data from a url by POST and return the Response.



   .. py:property:: disable
      :type: bool


      Disable caching request/responses.


.. py:function:: match_crs(geom, in_crs, out_crs)

   Reproject a geometry to another CRS.

   :Parameters: * **geom** (:class:`list` or :class:`tuple` or :class:`geometry`) -- Input geometry which could be a list of coordinates such as ``[(x1, y1), ...]``,
                  a bounding box like so ``(xmin, ymin, xmax, ymax)``, or any valid ``shapely``'s
                  geometry such as ``Polygon``, ``MultiPolygon``, etc..
                * **in_crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`) -- Spatial reference of the input geometry
                * **out_crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`) -- Target spatial reference

   :returns: :class:`same type as the input geometry` -- Transformed geometry in the target CRS.

   .. rubric:: Examples

   >>> from shapely import Point
   >>> point = Point(-7766049.665, 5691929.739)
   >>> match_crs(point, 3857, 4326).xy
   (array('d', [-69.7636111130079]), array('d', [45.44549114818127]))
   >>> bbox = (-7766049.665, 5691929.739, -7763049.665, 5696929.739)
   >>> match_crs(bbox, 3857, 4326)
   (-69.7636111130079, 45.44549114818127, -69.73666165448431, 45.47699468552394)
   >>> coords = [(-7766049.665, 5691929.739)]
   >>> match_crs(coords, 3857, 4326)
   [(-69.7636111130079, 45.44549114818127)]


.. py:function:: streaming_download(urls: str, kwds: dict[str, dict[Any, Any]] | None = None, fnames: str | pathlib.Path | None = None, root_dir: str | pathlib.Path | None = None, file_prefix: str = '', file_extention: str = '', method: Literal['GET', 'POST', 'get', 'post'] = 'GET', ssl: bool = True, chunk_size: int = CHUNK_SIZE, n_jobs: int = MAX_CONN) -> pathlib.Path | None
                 streaming_download(urls: list[str], kwds: list[dict[str, dict[Any, Any]]] | None = None, fnames: collections.abc.Sequence[str | pathlib.Path] | None = None, root_dir: str | pathlib.Path | None = None, file_prefix: str = '', file_extention: str = '', method: Literal['GET', 'POST', 'get', 'post'] = 'GET', ssl: bool = True, chunk_size: int = CHUNK_SIZE, n_jobs: int = MAX_CONN) -> list[pathlib.Path | None]

   Download and store files in parallel from a list of URLs/Keywords.

   .. rubric:: Notes

   This function runs asynchronously in parallel using ``n_jobs`` threads.

   :Parameters: * **urls** (:class:`tuple` or :class:`list`) -- A list of URLs to download.
                * **kwds** (:class:`tuple` or :class:`list`, *optional*) -- A list of keywords associated with each URL, e.g.,
                  ({"params": ..., "headers": ...}, ...). Defaults to ``None``.
                * **fnames** (:class:`tuple` or :class:`list`, *optional*) -- A list of filenames associated with each URL, e.g.,
                  ("file1.zip", ...). Defaults to ``None``. If not provided,
                  random unique filenames will be generated based on
                  URL and keyword pairs.
                * **root_dir** (:class:`str` or :class:`Path`, *optional*) -- Root directory to store the files, defaults to ``None`` which
                  uses HyRiver's cache directory. Note that you should either
                  provide ``root_dir`` or ``fnames``. If both are provided,
                  ``root_dir`` will be ignored.
                * **file_prefix** (:class:`str`, *optional*) -- Prefix to add to filenames when storing the files, defaults
                  to ``None``, i.e., no prefix. This argument will be only be
                  used if ``fnames`` is not passed.
                * **file_extention** (:class:`str`, *optional*) -- Extension to use for storing the files, defaults to ``None``,
                  i.e., no extension if ``fnames`` is not provided otherwise. This
                  argument will be only be used if ``fnames`` is not passed.
                * **method** (:class:`str`, *optional*) -- HTTP method to use, i.e, ``GET`` or ``POST``, by default "GET".
                * **ssl** (:class:`bool`, *optional*) -- Whether to use SSL verification, defaults to ``True``.
                * **chunk_size** (:class:`int`, *optional*) -- Chunk size to use when downloading, defaults to 100 * 1024 * 1024
                  i.e., 100 MB.
                * **n_jobs** (:class:`int`, *optional*) -- The maximum number of concurrent downloads, defaults to 10.

   :returns: :class:`list` -- A list of ``pathlib.Path`` objects associated with URLs in the
             same order.


.. py:function:: traverse_json(json_data, ipath)

   Extract an element from a JSON-like object along a specified ipath.

   This function is based on
   `bcmullins <https://bcmullins.github.io/parsing-json-python/>`__.

   :Parameters: * **json_data** (:class:`dict` or :class:`list` of :class:`dicts`) -- The input json dictionary.
                * **ipath** (:class:`list`) -- The ipath to the requested element.

   :returns: :class:`list` -- The sub-items founds in the JSON.

   .. rubric:: Examples

   >>> data = [
   ...     {"employees": [
   ...         {"name": "Alice", "role": "dev", "nbr": 1},
   ...         {"name": "Bob", "role": "dev", "nbr": 2},
   ...         ],},
   ...     {"firm": {"name": "Charlie's Waffle Emporium", "location": "CA"}},
   ... ]
   >>> traverse_json(data, ["employees", "name"])
   [['Alice', 'Bob'], [None]]


.. py:function:: validate_crs(crs)

   Validate a CRS.

   :Parameters: **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`) -- Input CRS.

   :returns: :class:`str` -- Validated CRS as a string.


