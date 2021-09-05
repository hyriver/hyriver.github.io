:py:mod:`pydaymet.core`
=======================

.. py:module:: pydaymet.core

.. autoapi-nested-parse::

   Core class for the Daymet functions.



Module Contents
---------------

.. py:class:: Daymet(variables = None, pet = False, time_scale = 'daily', region = 'na')

   Base class for Daymet requests.

   :Parameters: * **variables** (:class:`str` or :class:`list` or :class:`tuple`, *optional*) -- List of variables to be downloaded. The acceptable variables are:
                  ``tmin``, ``tmax``, ``prcp``, ``srad``, ``vp``, ``swe``, ``dayl``
                  Descriptions can be found `here <https://daymet.ornl.gov/overview>`__.
                  Defaults to None i.e., all the variables are downloaded.
                * **pet** (:class:`bool`, *optional*) -- Whether to compute evapotranspiration based on
                  `UN-FAO 56 paper <http://www.fao.org/3/X0490E/x0490e06.htm>`__.
                  The default is False
                * **time_scale** (:class:`str`, *optional*) -- Data time scale which can be daily, monthly (monthly summaries),
                  or annual (annual summaries). Defaults to daily.
                * **region** (:class:`str`, *optional*) -- Region in the US, defaults to na. Acceptable values are:

                  * na: Continental North America
                  * hi: Hawaii
                  * pr: Puerto Rico

   .. py:method:: check_dates(dates)
      :staticmethod:

      Check if input dates are in correct format and valid.


   .. py:method:: dates_todict(self, dates)

      Set dates by start and end dates as a tuple, (start, end).


   .. py:method:: dates_tolist(self, dates)

      Correct dates for Daymet accounting for leap years.

      Daymet doesn't account for leap years and removes Dec 31 when
      it's leap year.

      :Parameters: **dates** (:class:`tuple`) -- Target start and end dates.

      :returns: :class:`list` -- All the dates in the Daymet database within the provided date range.


   .. py:method:: years_todict(self, years)

      Set date by list of year(s).


   .. py:method:: years_tolist(self, years)

      Correct dates for Daymet accounting for leap years.

      Daymet doesn't account for leap years and removes Dec 31 when
      it's leap year.

      :Parameters: **years** (:class:`list`) -- A list of target years.

      :returns: :class:`list` -- All the dates in the Daymet database within the provided date range.



