from plone.testing import z2

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting, FunctionalTesting

class Layer(PloneSandboxLayer):
    default_bases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.ffcentral
        self.loadZCML(package=collective.ffcentral)

        # Install product and call its initialize() function
        z2.installProduct(app, 'collective.ffcentral')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'collective.ffcentral:default')

    def tearDownZope(self, app):
        # Uninstall product
        z2.uninstallProduct(app, 'collective.ffcentral')

FIXTURE = Layer()

INTEGRATION = IntegrationTesting(bases=(FIXTURE,),
                        name="collective.ffcentral:Integration")
FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,),
                        name="collective.ffcentral:Functional")
