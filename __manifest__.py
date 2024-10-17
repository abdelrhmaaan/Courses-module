{
    'name': 'Courses',
    'version': '17.0',
    'description': 'Manage Your Courses',
    'summary': '',
    'author': 'Abdelrhman Gouda',
    'website': '',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'base',
        'hr',
        'website',
        'contacts'
    ],
    'data': [
        'security/ir.model.access.csv',
        # data
        'data/department.xml',
        'data/website_menu.xml',
        #views
        'views/courses_view.xml',
        'views/instructors_view.xml',
        'views/attendee_view.xml',
        #website
        'views/courses_website.xml',
        # menus
        'views/menu_items.xml',
        #reports
        'reports/courses_report.xml',

    ],
    'auto_install': False,
    'application': True,
}
