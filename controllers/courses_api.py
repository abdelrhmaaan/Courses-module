from odoo import http
from odoo.http import request

class CourseController(http.Controller):

    @http.route('/courses/add', type='json', auth='user', methods=['POST'])
    def add_course(self, **kwargs):
        # Extract data from the request
        course_data = {
            'name': kwargs.get('name'),
            'instructor_id': kwargs.get('instructor_id'),
            'room_id': kwargs.get('room_id'),
            'start_date': kwargs.get('start_date'),
        }

        # Create course
        if not course_data['name']:
            return { 'Message': 'Missing Data field name' }

        new_course = request.env['courses.course'].sudo().create(course_data)
        return {'success': True, 'course_id': new_course.id}

    @http.route('/courses/update/<int:course_id>', type='json', auth='user', methods=['PUT'])
    def update_course(self, course_id,**kwargs):
        course = request.env['courses.course'].sudo().browse(course_id)
        if not course:
            return {'success': False, 'message': 'Course not found'}
        # Update course details
        if kwargs:
            course.write({
                'name': kwargs.get('name', course.name),
                'instructor_id': kwargs.get('instructor_id', course.instructor_id.id),
                'room_id': kwargs.get('room_id', course.room_id.id),
                'start_date': kwargs.get('start_date', course.start_date),
            })
            return {'success': True, 'message': 'Course updated successfully'}
        else:
            return {'message':'Please you need to add data'}

    @http.route('/courses', type='json', auth='user', methods=['GET'])
    def get_courses(self,**kwargs):
        
        instructor_id = kwargs.get('instructor_id', None)

        # Search for courses based on the presence of instructor_id
        domain = []
        if instructor_id:
            domain = [('instructor_id', '=', instructor_id)]

        # Fetch the courses based on the domain
        courses = request.env['courses.course'].sudo().search(domain)
        
        # Prepare the list of courses to return
        course_list = []
        for course in courses:
            course_list.append({
                'id': course.id,
                'name': course.name,
                'start_date': course.start_date,
                'room': course.room_id.name,
                'attendees': course.attendee_ids.mapped('name')
            })
        
        return {'courses': course_list}