+++++++++++



.. Contents::



PREREQUISITES
=============

cmptcomplexity requires the following software installed for your platform:


1) spacy

Type::

  pip3 install spacy --user
  python3 -m spacy download en

2) google
Type::

  pip3 install google --user

3) newspaper
Type::

  pip3 install newspaper --user

4) twython
Type::

    pip3 install twython --user

INSTALLING ptvalidator
======================

Development version from Git
----------------------------
Use the command::

 pip3 install git+https://github.com/AGHPythonCourse2017/zad3-moskalap.git --user

UNINSTALLING
============
Type::

  pip3 uninstall ptvalidator

USING ptvalidator
=================
BASIC USE
---------

To run ptvalidator after installation, first, you have to import module

   >>> import ptvalidator.checkit as checkit

To get information whether the information is true or not use


   >>> results = checkit.validate(query, key, verbose_log=True)

After executing this, you can:

    >>> results.is_true
    >>> results.display_sources()


    .. image:: https://raw.githubusercontent.com/AGHPythonCourse2017/zad2-moskalap/master/docs/img/sorted_plot.png?token=AWCREl9JX-_57k3FLB0UyIl52kAYEdNHks5ZFyCJwA%3D%3D



For more information read see jupyter example
