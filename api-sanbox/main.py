from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class BookingModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    person = db.Column(db.String(100), nullable = False)
    vehicle = db.Column(db.Integer, nullable=False)
    service = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Booking(person={self.person}, vehicle={self.vehicle}, service={self.service})"


# db.create_all()

booking_put_args = reqparse.RequestParser()
booking_put_args.add_argument('person', type=str, help="Name of the person is required", required=True)
booking_put_args.add_argument('vehicle', type=str, help="Name of the vehicle is required", required=True)
booking_put_args.add_argument('service', type=str, help="Service is required", required=True)

resource_fields ={
    'id': fields.Integer,
    'person': fields.String,
    'vehicle': fields.String,
    'service': fields.String
}

class Booking(Resource):
    @marshal_with(resource_fields) #Serialize the output of the query
    def get(self,booking_id):
        result = BookingModel.query.get(booking_id)
        if not result:
            abort(404, message="Sorry, could not find booking with that id")
        return result

    @marshal_with(resource_fields)
    def put(self, booking_id):
        args = booking_put_args.parse_args()
        already_exist = BookingModel.get(booking_id)
        if already_exist:
            abort(409, message="Booking id already registers, please modify the id")
        new_booking = BookingModel(
            id=booking_id,
            person=args['person'],
            vehicle= args['vehicle'],
            service=args['service']
        )
        db.session.add(new_booking)
        db.session.commit() # I add the register permantly to the db
        return new_booking, 201

    def __delete__(self, booking_id):
        return  'deleted',204

#TODO: add the path method
api.add_resource(Booking, "/booking/<int:booking_id>")
if __name__ == '__main__':
    app.run(debug=True)