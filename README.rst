Introduction
============

This products contain a simple view for a folder that contain some FeedFeederFolder.
It take 10 FeedItems in each FeedFeedFolder and present it in jquery Accordeon.

Installation
============

Add this product to your buildout with mr.developer

[buildout]
...
extensions = 
    mr.developer

sources = sources
auto-checkout =
    collective.ffcentral

[instance]
...
eggs =
  collective.ffcentral
..

[sources]
collective.ffcentral  = git git://github.com/tristanlt/collective.ffcentral.git

Activation
==========
In the folder which contain FeedFeedFolder(s)
http://localhost:8080/Plone/testfolder/foldselectViewTemplate?templateId=ffcentral_view
