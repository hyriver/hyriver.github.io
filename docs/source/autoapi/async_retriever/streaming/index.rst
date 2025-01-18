async_retriever.streaming
=========================

.. py:module:: async_retriever.streaming

.. autoapi-nested-parse::

   Download multiple files concurrently by streaming their content to disk.





Module Contents
---------------

.. py:function:: stream_write(urls, file_paths, request_method = 'get', ssl = True, chunk_size = CHUNK_SIZE, limit_per_host = 5)

   Download multiple files concurrently by streaming their content to disk.

   :Parameters: * **urls** (:class:`Sequence[str]`) -- List of URLs to download.
                * **file_paths** (:class:`Sequence[Path]`) -- List of file paths to save the downloaded content.
                * **request_method** (``{"get", "post"}``, *optional*) -- HTTP method to use (i.e., ``get`` or ``post``), by default ``get``.
                * **ssl** (:class:`bool` or :class:`ssl.SSLContext`, *optional*) -- Whether to verify SSL certificates, by default True. Also,
                  an SSLContext object can be passed to customize
                * **chunk_size** (:class:`int`, *optional*) -- Size of each chunk in bytes, by default 1 MB.
                * **limit_per_host** (:class:`int`, *optional*) -- Maximum simultaneous connections per host, by default 5.

   .. rubric:: Examples

   >>> import tempfile
   >>> url = "https://freetestdata.com/wp-content/uploads/2021/09/Free_Test_Data_500KB_CSV-1.csv"
   >>> with tempfile.NamedTemporaryFile(dir=".") as temp:
   ...     stream_write([url], [temp.name])


