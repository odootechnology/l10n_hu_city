# -*- coding: utf-8 -*-
{
    "name": "Hungarian City database",
    "version": "1.0.",
    "icon": "/l10n_hu_city/static/description/l10n.png",
    "category": "Accounting/Localizations",
    "author": "Informatikai Üzleti Megoldások Kft. (Juhász Krisztián)",
    "website": "www.uzletimegoldasok.hu",
    "description": """
Official Hungarian county, city and zip code list  
This module provides a list of Hungarian counties, cities and their zip codes.

Hivatalos magyarországi megye, város és irsz. lista 
Ez a modul a magyar megyék, városok és azok postai irányítószámai listáját tartalmazza.

Origin/Forrás: https://net.posta.hu/dashboard/public/dashboard-ui/iranyitoszam-kereso/download-as-table
Date: (XLSX; 987 KB, updated/frissítve: 2025.05.27)
    """,
    "depends": ["l10n_hu", "base_address_extended"],
    "data": [
        "data/res_state_data.xml",
        "data/res_city_data.xml",
        "data/res_country_data.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
#    "cloc_exclude": ["**/*"],
    "demo": [],
    'images': [
        'static/description/banner.png',
    ],
    'tags': ['localization', 'hungary', 'configuration'],

    # Version requirements
    'odoo_version': '18.0',
    'python_version': '>=3.11',
}
