# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName


def install(portal, reinstall=False):
    setup_tool = getToolByName(portal, 'portal_setup')
    qi = getToolByName(portal, 'portal_quickinstaller')
    if not reinstall and not qi.isProductInstalled('collective.twitter.accounts'):
        setup_tool.runAllImportStepsFromProfile('profile-collective.twitter.portlets:initial')

    setup_tool.runAllImportStepsFromProfile('profile-collective.twitter.portlets:default')
    return "Ran all uninstall steps."


def uninstall(portal, reinstall=False):
    if not reinstall:
        setup_tool = getToolByName(portal, 'portal_setup')
        setup_tool.runAllImportStepsFromProfile('profile-collective.twitter.portlets:uninstall')
        return "Ran all uninstall steps."
