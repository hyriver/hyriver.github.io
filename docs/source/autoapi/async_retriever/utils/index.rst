:py:mod:`async_retriever.utils`
===============================

.. py:module:: async_retriever.utils

.. autoapi-nested-parse::

   Core async functions.



Module Contents
---------------

.. py:class:: BaseRetriever(urls, read, request_kwds = None, request_method = 'GET', cache_name = None)

   Base class for async retriever.

   .. py:method:: generate_requests(urls, request_kwds)
      :staticmethod:

      Generate urls and keywords.



.. py:function:: create_cachefile(db_name = None)

   Create a cache folder in the current working directory.


.. py:function:: delete_url(url, method = 'GET', cache_name = None, **kwargs)
   :async:

   Delete cached response associated with ``url``.


.. py:function:: get_event_loop()

   Create an event loop.


.. py:function:: retriever(uid, url, s_kwds, session, read_type, r_kwds)
   :async:

   Create an async request and return the response as binary.

   :Parameters: * **uid** (:class:`int`) -- ID of the URL for sorting after returning the results
                * **url** (:class:`str`) -- URL to be retrieved
                * **s_kwds** (:class:`dict`) -- Arguments to be passed to requests
                * **session** (:class:`ClientSession`) -- A ClientSession for sending the request
                * **read_type** (:class:`str`) -- Return response as text, bytes, or json.
                * **r_kwds** (:class:`dict`) -- Keywords to pass to the response read function.
                  It is ``{"content_type": None}`` if ``read`` is ``json``
                  else an empty ``dict``.

   :returns: :class:`bytes` -- The retrieved response as binary.


