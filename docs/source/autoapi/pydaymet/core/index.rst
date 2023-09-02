:py:mod:`pydaymet.core`
=======================

.. py:module:: pydaymet.core

.. autoapi-nested-parse::

   Core class for the Daymet functions.



Module Contents
---------------

.. py:class:: Daymet(variables = None, pet = None, snow = False, time_scale = 'daily', region = 'na')


   Base class for Daymet requests.

   :Parameters: * **variables** (:class:`str` or :class:`list` or :class:`tuple`, *optional*) -- List of variables to be downloaded. The acceptable variables are:
                  ``tmin``, ``tmax``, ``prcp``, ``srad``, ``vp``, ``swe``, ``dayl``
                  Descriptions can be found `here <https://daymet.ornl.gov/overview>`__.
                  Defaults to None i.e., all the variables are downloaded.
                * **pet** (:class:`str`, *optional*) -- Method for computing PET. Supported methods are
                  ``penman_monteith``, ``priestley_taylor``, ``hargreaves_samani``, and
                  None (don't compute PET). The ``penman_monteith`` method is based on
                  :footcite:t:`Allen_1998` assuming that soil heat flux density is zero.
                  The ``priestley_taylor`` method is based on
                  :footcite:t:`Priestley_1972` assuming that soil heat flux density is zero.
                  The ``hargreaves_samani`` method is based on :footcite:t:`Hargreaves_1982`.
                  Defaults to ``None``.
                * **snow** (:class:`bool`, *optional*) -- Compute snowfall from precipitation and minimum temperature. Defaults to ``False``.
                * **time_scale** (:class:`str`, *optional*) -- Data time scale which can be daily, monthly (monthly summaries),
                  or annual (annual summaries). Defaults to daily.
                * **region** (:class:`str`, *optional*) -- Region in the US, defaults to na. Acceptable values are:

                  * na: Continental North America
                  * hi: Hawaii
                  * pr: Puerto Rico

   .. rubric:: References

   .. footbibliography::

   .. py:method:: check_dates(dates)
      :staticmethod:

      Check if input dates are in correct format and valid.


   .. py:method:: dates_todict(dates)

      Set dates by start and end dates as a tuple, (start, end).


   .. py:method:: dates_tolist(dates)

      Correct dates for Daymet accounting for leap years.

      Daymet doesn't account for leap years and removes Dec 31 when
      it's leap year.

      :Parameters: **dates** (:class:`tuple`) -- Target start and end dates.

      :returns: :class:`list` -- All the dates in the Daymet database within the provided date range.


   .. py:method:: separate_snow(clm, t_rain = T_RAIN, t_snow = T_SNOW)

      Separate snow based on :footcite:t:`Martinez_2010`.

      :Parameters: * **clm** (:class:`pandas.DataFrame` or :class:`xarray.Dataset`) -- Climate data that should include ``prcp`` and ``tmin``.
                   * **t_rain** (:class:`float`, *optional*) -- Threshold for temperature for considering rain, defaults to 2.5 degrees C.
                   * **t_snow** (:class:`float`, *optional*) -- Threshold for temperature for considering snow, defaults to 0.6 degrees C.

      :returns: :class:`pandas.DataFrame` or :class:`xarray.Dataset` -- Input data with ``snow (mm/day)`` column if input is a ``pandas.DataFrame``,
                or ``snow`` variable if input is an ``xarray.Dataset``.

      .. rubric:: References

      .. footbibliography::


   .. py:method:: years_todict(years)

      Set date by list of year(s).


   .. py:method:: years_tolist(years)

      Correct dates for Daymet accounting for leap years.

      Daymet doesn't account for leap years and removes Dec 31 when
      it's leap year.

      :Parameters: **years** (:class:`list`) -- A list of target years.

      :returns: :class:`list` -- All the dates in the Daymet database within the provided date range.



