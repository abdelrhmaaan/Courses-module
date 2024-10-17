from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Courses(models.Model):
    _name = 'courses.course'
    _description = 'Courses'

    name = fields.Char('Course Name',required=True)
    instructor_id = fields.Many2one(comodel_name='hr.employee',string='Instructor',domain=[('department_id.name','=','Teaching')])
    room_id = fields.Many2one(comodel_name='courses.room',string='Room')
    start_date = fields.Date(string='Starting Date')
    description = fields.Text(string='Description')
    attendee_ids = fields.Many2many(comodel_name='res.partner',string='Attendees')
    lesson_ids = fields.One2many('courses.lesson',inverse_name='course_id')

    # do a constrain for room
    @api.constrains('attendee_ids','room_id')
    def _attendee_constrain(self):
        if self.attendee_ids:
            if len(self.attendee_ids) > self.room_id.capacity :
                raise ValidationError("No of attendees is more than %s capacity"%self.room_id)

    @api.constrains('instructor_id','attendee_ids')
    def _instructor_constrain(self):
        if self.instructor_id.work_contact_id.id in self.attendee_ids.mapped('id'):
            raise ValidationError("Instructor can't be an Attendee")


class Room(models.Model):
    _name = 'courses.room'

    name = fields.Char('Name',required=True)
    capacity = fields.Integer('Room Capacity',required=True)
    # no_attendees = fields.Integer('Num Of Attendees',readonly=True)


class Lesson(models.Model):
    _name = 'courses.lesson'

    name = fields.Char('Lesson Name',required=True)
    course_id = fields.Many2one(comodel_name='courses.course',string='Course')
    room_id = fields.Many2one(comodel_name='courses.room',string='Room')
