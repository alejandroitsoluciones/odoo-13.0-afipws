{
    "name": "account_move_tax",
    'version': '13.0.1.0.0',
    'category': 'Localization/Argentina',
    'sequence': 14,
    'author': 'Str3n6th 4r Security Systems - Argentina',
    'license': 'AGPL-3',
    'summary': '',
    'depends': [
        'l10n_ar_afipws',
        'uom',
        'l10n_latam_invoice_document',
        'l10n_ar',
        'account'
    ],
    'external_dependencies': {
    },
    'data': [
        'views/move_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
    ],
    'images': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
