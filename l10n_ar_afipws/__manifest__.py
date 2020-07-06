{
    "name": "Modulo Base - Factura Electrónica Argentina",
    'version': '13.0.1.0.0',
    'category': 'Localization/Argentina',
    'sequence': 14,
    'author': 'Str3n6th 4r Security Systems - Argentina',
    'license': 'AGPL-3',
    'summary': '',
    'depends': [],
    'external_dependencies': {
        'python': ['pyafipws', 'OpenSSL', 'pysimplesoap']
    },
    'data': [
        'wizard/upload_certificate_view.xml',
        'views/afipws_menuitem.xml',
        'views/afipws_certificate_view.xml',
        'views/afipws_certificate_alias_view.xml',
        'views/afipws_connection_view.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
    ],
    'demo': [
        'demo/certificate_demo.xml',
        'demo/parameter_demo.xml',
    ],
    'images': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
