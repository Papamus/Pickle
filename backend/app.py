from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from auth_utils import hash_password, check_password
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['JWT_SECRET_KEY'] = 'super-secret-password' # Change this!
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)  # In a real app, ensure this is hashed
    last_login_date = db.Column(db.DateTime, nullable=True)
    daily_pickles = db.Column(db.Integer, default=0)

@app.route('/register', methods=['POST'])
def register_user():
    # Get data from request
    username = request.json.get('username', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    # Validate data
    if not username or not email or not password:
        return jsonify({"msg": "Missing required fields"}), 400
    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({"msg": "Email already exists"}), 400
    
    # Hash password
    hashed_password = hash_password(password)

    # Create new User instance and add to database
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    # Return success response
    return jsonify({"msg": "User created successfully"}), 201

@app.route('/login', methods=['POST'])
def login_user():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(username=username).first()
    if not user or not check_password(user.password, password):
        return jsonify({"msg": "Bad username or password"}), 401
    else:
        user.last_login_date = datetime.datetime.now()
        db.session.commit()
        access_token = create_access_token(identity=username, expires_delta=datetime.timedelta(days=1))
        return jsonify(access_token=access_token), 200

# 6. Implement Pickle Tracking
# @app.route('/pickles', methods=['POST'])
# def update_pickles():
#     # Update daily_pickles for the user
#     # Return updated count

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True)