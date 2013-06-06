Installation
------------

To enable this product in a buildout-based installation:

Edit your buildout.cfg and add ``collective.twitter.portlets`` to the list
of eggs to install::

    [buildout]
    ...
    eggs =
        collective.twitter.portlets


After updating the configuration you need to run ''bin/buildout'', which will
take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the 'Add-ons' link.

Check the box next to ``collective.twitter.portlets`` and click the 'Activate'
button.

Note: You may have to empty your browser cache and save your resource
registries in order to see the effects of the product installation.

