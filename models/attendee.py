from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Attendee(models.Model):
    _inherit = 'res.partner'

    course_ids = fields.Many2many(comodel_name='courses.course',string='Courses')
    instructor_id = fields.Many2one(comodel_name='hr.employee',string='Instructor',domain=[('department_id.name','=','Teaching')])

    @api.constrains('instructor_id')
    def _check_instructor(self):
        if self.instructor_id.work_contact_id.id == self.id:
            raise ValidationError("Instructor and Attendee can't be the same")

    @api.constrains('course_ids')
    def _check_courses(self):
        # if the attendee is an instructor of this course raise error
        for course in self.course_ids:
            if course.instructor_id.work_contact_id.id == self.id:  
                raise ValidationError('%s is an instructor of %s'%(self.name,course.name))