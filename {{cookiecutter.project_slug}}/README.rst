{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{ cookiecutter.project_short_description }}

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `orseni/cookiecutter-bottle-pydbwrapper`_ project template.

.. _Cookiecutter: https://github.com/orseni/cookiecutter-bottle-pydbwrapper
