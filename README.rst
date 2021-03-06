Important
=========

This app has been discontinued and is no longer maintained.

cmsplugin-blog-seo-addons
==========================

Allows to add meta descriptions to a cmsplugin-blog Entry.

An extension for `cmsplugin-blog <https://github.com/fivethreeo/cmsplugin-blog/>`_
which lets you add meta description to a blog entry.

Installation
------------

You need to install the following prerequisites in order to use this app:

* Django
* South
* django-cms
* cmsplugin-blog

If you want to install the latest stable release from PyPi::

    $ pip install cmsplugin-blog-seo-addons

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/cmsplugin-blog-seo-addons.git#egg=cmsplugin_blog_seo_addons

Add ``cmsplugin_blog_seo_addons`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'cmsplugin_blog_seo_addons',
    )


Usage
-----

Just write a blog Entry and you will see a new inline for meta description in
the Entry admin.


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
