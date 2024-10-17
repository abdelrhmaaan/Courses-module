from odoo import http
from odoo.http import request

class CourseController(http.Controller):

    @http.route('/coursespage', type='http', auth='public', methods=['GET'],website=True)
    def courses_page(self):
        courses = request.env['courses.course'].sudo().search([])
        print(courses)
        return request.render(template='courses.courses_page_template',qcontext={'courses':courses})