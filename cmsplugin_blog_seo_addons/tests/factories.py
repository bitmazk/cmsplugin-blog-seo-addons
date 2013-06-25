"""Factories for the ``cmsplugin_blog_seo_addons`` app."""
import factory
from cmsplugin_blog.models import Entry
from django_libs.tests.factories import SimpleTranslationMixin

from ..models import SEOAddon, SEOAddonTranslation


class EntryFactory(factory.Factory):
    """Factory for the ``Entry`` model."""
    FACTORY_FOR = Entry


class BaseSEOAddonFactory(factory.Factory):
    """Factory for the ``EntrySEOAddon`` model."""
    FACTORY_FOR = SEOAddon


class SEOAddonFactory(SimpleTranslationMixin, BaseSEOAddonFactory):
    FACTORY_FOR = SEOAddon

    @staticmethod
    def _get_translation_factory_and_field():
        return (SEOAddonTranslationFactory, 'seoaddon')


class SEOAddonTranslationFactory(factory.Factory):
    """Factory for the ``EntrySEOAddonTranslation`` model."""
    FACTORY_FOR = SEOAddonTranslation

    meta_description = factory.Sequence(
        lambda n: 'Meta description {}'.format(n))
    seoaddon = factory.SubFactory(BaseSEOAddonFactory)
