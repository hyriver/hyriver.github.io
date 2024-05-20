pygridmet.core
==============

.. py:module:: pygridmet.core

.. autoapi-nested-parse::

   Core class for the GridMET functions.





Module Contents
---------------

.. py:class:: GridMET(dates = 2000, variables = None, snow = False)

   Base class for GridMET requests.

   :Parameters: * **dates** (:class:`tuple` or :class:`int` or :class:`list`, *optional*) -- Start and end dates as a tuple, (start, end), or a list of years.
                  Defaults to ``2000`` so the class can be initialized without any arguments.
                * **variables** (:class:`str` or :class:`list` or :class:`tuple`, *optional*) -- List of variables to be downloaded. The acceptable variables are:
                  ``pr``, ``rmax``, ``rmin``, ``sph``, ``srad``, ``th``, ``tmmn``, ``tmmx``, ``vs``,
                  ``bi``, ``fm100``, ``fm1000``, ``erc``, ``etr``, ``pet``, and ``vpd``.
                  Descriptions can be found `here <https://www.climatologylab.org/gridmet.html>`__.
                  Defaults to ``None``, i.e., all the variables are downloaded.
                * **snow** (:class:`bool`, *optional*) -- Compute snowfall from precipitation and minimum temperature. Defaults to ``False``.

   .. rubric:: References

   .. footbibliography::


   .. py:method:: check_dates(dates)
      :staticmethod:


      Check if input dates are in correct format and valid.



   .. py:method:: dates_todict(dates)

      Set dates by start and end dates as a tuple, (start, end).



   .. py:method:: dates_tolist(dates)

      Correct dates for GridMET accounting for leap years.

      GridMET doesn't account for leap years and removes Dec 31 when
      it's leap year.

      :Parameters: **dates** (:class:`tuple`) -- Target start and end dates.

      :returns: :class:`list` -- All the dates in the GridMET database within the provided date range.



   .. py:method:: separate_snow(clm, t_rain = T_RAIN, t_snow = T_SNOW)

      Separate snow based on :footcite:t:`Martinez_2010`.

      :Parameters: * **clm** (:class:`pandas.DataFrame` or :class:`xarray.Dataset`) -- Climate data that should include ``pr`` and ``tmmn``.
                   * **t_rain** (:class:`float`, *optional*) -- Threshold for temperature for considering rain, defaults to 2.5 K.
                   * **t_snow** (:class:`float`, *optional*) -- Threshold for temperature for considering snow, defaults to 0.6 K.

      :returns: :class:`pandas.DataFrame` or :class:`xarray.Dataset` -- Input data with ``snow (mm)`` column if input is a ``pandas.DataFrame``,
                or ``snow`` variable if input is an ``xarray.Dataset``.

      .. rubric:: References

      .. footbibliography::



   .. py:method:: years_todict(years)

      Set date by list of year(s).



   .. py:method:: years_tolist(years)

      Correct dates for GridMET accounting for leap years.

      GridMET doesn't account for leap years and removes Dec 31 when
      it's leap year.

      :Parameters: **years** (:class:`list`) -- A list of target years.

      :returns: :class:`list` -- All the dates in the GridMET database within the provided date range.



