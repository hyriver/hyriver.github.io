pygeohydro.levee
================

.. py:module:: pygeohydro.levee

.. autoapi-nested-parse::

   Accessing National Flood Hazard Layers (NLD) through web services.





Module Contents
---------------

.. py:class:: NLD(layer, outfields = '*', crs = 4326)



   Access National Levee Database (NLD) services.

   .. rubric:: Notes

   For more info visit: https://geospatial.sec.usace.army.mil/server/rest/services/NLD2_PUBLIC/FeatureServer

   :Parameters: * **layer** (:class:`str`, *optional*) -- A valid service layer. Valid layers are:

                  - ``boreholes``
                  - ``crossings``
                  - ``levee_stations``
                  - ``piezometers``
                  - ``pump_stations``
                  - ``relief_wells``
                  - ``alignment_lines``
                  - ``closure_structures``
                  - ``cross_sections``
                  - ``embankments``
                  - ``floodwalls``
                  - ``frm_lines``
                  - ``pipe_gates``
                  - ``toe_drains``
                  - ``leveed_areas``
                  - ``system_routes``
                  - ``pipes``
                  - ``channels``
                * **outfields** (:class:`str` or :class:`list`, *optional*) -- Target field name(s), default to "*" i.e., all the fields.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- Target spatial reference, default to ``EPSG:4326``.

   .. method:: bygeom(geom, geo_crs=4326, sql_clause="", distance=None, return_m=False, return_geom=True)

      Get features within a geometry that can be combined with a SQL where clause.

   .. method:: byids(field, fids, return_m=False, return_geom=True)

      Get features by object IDs.

   .. method:: bysql(sql_clause, return_m=False, return_geom=True)

      Get features using a valid SQL 92 WHERE clause.
      

   .. rubric:: Examples

   >>> from pygeohydro import NLD
   >>> nld = NLD("levee_stations")
   >>> levees = nld.bygeom((-105.914551, 37.437388, -105.807434, 37.522392))
   >>> levees.shape
   (1838, 12)


