# -*- coding: utf-8 -*-
##########################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
##########################################################################

{
    'name': 'Odoo Fleet Traccar Tracking',
    'version': '1.0.3',
    'category': 'Generic Modules',
    'author': 'Webkul Software Pvt. Ltd.',
    'website': 'https://store.webkul.com/Odoo-Fleet-Traccar-Tracking.html',
    'sequence': 1,
    'summary': 'Basic Traccar Application',
    'description': """This module works very well with Odoo 14.0""",
    'depends': [
        'fleet',
        'base_geolocalize',
        'wk_wizard_messages'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/template.xml',
        'data/trip_cron.xml',
        'data/trip_sequence.xml',
        'wizard/tracking_history_wizard_view.xml',
        'views/traccar_configuration_views.xml',
        'views/fleet_vehicle_views.xml',
        'views/trip_details_views.xml',
        'views/traccar_action_views.xml',
        'views/traccar_menus.xml'
    ],

    'application': True,
    'images'     : ['static/description/Banner.png'],
    'installable': True,
    'auto_install': False,
	'price'      :  149,
	'currency'   : 'USD',
    'pre_init_hook': 'pre_init_check',
}
