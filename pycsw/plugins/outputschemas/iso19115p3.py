from pycsw.core import util
from pycsw.core.etree import etree

NAMESPACE = 'http://standards.iso.org/iso/19115/-3/mdb/2.0'
NAMESPACES = {'mdb': NAMESPACE}

def write_record(result, esn, context, url=None):
    """Minimal ISO19115-3 serializer"""
    typename = util.getqattr(result, context.md_core_model['mappings']['pycsw:Typename'])
    if esn == 'full' and typename == 'mdb:MD_Metadata':
        return etree.fromstring(util.getqattr(result, context.md_core_model['mappings']['pycsw:XML']), context.parser)

    node = etree.Element(util.nspath_eval('mdb:MD_Metadata', NAMESPACES))
    node.attrib[util.nspath_eval('xsi:schemaLocation', context.namespaces)] = \
        '%s https://schemas.isotc211.org/19115/-3/mdb/2.0/mdb.xsd' % NAMESPACE

    etree.SubElement(node, util.nspath_eval('mdb:fileIdentifier', NAMESPACES)).text = \
        util.getqattr(result, context.md_core_model['mappings']['pycsw:Identifier'])
    etree.SubElement(node, util.nspath_eval('mdb:title', NAMESPACES)).text = \
        util.getqattr(result, context.md_core_model['mappings']['pycsw:Title'])
    etree.SubElement(node, util.nspath_eval('mdb:abstract', NAMESPACES)).text = \
        util.getqattr(result, context.md_core_model['mappings']['pycsw:Abstract'])

    return node
